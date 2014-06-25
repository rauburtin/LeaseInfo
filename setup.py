#!/usr/bin/env python
from setuptools import setup
import os

_dirname = os.path.abspath(os.path.dirname(__file__))
README_PATH = os.path.join(_dirname, 'README.md')

description = '''\
Parses ISC dhcpd leases file and returns dict[IP, tuple(mac, name)].'''

if os.path.exists(README_PATH):
    long_description = open(README_PATH).read()
else:
    long_description = description

setup(name='py-lease-file-parser',
    version='0.1',
    description=description,
    license='BSD',
    url='https://github.com/jm1024/LeaseInfo',
    author='jm1024',
    author_email='info@vxk.cz',
    py_modules=['LeaseInfo'],
    install_requires=[],
    keywords="isc linux dhcpd lease parse",
    include_package_data=True,
)
