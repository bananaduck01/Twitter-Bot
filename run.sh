#!/usr/bin/env bash
# Enable error reporting
set -e

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Run Python script using system Python
python3 "$DIR/main.py"
