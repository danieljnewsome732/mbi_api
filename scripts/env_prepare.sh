#!/usr/bin/env bash

pip install -U pip
pip install -U -r requirements.txt
pip install -e .
export ENV="local"