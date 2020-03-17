#!/usr/bin/env bash

set -e

python3 -m venv .env
. .env/bin/activate

. ./scripts/env_prepare.sh

export ENV="local"

python mbi_api/manage.py run
