#!/bin/bash
# Install dependencies with --break-system-packages for Vercel uv Python environment
python3 -m pip install -r requirements.txt --break-system-packages

# Run database migrations
python3 hotel/manage.py migrate --no-input

# Create default admin user
python3 hotel/manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.filter(username='admin').exists() or User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')"

# Run collectstatic for static files
python3 hotel/manage.py collectstatic --no-input --clear
