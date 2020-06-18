#!/usr/bin/env bash

python3 -m venv env
. env/bin/activate
pip install --upgrade pip
pip install pytest pytest-cov
