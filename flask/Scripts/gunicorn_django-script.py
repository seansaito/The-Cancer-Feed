#!C:\Users\SeanSaito\Dev\cancer-feed\flask\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'gunicorn==19.2.1','console_scripts','gunicorn_django'
__requires__ = 'gunicorn==19.2.1'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('gunicorn==19.2.1', 'console_scripts', 'gunicorn_django')()
    )
