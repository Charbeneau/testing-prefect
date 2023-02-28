ifeq (, $(shell which python))
	$(error "python was not found in $(PATH). For installation instructions go to https://www.python.org/downloads/.")
endif

.PHONY: dependencies
install:
	python -m ensurepip --upgrade && pip install -r requirements.txt

install-test:
	python -m ensurepip --upgrade && pip install -r requirements-test.txt

login:
	prefect cloud login -k ${PREFECT_CLOUD_LOCAL_API_KEY}

unit-test:
	pytest -v --cov=flows tests/

run:
	python ./flows/example.py

uninstall-all:
	pip freeze | xargs pip uninstall -y

lint:
	python -m black flows tests
