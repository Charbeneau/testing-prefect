# prefect-cloud-local

Here I try to get off the ground unit testing [Prefect](https://www.prefect.io/cloud/) with [Pytest](https://docs.pytest.org/en/7.2.x/).

# Requirements
    - A Prefect Cloud 2 account
    - [Python 3](https://www.python.org/) (I used Python 3.11.2)
    - [Make](https://www.gnu.org/software/make/) (I used 3.81)

# Usage

0. Sign into [Prefect Cloud 2](https://app.prefect.cloud/auth/login).

1. Create a new Workspace.
```sh
Owner:  [YOUR EMAIL ADDRESS WITHOUT ANY PERIODS]
Workspace Name:  prefect-cloud-local
Description (Optional):
```

2. Create an [API key](https://app.prefect.cloud/my/api-keys), **and copy its value ("[API_KEY_VALUE]") for step 3 below**.
```sh
Name:  prefect-cloud-local
Expiration Date:  05/21/23
```

3.  Assign [API_KEY_VALUE] to a new environment variable called PREFECT_CLOUD_LOCAL_API_KEY, by adding the line below to ~/.bash_profile.
```sh
vim ~/.bash_profile
.
.
.
export PREFECT_CLOUD_LOCAL_API_KEY=[API_KEY_VALUE]
```

4.  Source ~/.bash_profile, and confirm that PREFECT_CLOUD_LOCAL_API_KEY has a value.
```sh
source ~/.bash_profile
echo $PREFECT_CLOUD_LOCAL_API_KEY
```

5. Create a Python virtual environment.
```sh
python3 -m venv ./venv
source venv/bin/activate
```

6. Install Python packages.
```sh
make install
```

7. Install Python packages for unit testing.
```sh
make install-test
```

8. Run unit tests.
```sh
make unit-test
```

Here's what you should see:
```sh
pytest -v --cov=flows tests/
======================================================================================= test session starts =======================================================================================
platform darwin -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0 -- /Users/jeffcharbeneau/Documents/GitHub/testing-prefect/venv/bin/python3.11
cachedir: .pytest_cache
rootdir: /Users/jeffcharbeneau/Documents/GitHub/testing-prefect
plugins: cov-4.0.0, anyio-3.6.2
collected 1 item                                                                                                                                                                                  

tests/test_example_test_flow.py::test_my_favorite_flow PASSED                                                                                                                               [100%]

======================================================================================== warnings summary =========================================================================================
tests/test_example_test_flow.py::test_my_favorite_flow
  /Users/jeffcharbeneau/Documents/GitHub/testing-prefect/venv/lib/python3.11/site-packages/prefect/server/database/migrations/versions/sqlite/2022_04_25_135207_b75d279ba985_replace_version_with_checksum.py:107: RemovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0. To prevent incompatible upgrades prior to updating applications, ensure requirements files are pinned to "sqlalchemy<2.0". Set environment variable SQLALCHEMY_WARN_20=1 to show all deprecation warnings.  Set environment variable SQLALCHEMY_SILENCE_UBER_WARNING=1 to silence this message. (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    meta_data = sa.MetaData(bind=connection)

tests/test_example_test_flow.py::test_my_favorite_flow
  /usr/local/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py:144: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__coalesce_start_time_expected_start_time_desc
    next(self.gen)

tests/test_example_test_flow.py::test_my_favorite_flow
  /usr/local/Cellar/python@3.11/3.11.2_1/Frameworks/Python.framework/Versions/3.11/lib/python3.11/contextlib.py:144: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__coalesce_start_time_expected_start_time_asc
    next(self.gen)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------- coverage: platform darwin, python 3.11.2-final-0 ----------
Name                Stmts   Miss  Cover
---------------------------------------
flows/__init__.py       0      0   100%
flows/example.py        7      2    71%
---------------------------------------
TOTAL                   7      2    71%

================================================================================= 1 passed, 3 warnings in 17.51s ==================================================================================
```

9. Log into Prefect Cloud.
```sh
make login
```

Here's what you should see:
```sh
Authenticated with Prefect Cloud! Using workspace '[YOUR EMAIL ADDRESS WITHOUT ANY PERIODS]/prefect-cloud-local'.
```

or

```sh
This profile is already authenticated with that key.
```

10. Run [flows/example.py](./flows/example.py).
```
python ./flows/example.py
```

Here's what you should see:
```
11:11:38.656 | INFO    | prefect.engine - Created flow run 'calm-horse' for flow 'my-favorite-flow'
11:11:39.511 | INFO    | Flow run 'calm-horse' - Finished in state Completed()
42
```