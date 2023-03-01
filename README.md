# prefect-cloud-local

Here I try to get off the ground unit testing [Prefect Cloud 2](https://www.prefect.io/cloud/) with [Pytest](https://docs.pytest.org/en/7.2.x/) inside [Docker](https://www.docker.com/).

# Requirements
    - A Prefect Cloud 2 account
    - [Docker Desktop](https://www.docker.com/products/docker-desktop/)
      - I used Docker version 20.10.17, build 100c701
    - [Make](https://www.gnu.org/software/make/)
      - I used 3.81

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

3.  Assign [API_KEY_VALUE] to a new environment variable called PREFECT_CLOUD_LOCAL_API_KEY.  I added it to my ~/.bash_profile thusly.
```sh
vim ~/.bash_profile
.
.
.
export PREFECT_CLOUD_LOCAL_API_KEY=[API_KEY_VALUE]
```

4.  Confirm that PREFECT_CLOUD_LOCAL_API_KEY has a value.  You might need to `source ~/.bash_profile`.
```sh
echo $PREFECT_CLOUD_LOCAL_API_KEY
```

5. Build the testing-prefect container.
```sh
make build
```

6. Run unit tests.
```sh
make unit-tests
```

Here's what you should see.
```sh
docker run --interactive --tty testing-prefect unit-tests
======================================================================================= test session starts =======================================================================================
platform linux -- Python 3.11.2, pytest-7.2.1, pluggy-1.0.0 -- /usr/local/bin/python
cachedir: .pytest_cache
rootdir: /workspace
plugins: cov-4.0.0, anyio-3.6.2
collected 1 item                                                                                                                                                                                  

tests/test_example_test_flow.py::test_my_favorite_flow PASSED                                                                                                                               [100%]

======================================================================================== warnings summary =========================================================================================
tests/test_example_test_flow.py::test_my_favorite_flow
  /usr/local/lib/python3.11/site-packages/prefect/server/database/migrations/versions/sqlite/2022_04_25_135207_b75d279ba985_replace_version_with_checksum.py:107: RemovedIn20Warning: Deprecated API features detected! These feature(s) are not compatible with SQLAlchemy 2.0. To prevent incompatible upgrades prior to updating applications, ensure requirements files are pinned to "sqlalchemy<2.0". Set environment variable SQLALCHEMY_WARN_20=1 to show all deprecation warnings.  Set environment variable SQLALCHEMY_SILENCE_UBER_WARNING=1 to silence this message. (Background on SQLAlchemy 2.0 at: https://sqlalche.me/e/b8d9)
    meta_data = sa.MetaData(bind=connection)

tests/test_example_test_flow.py::test_my_favorite_flow
  /usr/local/lib/python3.11/contextlib.py:144: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__coalesce_start_time_expected_start_time_desc
    next(self.gen)

tests/test_example_test_flow.py::test_my_favorite_flow
  /usr/local/lib/python3.11/contextlib.py:144: SAWarning: Skipped unsupported reflection of expression-based index ix_flow_run__coalesce_start_time_expected_start_time_asc
    next(self.gen)

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html

---------- coverage: platform linux, python 3.11.2-final-0 -----------
Name                Stmts   Miss  Cover
---------------------------------------
flows/__init__.py       0      0   100%
flows/example.py        7      2    71%
---------------------------------------
TOTAL                   7      2    71%

================================================================================= 1 passed, 3 warnings in 19.91s ==================================================================================
```

7. Run the container, and open a shell.
```sh
make shell
```

Here's what you should see.
```sh
docker run --interactive --tty --volume $(pwd)/testing-prefect:/workspace/testing-prefect \
	--env PREFECT_CLOUD_LOCAL_API_KEY=[API_KEY_VALUE] \
		testing-prefect /bin/sh
# 
```

8. **From inside the running container**, log into Prefect 2 Cloud.
```sh
# prefect cloud login -k $PREFECT_CLOUD_LOCAL_API_KEY
```

Here's what you should see.
```sh
Authenticated with Prefect Cloud! Using workspace '[YOUR EMAIL ADDRESS WITHOUT ANY PERIODS]/prefect-cloud-local'.
```

9. **From inside the container**, run a flow.
```sh
# python ./flows/dictionary.py
```

Here's what you should see.
```sh
20:51:04.869 | INFO    | prefect.engine - Created flow run 'orange-avocet' for flow 'dictionaries-flow'
20:51:05.590 | INFO    | Flow run 'orange-avocet' - Created task run 'encode_task-0' for task 'encode_task'
20:51:05.593 | INFO    | Flow run 'orange-avocet' - Executing 'encode_task-0' immediately...
20:51:05.861 | INFO    | Task run 'encode_task-0' - Creating masked_ip from ip.
20:51:05.862 | INFO    | Task run 'encode_task-0' - Creating masked_device_id from device_id.
20:51:06.062 | INFO    | Task run 'encode_task-0' - Finished in state Completed()
20:51:06.197 | INFO    | Flow run 'orange-avocet' - Created task run 'str_to_int_task-0' for task 'str_to_int_task'
20:51:06.198 | INFO    | Flow run 'orange-avocet' - Executing 'str_to_int_task-0' immediately...
20:51:06.469 | INFO    | Task run 'str_to_int_task-0' - Making app_version an int.
20:51:06.563 | INFO    | Task run 'str_to_int_task-0' - Finished in state Completed()
20:51:06.740 | INFO    | Flow run 'orange-avocet' - Created task run 'create_date_task-0' for task 'create_date_task'
20:51:06.741 | INFO    | Flow run 'orange-avocet' - Executing 'create_date_task-0' immediately...
20:51:07.074 | INFO    | Task run 'create_date_task-0' - Creating create_date an int.
20:51:07.170 | INFO    | Task run 'create_date_task-0' - Finished in state Completed()
20:51:07.281 | INFO    | Flow run 'orange-avocet' - Finished in state Completed()
{'app_version': 2,
 'create_date': datetime.datetime(2023, 3, 1, 20, 51, 7, 75601),
 'device_type': 'android',
 'locale': 'RU',
 'masked_device_id': 'NTkzLTQ3LTU5Mjg=',
 'masked_ip': 'MTk5LjE3Mi4xMTEuMTM1',
 'user_id': '424cdd21-063a-43a7-b91b-7ca1a833afae'}
```

10. Exit the container.
```sh
# exit
```

11. In Prefect Cloud 2, in the "prefect-cloud-local" workspace, look for the "dictionaries-flow" run.  Your run probably isn't called 'orange-avocet'.  