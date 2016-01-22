#!/usr/bin/env python
# encoding: utf-8
"""Download programs from DR TV.

See:
https://github.com/simonbs/dldr
"""

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='dldr',
    version='1.0.1',
    description='Download programs from DR TV.',
    long_description=long_description,
    url='https://github.com/simonbs/dldr',
    author='Simon Støvring',
    author_email='mail@simonbs.dk',
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],

  keywords='dr tv dk download danmarks radio',
  packages=find_packages(exclude=['contrib', 'docs', 'tests']),

  install_requires=['docopt', 'schema'],
  
  # To provide executable scripts, use entry points in preference to the
  # "scripts" keyword. Entry points provide cross-platform support and allow
  # pip to create the appropriate form of executable for the target platform.
  entry_points={
    'console_scripts': [
      'dldr = dldr:run',
    ],
  },
)
