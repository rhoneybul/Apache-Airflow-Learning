from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

import datetime

from default_args import args

dag = DAG(
    dag_id='helloworld-dag',
    default_args=args,
    schedule_interval=None
)


def basic_task():
    print('basic task initialised.')
    return 'basic task.'



task = PythonOperator(
    task_id='first.tag',
    python_callable=basic_task,
    dag=dag
)

