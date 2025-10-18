#!/bin/bash
# ABOUTME: SC2164 - cd without error handling

set -e

main() {
    local target_dir="${1:-/tmp}"

    # This will cause SC2164: Use 'cd ... || exit' in case cd fails
    cd $target_dir

    echo "Current directory: $(pwd)"
    ls -la
}

main "$@"
