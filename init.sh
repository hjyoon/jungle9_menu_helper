#!/bin/sh

cd "$(dirname "$0")" || exit

rm -rf venv-jungle/ __pycache__/

python -m venv venv-jungle

. ./venv-jungle/bin/activate

pip install -r ./requirements.txt
