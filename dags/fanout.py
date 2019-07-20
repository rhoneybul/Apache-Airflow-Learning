from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

from default_args import args

dag = DAG(
    dag_id="fanout-dag",
    default_args=args,
    schedule_interval=None
)

def core_task():
    print('The core task has started. Now fanning out.')
    return 

coreTask = PythonOperator(
    task_id='core-task',
    python_callable=core_task,
    dag=dag,
)

def fanned_out(index):
    print('fannout out, with index: ', index)
    return 

for i in range(10):
    fannoutTask = PythonOperator(
        task_id=f'fannout-{i}',
        python_callable=fanned_out,
        op_kwargs={'index': i},       
        dag=dag, 
    )
    coreTask >> fannoutTask