## ETL Assignment

## Requirements

1. Python 3.7+ - [link](https://www.python.org/)
2. Docker/docker-compose [link](https://www.docker.com/)


## Run ETL job

1. Create virtual enviroment - [link](https://docs.python.org/3/library/venv.html).

2. Run below command:
```sh
pip install -r requirements.txt
```
3. Run job:
```sh
python run_etl.py --destination db --transformation test_utilization
```
Aviaible options:
destination - db (postgres database) or dir (local directory)
transformation - test_utilization / test_average_scores

## Run tests

```sh
pytest -v
```