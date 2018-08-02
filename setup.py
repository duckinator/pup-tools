#!/usr/bin/env python3

from setuptools import setup

setup(
    entry_points={
        'console_scripts': [
            'pup.xpath=pup.xpath:_main',
            'pup.http=pup.http:_main',
            'pup.py=pup.py:main',
        ],
        'distutils.commands': [
            'release = distutils_twine:release',
        ],
    },
)
