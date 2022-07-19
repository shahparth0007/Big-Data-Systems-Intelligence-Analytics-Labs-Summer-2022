# Airflow Tutorial

## STEP 1
Create virtual environment

`python3.9 -m venv airflow`

## STEP 2
Activate Virtual Environment

For macos/linx:

`source airflow/bin/activate`

For windows

`source activate.ps1`

## STEP 3

Set airflow home to current directory or airflow will make a default folder in users folder

`export AIRFLOW_HOME=${pwd}`

## STEP 4

Install Airflow with pip 

pip3 install 'apache-airflow[postgres,google]==2.3.3' --constraint https://raw.githubusercontent.com/apache/airflow/constraints-2.3.3/constraints-3.9.txt

