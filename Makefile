#!/usr/bin/env make
#
# makefile for project commands
#

app_root := ${PWD}
proj := ${PROJECT}
db_host_port := ${DB_POSTGRES_HOST_PORT}
local := ${DOCKER_IP}
jupy_port := ${JUPYTER_PORT}

SHELL := /usr/bin/env bash

env:
	@conda env create -f ${app_root}/py/environment.yml

lab:
	@jupyter lab --notebook-dir=${app_root}/py/lab --port=${jupy_port}

build:
	@docker-compose build

up:
	@docker-compose up -d

down:
	@docker-compose down

psql:
	@psql -h ${local} -p ${db_host_port} -U ${proj} -d ${proj}

bashdb:
	@docker exec -it ${proj}_db bash

bashpy:
	@docker exec -it ${proj}_py bash

bashrs:
	@docker exec -it ${proj}_rs bash

pyapp:
	@docker exec -it ${proj}_py python app/app.py

pydb:
	@docker exec -it ${proj}_py python app/db_app.py

flask:
	@docker exec ${proj}_py bash app/run_flask.sh > /dev/null 2>&1 &

dash:
	@docker exec ${proj}_py bash app/run_dash.sh > /dev/null 2>&1 &

air:
	@docker exec ${proj}_py bash app/run_airflow.sh

check_task:
	@docker exec ${proj}_py airflow test my_hello_dag print_hello 2019-10-22

run_dag:
	@docker exec ${proj}_py airflow trigger_dag my_hello_dag

rapp:
	@docker exec -it ${proj}_rs Rscript db_conn.R

putdata:
	@docker cp data/. ${proj}_rs:/data/

getdata:
	@docker cp ${proj}_rs:/data/. data/
