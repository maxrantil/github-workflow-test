#!/bin/bash
# ABOUTME: Complex clean script - functions, loops, conditionals

set -euo pipefail

# Process a list of files
process_files() {
    local dir="${1:-.}"
    local count=0

    if [[ ! -d "${dir}" ]]; then
        echo "Error: Directory not found: ${dir}" >&2
        return 1
    fi

    for file in "${dir}"/*.txt; do
        if [[ -f "${file}" ]]; then
            echo "Processing: ${file}"
            count=$((count + 1))
        fi
    done

    echo "Processed ${count} files"
    return 0
}

# Check environment
check_environment() {
    case "${SHELL}" in
        */bash)
            echo "Running in bash"
            ;;
        */zsh)
            echo "Running in zsh"
            ;;
        *)
            echo "Unknown shell: ${SHELL}"
            ;;
    esac
}

main() {
    check_environment
    process_files "${1:-.}"
}

main "$@"
