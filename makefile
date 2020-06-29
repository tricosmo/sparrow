VIRTUAL_ENV_PATH := .venv
VIRTUAL := . $(VIRTUAL_ENV_PATH)/bin/activate &&
PYTHON_EXE := /usr/local/bin/python3
.PHONY : venv setup run clean test

setup: $(VIRTUAL_ENV_PATH)/bin/activate
$(VIRTUAL_ENV_PATH)/bin/activate: requirements.txt
	test -d $(VIRTUAL_ENV_PATH) || $(PYTHON_EXE) -m virtualenv $(VIRTUAL_ENV_PATH)
	$(VIRTUAL) pip install -U pip
	$(VIRTUAL) pip install --no-cache-dir -r requirements.txt
	$(VIRTUAL) pre-commit install

run:
	$(VIRTUAL) FLASK_APP=web/hello.py FLASK_ENV=development flask run --host=0.0.0.0

validate-circleci:
	circleci config process .circleci/config.yml

run-circleci-local:
	circleci local execute

lint:
	hadolint Dockerfile
	pylint --disable=R,C,W1203,W1202 web/**.py

clean:
	rm -rf $(VIRTUAL_ENV_PATH)
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	find . -name "__pycache__" -type d -exec rm -fr "{}" +;
test:
	$(VIRTUAL) PYTHONPATH=. pytest tests
