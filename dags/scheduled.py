from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

import datetime 

from default_args import args 

def the_task():
    print('the task is running', datetime.datetime.now())

dag = DAG(
    dag_id='scheduled-dag',
    default_args=args,
    schedule_interval='*/1 * * * *',
)

task = PythonOperator(
    task_id='scheduled-task',
    python_callable=the_task,
    dag=dag,
)