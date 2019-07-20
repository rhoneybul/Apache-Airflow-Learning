from airflow.operators.python_operator import PythonOperator
from airflow.models import DAG

import datetime

args = {
    'owner': 'rhoneybul',
    'start_date': datetime.datetime.now() - datetime.timedelta(5),
}

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