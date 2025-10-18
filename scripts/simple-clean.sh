#!/bin/bash
# ABOUTME: Simple clean script - should pass all checks

set -euo pipefail

main() {
    local name="${1:-World}"
    echo "Hello, ${name}!"
    return 0
}

main "$@"
