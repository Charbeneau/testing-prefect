.PHONY: python-package help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([0-9a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

args = `arg="$(filter-out $@,$(MAKECMDGOALS))" && echo $${arg:-${1}}`

%:
    @:

CONTAINER_TAG=testing-prefect

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean-unused:
	docker system prune --all --force --volumes

clean-all:
	docker container stop $$(docker container ls --all --quiet) && docker system prune --all --force --volumes

build:
	docker build --tag ${CONTAINER_TAG} .

unit-tests:
	docker run --interactive --tty ${CONTAINER_TAG} unit-tests

shell:
	docker run --interactive --tty --volume $$(pwd)/testing-prefect:/workspace/testing-prefect \
	--env PREFECT_CLOUD_LOCAL_API_KEY=${PREFECT_CLOUD_LOCAL_API_KEY} \
		${CONTAINER_TAG} /bin/sh

black:
	docker run --rm -v $$(pwd):/data cytopia/black flows tests