#!/bin/bash
# ABOUTME: Script with Unicode characters and special symbols

set -euo pipefail

main() {
    local greeting="Héllo Wörld! 你好世界 🌍"
    local symbols="!@#$%^&*()_+-=[]{}|;:',.<>?/~\`"

    echo "${greeting}"
    echo "${symbols}"

    # Function with Unicode name (valid in bash)
    grëët_üser() {
        echo "Grëëtings!"
    }

    grëët_üser
}

main "$@"
