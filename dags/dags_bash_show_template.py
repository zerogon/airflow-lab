from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.decorators import task

with DAG(
    dag_id="dags_bash_with_template",
    schedule="30 9 * * *",
    start_date=pendulum.datetime(2024, 6, 5, tz="Asia/Seoul"),
    catchup=True
) as dag:
    @task(task_id = 'python_task')
    def show_templates(**kwargs):
        from pprint import pprint
        pprint(kwargs)
