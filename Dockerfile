FROM apache/airflow:2.3.0

RUN pip install apache-airflow-providers-http
RUN pip install apache-airflow-providers-postgres
RUN pip install pydantic

ENV PYTHONPATH "${PYTHONPATH}:/opt/airflow"
