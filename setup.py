#!/usr/bin/env python3

import sys
import os
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.rst')).read()

setup(name='grepurl',
      version='0.2.0',
      description='extract URLs from websites or local HTML files',
      long_description=README,
      author='Arne Neumann',
      maintainer_email='grepurl.programming@arne.cl',
      url='https://github.com/arne-cl/grepurl',
      install_requires=['beautifulsoup4', 'requests'],
      py_modules=['grepurl'],
      entry_points={'console_scripts': ['grepurl=grepurl:main']},
      license='GPLv2 or later',
)


