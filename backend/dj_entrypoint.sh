#!/bin/bash
set -e

if [[ -e venv/bin/activate ]]; then
source venv/bin/activate
fi

exec "$@"