# tufterati

manipulate tables with SQL, pandas, plyr

## Purpose

Manipulate tabular data from a number of sources with modern tools.

## Prerequisites

Docker. VSCode for Python remote debugging.

## Getting started

* export the environment variables for Docker

```
source sh/export_env.sh .env
```

* build the containers and launch the services

```
make build
make up
```

* run any of the docker commands in the `Makefile`, e.g.,

```
make psql
```

* export the environment variables for Python

```
source sh/export_env.sh py/.env
```

* create the conda environment for local python

```
make env
```

* do the one-time build for plotly in Jupyter Lab

```
bash sh/setup_jupyter_plotly.sh
```

* run local ipython

```
conda activate ${PROJECT}
ipython
```

* run local jupyter lab

```
make lab
```


## Running tests

```
pytest py/tests
```

## Linting

```
pylint py/**/*.py
```

