#!/bin/bash
# ABOUTME: Redirects without spaces

set -euo pipefail

main() {
    local output_file="/tmp/output.txt"
    local input_file="/tmp/input.txt"

    # Should be: > file not >file (no space before redirect)
    echo "Writing to file">>"${output_file}"
    cat "${input_file}">"${output_file}"
    grep "pattern" "${input_file}">"${output_file}"

    return 0
}

main "$@"
