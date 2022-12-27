from datetime import datetime, timedelta, timezone
import os

from airflow.exceptions import AirflowFailException
from airflow.decorators import dag, task
from airflow.models import Variable
from airflow.operators.python import get_current_context
from airflow.providers.http.operators.http import SimpleHttpOperator

from plugins.schemas import ApiResponse
from plugins.db import models
from plugins.db.session import session
from plugins.utils import handle_response


count_next_matches = int(Variable.get("LAST_MATCHES_CNT"))
season_id = Variable.get("SEASON_ID")
api_key = os.environ.get("APIKEY")

headers = {
    "apikey": api_key
}

default_args = {
    'start_date': datetime(2022, 1, 1),
    'retries': 1,
}


@dag(
    default_args=default_args,
    schedule_interval=timedelta(hours=1),
    catchup=False
)
def next_matches():
    get_data = SimpleHttpOperator(
        http_conn_id='TESTAPI',
        task_id="get_data",
        method="GET",
        headers=headers,
        data={
            "season_id": season_id,
            "date_from": '{{ ds }}',
        },
        extra_options={
            "timeout": 10,
        },
        response_check=lambda response: handle_response(response)
    )

    @task
    def filter_data(response: str) -> str:
        exec_time = get_current_context()["data_interval_end"]
        try:
            data_obj = ApiResponse.parse_raw(response)
        except Exception as exc:
            raise AirflowFailException(str(exc))

        actual_data = []
        for match in data_obj.data:
            if len(actual_data) >= count_next_matches:
                break

            dt = datetime.strptime(match.match_start, "%Y-%m-%d %H:%M:%S")
            dttz = dt.replace(tzinfo=timezone.utc)

            if dttz > exec_time:
                actual_data.append(match)

        data_obj.data = actual_data

        return data_obj.json()

    @task
    def load_data(data: str) -> None:
        exec_time = get_current_context()["data_interval_end"]

        with session() as s:
            item = models.NextMatches(
                datetime=exec_time,
                data=data,
            )
            s.add(item)
            s.commit()

    load_data(filter_data(get_data.output))


dag = next_matches()
