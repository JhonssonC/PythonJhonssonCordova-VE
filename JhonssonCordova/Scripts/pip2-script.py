#!D:\Datos\JhonssonCordova\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'pip==6.0.8','console_scripts','pip2'
__requires__ = 'pip==6.0.8'
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.exit(
        load_entry_point('pip==6.0.8', 'console_scripts', 'pip2')()
    )
