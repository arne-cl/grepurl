#!/usr/bin/env python

import sys
import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='grepurl',
      version='my_version_number',
      description='0.1.1',
      long_description=README,
      author='Gerome Fournier',
#      author_email='',
      url='https://github.com/arne-cl/grepurl',
      py_modules=['grepurl'],
      entry_points={'console_scripts': ['grepurl=grepurl:main']},
      license='GPLv2 or later',
)


