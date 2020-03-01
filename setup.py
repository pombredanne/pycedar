#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from Cython.Distutils import build_ext
from setuptools import find_packages
from setuptools import setup
from setuptools import Extension

MAIN_PACKAGE = 'pycedar'

ext_modules=[
    Extension(
        'pycedar',
        ['pycedar/pycedar.pyx', 'pycedar/pycedar.pxd'],
        include_dirs = ['./cedar/src'],
        language='c++',
    ),
]

base_path = os.path.dirname(__file__)
version_path = os.path.join(base_path, MAIN_PACKAGE, 'VERSION')
version = open(version_path).read().strip()
description_path = os.path.join(base_path, 'README.md')
long_description = open(description_path).read()

setup(
    name = 'pycedar',
    version = version,
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules,
    packages = find_packages(),
    data_files = [
        ('cedar', ['cedar/src/cedarpp.h']),
        ('pycedar', ['pycedar/VERSION']),
    ],
    description = 'Python binding of cedar (implementation of efficiently-updatable double-array trie) using Cython',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/akivajp/pycedar',
    author = 'Akiva Miura',
    author_email = 'akiva.miura@gmail.com',
    license = 'GPLv2, GPLv2.1 and BSD',
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Utilities",
    ],
)
