#!/bin/bash
set -euo pipefail

case ${1:-} in
  unit-tests)
  pytest -v --cov=flows tests/
    ;;
  *)
    exec "$@"
    ;;
esac