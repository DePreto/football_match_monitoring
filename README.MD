<h1 align="center">Football matches monitoring

[![API URL](https://lh3.googleusercontent.com/yu4XcUAnsY8nnov3l6rSZBKELkc5mEGlL5I4n4b1SX3SDH209XEJGP2CN2Pg9VpIbl0=s180)](https://sportdataapi.com/football-soccer-api/) 
</h1>

***

## Краткое описание

Проектом реализован мониторинг ближайших футбольных матчей с настраиваемой периодичностью с использованием оркестратора Apache Airflow.


**Для разработки и функционирования проекта используется открытый API, который расположен на сайте [Footbal API](https://sportdataapi.com/football-soccer-api/).**

***


## Особенности
<ul>
	<li>В проект внедрён alembic и исполнение `alembic upgrade head` при поднятии сборки, что позволяет поднимать сборку с актуальным состоянием БД.
	<li>Для расширения переменных и соединений `Airflow` достаточно расширить существующие файлы `connections.json` & `variables.json`, которые наполняют airflow при поднятии сборки.
	<li>В качестве валидатора API response используется Pydantic.
	</li>
</ul>

***

## Локальная установка
Эти инструкции помогут вам развернуть проект на локальном компьютере для разработки и тестирования

**Перед тем, как начать:**
- Если вы не пользуетесь `Python 3`, вам нужно установить инструмент `virtualenv` при помощи `pip install virtualenv`. 
Если вы используете `Python 3`, у вас уже установлен модуль [venv](https://docs.python.org/3/library/venv.html) в стандартной библиотеке.


### Запуск проекта (Linux Ubuntu)

- Создайте на своем компютере папку проекта
- Склонируйте этот репозиторий в папку проекта `git clone https://github.com/...`
- Создайте файл `.env` и добавьте в него переменные окружения:
```
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow

APP_POSTGRES_SERVER=app_db
APP_POSTGRES_USER=postgres
APP_POSTGRES_PASSWORD=password
APP_POSTGRES_DB=app

APIKEY=**YOURAPIKEY** (временно ae9829f0-8530-11ed-aef1-1ba6f6d0a081)

PGADMIN_DEFAULT_EMAIL = test@mail.ru
PGADMIN_DEFAULT_PASSWORD = password
PGADMIN_LISTEN_ADDRESS = [0.0.0.0.]
PGADMIN_LISTEN_PORT=8081
```
- Настройка пользовательских прав `Airflow`: `echo -e "AIRFLOW_UID= $( id -u ) \nAIRFLOW_GID=0" > .env`
- Запустите сборку командой `docker-compose up --build -d` из Терминала из папки с проектом 

**Для разработки**:
- Создайте/Активируйте виртуальное окружение `python3 -m venv venv && source venv/bin/activate`
- Установите все зависимости `pip install -r requirements.txt`


**Доступные ресурсы**:
- `Apache airflow`: http://localhost:8080/
- `PGADMIN`: http://localhost:8081/

***

## В разработке использованы

- [Python 3.10](https://www.python.org/)
- [Apache Airflow 2.3](https://airflow.apache.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Docker](https://www.docker.com/)
- [FootballAPI](https://sportdataapi.com/football-soccer-api/)
