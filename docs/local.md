* checklist for python setup

```
OK jupyter lab
OK ipython
OK pylint
OK pytest
OK import module
OK load file
OK read/write file
OK matplotlib
OK plotly
OK flask
OK dash
OK airflow
OK postgres
OK snowflake
OK sqlite
```

```
python py/app/flask_app.py
```

```
python py/app/dash_app.py
```

```
python py/app/dash_app.py
```


* background tasks

```
jobs
kill
ps
fg
bg
```

ctrl+z

```
ipython
```

* PYTHONPATH should include `py` directory for Docker equivalency
* other PATHS should be set as variables or accessible from $PROJECT

* running tests

```
(tufterati) ~/Projects/tufterati $ pytest py/tests                            
/Users/M_Percival/anaconda3/envs/tufterati/lib/python3.7/site-packages/dash/testing/plugin.py:17: UserWarning:

run `pip install dash[testing]` if you need dash.testing

=================================================================== test session starts ===================================================================
platform darwin -- Python 3.7.4, pytest-5.3.2, py-1.8.0, pluggy-0.13.1
rootdir: /Users/M_Percival/Projects/tufterati
plugins: dash-1.4.1
collected 1 item                                                                                                                                          

py/tests/test_utils/test_db_utils.py .                                                                                                              [100%]

==================================================================== 1 passed in 0.02s ====================================================================
```
