"""
WSGI config for portfolio project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/

"""
import os
import sys

sys.path.append(r"C:\Users\Malena del Rosario\Documents\Ateneo\Github Portfolio\Django\portfolio")

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
