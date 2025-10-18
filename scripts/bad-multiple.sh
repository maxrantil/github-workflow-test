#!/bin/bash
# ABOUTME: Multiple ShellCheck violations in one file

set -e

main() {
    # SC2006: Backticks
    local date=`date +%Y-%m-%d`

    # SC2086: Unquoted variable
    local dir=$1
    cd $dir

    # SC2046: Word splitting
    rm $(find . -name "*.tmp")

    # SC2181: Checking $?
    ls /nonexistent
    if [ $? -ne 0 ]; then
        echo "Failed"
    fi
}

main "$@"
