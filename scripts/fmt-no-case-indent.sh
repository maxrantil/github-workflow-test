#!/bin/bash
# ABOUTME: Case statement without proper indentation

set -euo pipefail

main() {
    local option="${1:-help}"

    case "${option}" in
    start)
    echo "Starting service..."
    ;;
    stop)
    echo "Stopping service..."
    ;;
    restart)
    echo "Restarting service..."
    ;;
    *)
    echo "Unknown option: ${option}"
    ;;
    esac
}

main "$@"
