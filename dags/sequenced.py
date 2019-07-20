from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

import datetime

from default_args import args 

def start_task():
    print('starting the task')
    return

def sequenced_task():
    print('the other one goes first...?')


dag = DAG(
    dag_id='sequenced-dag',
    default_args=args,
    schedule_interval=None
)

task = PythonOperator(
    task_id='first_task',
    python_callable=start_task,
    dag=dag
)

sequencedTask = PythonOperator(
    task_id='sequenced_task',
    python_callable=sequenced_task,
    dag=dag
)

task >> sequencedTask