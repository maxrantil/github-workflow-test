#!/bin/bash
# ABOUTME: Clean script demonstrating array handling

set -euo pipefail

# Array operations
demonstrate_arrays() {
    local -a fruits=("apple" "banana" "cherry")
    local -a colors=()

    echo "Fruits list:"
    for fruit in "${fruits[@]}"; do
        echo "  - ${fruit}"
    done

    # Add elements
    colors+=("red")
    colors+=("yellow")
    colors+=("purple")

    echo "Colors list:"
    printf '  - %s\n' "${colors[@]}"

    # Array length
    echo "Total fruits: ${#fruits[@]}"
    echo "Total colors: ${#colors[@]}"
}

# Associative array
demonstrate_map() {
    local -A config=(
        [host]="localhost"
        [port]="8080"
        [debug]="true"
    )

    echo "Configuration:"
    for key in "${!config[@]}"; do
        echo "  ${key} = ${config[${key}]}"
    done
}

main() {
    echo "=== Array Demonstration ==="
    demonstrate_arrays
    echo
    echo "=== Map Demonstration ==="
    demonstrate_map
}

main "$@"
