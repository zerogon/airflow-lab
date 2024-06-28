from __future__ import annotations

import datetime

import pendulum

from airflow.models.dag import DAG
from airflow.operators.python import PythonOperator
from airflow.decorators import task
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 6 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"),
    catchup=False
) as dag:
    regist2_t1 = PythonOperator(
        task_id='regist2_t1',
        python_callable=regist2,
        op_args=['zerogon','man','kr','seoul'],
        op_kwargs={'email' : 'ss@na.com', 'phone' : '010'}
    )
regist2_t1
'''
def regist2(name, sex, *args,**kwargs):
    print(f'이름: {name}')
    print(f'성별: {sex}')
    print(f'기타옵션: {args}')
    email = kwargs['email'] or None
    phone = kwargs['phone'] or None
    if email :
        print(email)
    if phone :
        print(phone)
'''