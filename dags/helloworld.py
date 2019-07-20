from airflow.models import DAG
from airflow.operators.python_operator import PythonOperator

import datetime

args = {
    'owner': 'rhoneybul',
    'start_date': datetime.datetime.now() - datetime.timedelta(1),
}

dag = DAG(
    dag_id='helloworld.dag',
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

