#!/bin/bash
# Install dependencies with --break-system-packages for Vercel uv Python environment
python3 -m pip install -r requirements.txt --break-system-packages

# Run collectstatic for static files
python3 hotel/manage.py collectstatic --no-input --clear
