# tufterati

manipulate tables with SQL, pandas, plyr

## Purpose

Manipulate tabular data from a number of sources with modern tools.

## Prerequisites

Docker. VSCode for Python remote debugging.

## Getting started

* export the environment variables

```
source export_env.sh
```

* build the containers and launch the services

```
make build
make up
```

* run any of the commands in the `Makefile`, e.g.,

```
make psql
```

* run local ipython

```
conda activate tufterati
ipython
```

* run local jupyter lab

```
make lab
```

