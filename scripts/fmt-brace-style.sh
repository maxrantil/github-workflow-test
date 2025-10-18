#!/bin/bash
# ABOUTME: Wrong function brace placement

set -euo pipefail

# Function with brace on wrong line
function greet()
{
    local name="${1:-World}"
    echo "Hello, ${name}!"
}

# Another function with different style
process_data()
{
    local data="${1}"
    echo "Processing: ${data}"
}

main() {
    greet "Doctor Hubert"
    process_data "test-data"
}

main "$@"
