#!/usr/bin/env python3
from setuptools import setup

setup(
    name="tap-chatitive",
    version="0.1.1",
    description="Singer.io tap for extracting data",
    author="Simon Data",
    url="http://simondata.com",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    py_modules=["tap_chatitive"],
    install_requires=[
        "singer-python==5.2.0",
        'requests==2.18.4',
        "pendulum==1.2.0",
        "tap-kit @ git+https://github.com/Radico/tap-kit.git@master"
    ],
    entry_points="""
    [console_scripts]
    tap-chatitive=tap_chatitive:main
    """,
    packages=["tap_chatitive"],
    include_package_data=True,
