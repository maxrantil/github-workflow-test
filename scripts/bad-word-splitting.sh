#!/bin/bash
# ABOUTME: SC2046 - Word splitting in command substitution

set -e

main() {
    # This will cause SC2046: Quote this to prevent word splitting
    echo "Listing files:"
    ls -l $(find . -name "*.txt")

    # Also problematic
    for file in $(ls *.sh); do
        echo "File: $file"
    done
}

main "$@"
