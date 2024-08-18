#!/bin/bash

# Check if python3 is installed
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found. Please install Python 3."
    exit
fi

# Activate virtual environment
source venv/bin/activate

# Install required packages
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
else
    echo "requirements.txt not found."
fi
