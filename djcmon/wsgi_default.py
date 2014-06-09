import os, sys

# python
sys.path.append('/usr/lib/python2.7/local/dist-packages/')
sys.path.append('/usr/lib/python2.7/dist-packages/')
sys.path.append('/usr/lib/python2.7/')
sys.path.append('/data2/django_current/')
sys.path.append('/data2/django_third/')
sys.path.append('/data2/django_projects/')
# Django
os.environ['DJANGO_SETTINGS_MODULE'] = 'djcmon.settings'
os.environ['PYTHON_EGG_CACHE'] = '/var/cache/python/.python-eggs'
os.environ['TZ'] = 'America/Chicago'
# wsgi
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

