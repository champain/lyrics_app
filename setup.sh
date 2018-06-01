#!/usr/bin/env bash

if ! which python3 > /dev/null; then
  echo 'python3 binary not found.'
  echo "Please ensure it's installed and in your path"
  exit 2
else
  echo 'Setting up virtualenv'
fi

python3 -m virtualenv .venv

pip install -r requirements.txt

python -m textblob.download_corpora
