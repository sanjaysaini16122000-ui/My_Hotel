"""
WSGI config for hotel project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

# Add project directory to sys.path for Vercel environment
BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hotel.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
app = application

# Ensure database tables & superuser exist in /tmp on Vercel lambda instance startup
if 'VERCEL' in os.environ or os.environ.get('VERCEL_ENV') is not None:
    try:
        from django.core.management import call_command
        call_command('migrate', interactive=False)
        from django.contrib.auth import get_user_model
        User = get_user_model()
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin12345')
    except Exception as e:
        print("Vercel database initialization error:", e)
