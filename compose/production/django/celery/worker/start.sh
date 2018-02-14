#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A bike_rents.taskapp worker -l INFO
