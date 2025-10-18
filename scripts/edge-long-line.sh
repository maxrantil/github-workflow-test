#!/bin/bash
# ABOUTME: Script with very long lines

set -euo pipefail

main() {
    local very_long_variable_name_that_goes_on_and_on="This is a very long string that contains a lot of text and goes on for quite a while to test how the formatter and linter handle extremely long lines that exceed normal line length limits which are typically around 80 or 120 characters but this line is much much longer than that"

    echo "${very_long_variable_name_that_goes_on_and_on}"

    # Very long command line
    find /usr/local/bin /usr/bin /bin /sbin /usr/sbin /opt/bin /opt/sbin /home/user/bin /home/user/.local/bin -type f -name "*.sh" -o -name "*.bash" -o -name "*.zsh" | grep -v "test" | grep -v "tmp" | sort | uniq

    return 0
}

main "$@"
