#!/bin/bash
# Shell Script to automate environment setup:

echo "Setting up virtual environment and installing dependencies..."
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
