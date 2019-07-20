from airflow.models import DAG, Variable
from airflow.hooks.S3_hook import S3Hook
from airflow.operators.python_operator import PythonOperator

import logging

from default_args import args 

def list_keys():
    hook = S3Hook(aws_conn_id='amazon-s3')
    bucket = Variable.get('s3-bucket')
    keys = hook.list_keys(bucket)
    for key in keys:
        logging.info(f'Listing S3 Keys::{key}')

dag = DAG(
    's3-list-keys',
    default_args=args,
)

list_task = PythonOperator(
    task_id='list-keys',
    python_callable=list_keys,
    dag=dag
)