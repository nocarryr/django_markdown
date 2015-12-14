import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tests.settings')

import django

if django.VERSION >= (1, 7):
    django.setup()
    cmd, kwargs = 'migrate', {}
else:
    cmd, kwargs = 'syncdb', dict(interactive=False)

from django.core.management import call_command

call_command(cmd, **kwargs)

from django_markdown.tests import * # noqa
