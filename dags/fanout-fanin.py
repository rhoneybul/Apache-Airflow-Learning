from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

import time 
import datetime

from default_args import args

dag = DAG(
    'fannout-fan-in',
    default_args=args,
    schedule_interval=None,
)

def start_task():
    print('start task.')
    return 

def fanned_task(index):
    print(f'fanned task: {index}, starting @ {datetime.datetime.now()}')
    time.sleep(5 * int(index))
    print(f'fanned task: {index} ending.')
    return 

def end_task():
    print('end task')
    return 

startTask = PythonOperator(
    task_id="start.task",
    python_callable=start_task,
    dag=dag
)

endTask = PythonOperator(
    task_id='end.task',
    python_callable=end_task,
    dag=dag
)

for i in range(10):
    ftask_i = PythonOperator(
        task_id=f'fanout.task.{i}',
        python_callable=fanned_task,
        op_kwargs={'index': i},
        dag=dag
    )
    startTask >> ftask_i >> endTask


