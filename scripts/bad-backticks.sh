#!/bin/bash
# ABOUTME: SC2006 - Deprecated backtick command substitution

set -e

main() {
    # This will cause SC2006: Use $(...) notation instead of legacy backticked `...`
    local date=`date +%Y-%m-%d`
    local user=`whoami`

    echo "Current date: $date"
    echo "Current user: $user"
}

main "$@"
