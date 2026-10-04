#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Run collectstatic for static files
python hotel/manage.py collectstatic --no-input --clear
