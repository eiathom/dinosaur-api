# `dinosaur-api`

Interface to dinosaur data.

# API

## `getLargestDinosaurSpeciesByNameByLengthInMetres() -> str`

Returns the largest species - by name - by length (measured in metres).

**Note:**

* if data does not contain a `length` property value, 1.0m is used as a default
value
* if data does not contain a `species` property value, that data is ignored

## `getDinosaurNamesAnagramsList() -> List[List[str]]`

Returns a List of Lists, where each sub-List contains string items that are
anagrams.

# Developing

This repository is developed with Python version `3.7`.

## Required local configuration

```
# install pyenv
curl https://pyenv.run | bash

# once installed and the run script is added to ~/.bashrc do
pyenv install 3.7.2

# set the local Python interpreter
pyenv local $(head -1 .python-version)

# create a local environment
python -m venv venv

# install dev dependencies
python -m pip install -r requirements/development.txt

# run unit tests
pytest -sv app/test/unit

# run integration tests
pytest -sv app/test/integration

```

# Usage


