create-venv:
	rm -rf venv
	python -m venv venv

install-dev:
	pip install -r requirements/development.txt

unit:
	pytest -sv app/test/unit

integration:
	pytest -sv app/test/integration

test: unit integration

clean:
	find . -type f -name "*.pyc" -delete
	rm -fr .cache .mypy_cache .pytest_cache

lint:
	black --target-version py36 --diff --color app/

.PHONY: create-env install unit integration test clean lint
