#!/usr/bin/env python3
import os, sys
from setuptools import setup, find_packages

# https://github.com/pypa/pip/issues/4187#issuecomment-452862842
def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')

    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]

    return requirements


setup(
    name="tap-chatitive",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_chatitive"],
    install_requires=read_requirements(),
    entry_points="""
    [console_scripts]
    tap-chatitive=tap_chatitive:main
    """,
    packages=["tap_chatitive"],
    include_package_data=True,
)
