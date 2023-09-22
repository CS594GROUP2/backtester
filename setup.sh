#!/bin/bash

# Create a new virtual environment
python3 -m venv env

# Activate the virtual environment
source env/bin/activate

# Install the required Python packages
pip install -r requirements.txt

# Deactivate the virtual environment
# deactivate

echo "Python environment created successfully: my_env"