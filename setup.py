# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in bluetheme/__init__.py
from bluetheme import __version__ as version

setup(
	name='bluetheme',
	version=version,
	description='Blue Theam for ERPNext',
	author='ErPneXt',
	author_email='ErPneXt@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
