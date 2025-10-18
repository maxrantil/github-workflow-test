#!/bin/bash
# ABOUTME: Mixed tabs and spaces

set -euo pipefail

main() {
	local name="${1:-World}"	# This line uses tabs
    echo "Hello, ${name}!"    # This line uses spaces
	return 0	# This line uses tabs
}

main "$@"
