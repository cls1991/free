#!/usr/bin/env python
# coding: utf8

from setuptools import setup

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='macos-free',
    version='1.1.0',
    keywords=['memory', 'free'],
    description='Memory usage for macOS, an alternative to free command.',
    long_description=readme,
    author='cls1991',
    author_email='tzk19910406@hotmail.com',
    url='https://github.com/cls1991/free',
    py_modules=['free'],
    install_requires=[
        'click>=6.7',
        'prettytable>=0.7.2',
        'sh>=1.12.14',
        'pytest>=3.3.1'
    ],
    license='Apache License 2.0',
    zip_safe=False,
    platforms='any',
    entry_points={
        'console_scripts': ['free = free:cli']
    },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Operating System :: MacOS'
    ]
)
