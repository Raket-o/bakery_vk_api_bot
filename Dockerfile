#FROM python:3.12-slim
#
#ENV PYTHONUNBUFFERED=1
#
#RUN pip install --upgrade pip "poetry"
#RUN poetry config virtualenvs.create false --local
#COPY pyproject.toml poetry.lock ./
#RUN poetry install
#
#COPY ./config_data ./config_data
#COPY alembic.ini alembic.ini
#COPY alembic alembic
#COPY .env .env
#COPY ./app ./app
#
#ENTRYPOINT ["./app/docker-entrypoint.sh"]


FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

RUN mkdir /app

COPY ./requirements.txt /app/

RUN python -m pip install --upgrade pip

RUN python -m pip install -r /app/requirements.txt

#COPY . /app/
#COPY ../.env /app/
#COPY ../app /app/
#COPY ../database /app/
#COPY ../config_data /app/

WORKDIR /app
