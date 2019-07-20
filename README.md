# Apache-Airflow-Learning

This repository contains exercises I went through while learning how to use Apache Airflow

## Getting Started

To start the apache airflow webserver, and corresponding database, use `docker-compose up -d`.

The DAGS are contained in the dags folder, which is subsequently volume mounted to the airflow system.

## Learning Points

The following gives some points of learning which I have found so far;

* Airflow throws errors when trying to use the `start_date`, as `datetime.datetime.now()`. To solve this, I started using `datetime.datetime.now() - datetime.timedelta(1)`.
* If you name a DAG with dogs in the name, the CSS selectors become invalid in the UI, and the `Recent Tasks`, and `DAG Runs`, are empty.
* If you forget to specify the `dag` for a task, then Airflow will raise an exception for `Task is missing the start_date parameter`.
* The best way to debug is using the logs from the airflow container. The airflow container will restart every 10s or so. The logs from airflow will indicate the success of adding the new dag.
* We can add variables in airflow, and access them as follows;

```
from airflow.models import Variable 

Variable.get('<variable_name>')
```

* Trying to use the s3 operator with the default dockerfile caused issues. Hence, I had to pull the dockerfile, and added a `pip install botocore` step into the dockerfile.


