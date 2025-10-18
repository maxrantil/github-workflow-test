#!/bin/bash
# ABOUTME: SC2086 - Unquoted variable expansion

set -e

main() {
    local files="file1.txt file2.txt file3.txt"

    # This will cause SC2086: Double quote to prevent globbing and word splitting
    rm $files

    echo "Deleted files: $files"
}

main "$@"
