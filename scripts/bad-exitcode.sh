#!/bin/bash
# ABOUTME: SC2181 - Checking $? directly instead of if/while

set -e

main() {
    local result_file="/tmp/result.txt"

    grep "pattern" "${result_file}"

    # This will cause SC2181: Check exit code directly with e.g. 'if grep pattern file'
    if [ $? -eq 0 ]; then
        echo "Pattern found"
    else
        echo "Pattern not found"
    fi
}

main "$@"
