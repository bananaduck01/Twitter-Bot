#!/bin/bash
# Enable error reporting
set -e

# Get the directory of this script
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Activate the virtual environment
source "$DIR/env/bin/activate"

# Run the python script
python3 "$DIR/main.py"
