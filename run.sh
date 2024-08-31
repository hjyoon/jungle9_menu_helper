#!/bin/sh

cd "$(dirname "$0")" || exit

if [ -d "venv-jungle" ]; then
    . ./venv-jungle/bin/activate
    python main.py "$1"
fi