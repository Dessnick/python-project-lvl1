install:
	@poetry install

# test:
# 	poetry run pytest hexlet_python_package tests

lint:
	poetry run flake8

selfcheck:
	poetry check

check: selfcheck lint

build: check
	@poetry build

.PHONY: install lint selfcheck check build