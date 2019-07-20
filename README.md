# Apache-Airflow-Learning

This repository contains exercises I went through while learning how to use Apache Airflow

## Getting Started

To start the apache airflow webserver, and corresponding database, use `docker-compose up -d`.

The DAGS are contained in the dags folder, which is subsequently volume mounted to the airflow system.

## Learning Points

The following gives some points of learning which I have found so far;

* Airflow throws errors when trying to use the `start_date`, as `datetime.datetime.now()`. To solve this, I started using `datetime.datetime.now() - datetime.timedelta(1)`.
* If you name a DAG with dogs in the name, the CSS selectors become invalid in the UI, and the `Recent Tasks`, and `DAG Runs`, are empty.
