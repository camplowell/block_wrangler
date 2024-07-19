#!/bin/bash

if [ ! -d "./venv_dev" ]; then
	python3 -m venv ./venv_dev
	pip install -e '.[dev]'
fi
source ./venv_dev/bin/activate
python scripts/importer.py "$@"