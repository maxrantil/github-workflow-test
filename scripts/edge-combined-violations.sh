#!/bin/bash
# ABOUTME: Multiple violations - both ShellCheck and shfmt

set -e

main() {
  # Wrong indentation (2 spaces)
  local date=`date`  # Backticks
  local dir=$1  # Unquoted variable
  cd $dir  # No error handling

  # Wrong case indentation
  case "${2}" in
  foo)
  echo "foo"  # Wrong indent
  ;;
  bar)
  echo "bar"
  ;;
  esac

  # No space in redirect
  echo "output">"file.txt"
}

main "$@"
