#!/usr/bin/env bash

set -e

test_file=$1

python3 -m venv .env
. .env/bin/activate

. ./scripts/env_prepare.sh

if [[ -z "${test_file}" ]]; then
    pytest --cov mbi_api
else
    if [[ ! -e "${test_file}" ]]; then
    echo ${test_file}: no such file
    exit 1
    fi
    pytest -s "${test_file}"
fi
