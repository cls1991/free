#!/usr/bin/env python
# coding: utf8

import os
from codecs import open

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))

packages = ['x-free']

requires = [
    'click>=6.7',
    'prettytable>=0.7.2',
    'sh>=1.12.14'
]

about = {}
with open(os.path.join(here, 'x-free', '__version__.py'), 'r') as f:
    exec (f.read(), about)

setup(
    name=about['__title__'],
    version=about['__version__'],
    keywords=['memory', 'macos', 'linux', 'x-free'],
    description=about['__description__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    install_requires=requires,
    license=about['__license__'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6'
    ]
)
