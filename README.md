# `dinosaur-api`

Interface to dinosaur data.

# API

## `getLargestDinosaurSpeciesByNameByLengthInMetres() -> List[str]`

Returns the largest species - by name - by length (measured in metres).

**Note:**

* if data does not contain a `length` property value, 1.0m is used as a default
value
* if data does not contain a `species` property value, that data is ignored
* if there are multiple matches in terms of `length`, then all matches are
returned
* an empty list is returned if no data can be found

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

# activate local environment
source venv/bin/activate

# install dev dependencies
python -m pip install -r requirements/development.txt

# run unit tests
pytest -sv app/test/unit

# run integration tests
pytest -sv app/test/integration

# deactivate local environment
deactivate

```

# Usage

There is a `main` module to showcase the API being presented here.

Each current API can be showcased against test data:

```bash
# showcase the `getLargestDinosaurSpeciesByNameByLengthInMetres` API
CSV_DATA_FILE_LOCATION="./data/largest.csv" python main.py largest

# showcase the `getDinosaurNamesAnagramsList` API
CSV_DATA_FILE_LOCATION="./data/anagrams.csv" python main.py anagrams

```

