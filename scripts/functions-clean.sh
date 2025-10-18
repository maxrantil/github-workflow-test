#!/bin/bash
# ABOUTME: Clean script with multiple functions

set -euo pipefail

# Global variables
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
readonly SCRIPT_DIR
readonly LOG_FILE="${SCRIPT_DIR}/output.log"

# Logging function
log() {
    local level="${1}"
    shift
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] [${level}] $*" | tee -a "${LOG_FILE}"
}

# Validation function
validate_input() {
    local input="${1}"

    if [[ -z "${input}" ]]; then
        log "ERROR" "Input cannot be empty"
        return 1
    fi

    if [[ ! "${input}" =~ ^[a-zA-Z0-9_-]+$ ]]; then
        log "ERROR" "Input contains invalid characters"
        return 1
    fi

    return 0
}

# Processing function
process_data() {
    local data="${1}"

    log "INFO" "Processing data: ${data}"

    if validate_input "${data}"; then
        log "SUCCESS" "Data validated successfully"
        return 0
    else
        log "ERROR" "Data validation failed"
        return 1
    fi
}

main() {
    log "INFO" "Script started"

    if [[ $# -eq 0 ]]; then
        log "ERROR" "No arguments provided"
        exit 1
    fi

    for arg in "$@"; do
        process_data "${arg}"
    done

    log "INFO" "Script completed"
}

main "$@"
