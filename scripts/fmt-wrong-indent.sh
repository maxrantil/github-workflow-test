#!/bin/bash
# ABOUTME: Wrong indentation (2 spaces instead of 4)

set -euo pipefail

main() {
  local name="${1:-World}"
  if [[ -n "${name}" ]]; then
    echo "Hello, ${name}!"
  else
    echo "Hello, World!"
  fi
  return 0
}

main "$@"
