"""Django ORM Practice Setup Code"""

import os
import sys
import django
from pathlib import Path


def django_setup():
    """Setup Django environment for ORM practice.

        1. Append the project root directory to `sys.path`.
        2. Set the Django settings module.
        3. Initialize Django.
    """
    sys.path.append(str(Path(__file__).resolve().parent.parent))
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
    django.setup()
