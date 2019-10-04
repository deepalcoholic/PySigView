"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

import shutil
import sys
import os

import scipy

from sigpy.config.base import MAC_APP_NAME

DATA_FILES = []
OPTIONS = {}

# To deal with a bug in py2app 0.9
sys.setrecursionlimit(1500)

# =============================================================================
# App creation
# =============================================================================
APP_MAIN_SCRIPT = MAC_APP_NAME[:-4] + '.py'

shutil.copyfile('scripts/sigpy', APP_MAIN_SCRIPT)

APP = [APP_MAIN_SCRIPT]
DEPS = ['scipy', 'setuptools']
EXCLUDES = DEPS + ['mercurial']
PACKAGES = ['sigpy', 'PyQt5', 'numpy', 'vispy',  # Necessary
            'pymef', 'OpenGL',  # Wanted
            # Required for plugins
            'pandas', 'bcolz', 'sqlalchemy', 'pymysql', 'qtconsole']

# Note: numpy and OpenGL might not be necessary

# INCLUDES = get_stdlib_modules()
# EDIT_EXT = [ext[1:] for ext in _get_extensions(EDIT_FILETYPES)]
destination = '/Users/jan/Desktop/'
BUILD_FOLDER = destination+'sigpy_build'
DIST_FOLDER = destination+'sigpy_dist'


OPTIONS = {
    'compressed': False,
    'optimize': 0,
    'packages': PACKAGES,
    'bdist_base': BUILD_FOLDER,
    'dist_dir': DIST_FOLDER,
    # 'includes': INCLUDES,
    'excludes': EXCLUDES,
    'iconfile': 'icons/sigpy.icns',
}

setup(
    app=APP,
    options={'py2app': OPTIONS}
)

# Remove script for app
os.remove(APP_MAIN_SCRIPT)

# =============================================================================
# Post setup tasks
# =============================================================================

print('Copying scipy...')

# Important note! - due to a bug in macholib and scipy. scipy has to be copied
# manually from the site-packages of the given interpreter

# Python version
pv = str(sys.version_info[0])+'.'+str(sys.version_info[1])

scipy_src = scipy.__path__[0]
scipy_dest = (DIST_FOLDER+'/'+MAC_APP_NAME+'/Contents/Resources/lib/'
              'python'+pv+'/scipy')
try:
    shutil.rmtree(scipy_dest)
except Exception as e:
    pass

shutil.copytree(scipy_src, scipy_dest)