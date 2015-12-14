import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

import django

if django.VERSION >= (1, 7):
    django.setup()

from django.core.management import call_command

call_command('test')
