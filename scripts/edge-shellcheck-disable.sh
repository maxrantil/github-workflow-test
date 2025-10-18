#!/bin/bash
# ABOUTME: Attempt to bypass ShellCheck with disable comments

set -e

main() {
    # shellcheck disable=SC2086
    local files="file1.txt file2.txt"
    rm $files

    # shellcheck disable=SC2006
    local date=`date +%Y-%m-%d`

    echo "Date: $date"
}

main "$@"
