"""
==============
Hi Hy Lang
==============
A simple package in Hy language that says Hi.

Its main purpose is to show how to create and publish a Python package that
contains Hy code.

See GitHub repository for the Hy package publication guide.
"""
from setuptools import setup,find_packages

setup(
	name='hihylang',
	version='1.0',
	url='https://github.com/MonsieurV/hy-lang-create-package',
	author='Yoan Tournade',
	author_email='yoan@ytotech.com',
	description='A Hy package that says Hi.',
	long_description=__doc__,
	packages=find_packages(exclude=['tests*']),
	package_data={
		'hihylang': ['*.hy']
	},
	include_package_data=True,
	zip_safe=True,
	platforms='any',
	install_requires=[
		'hy'
	]
)
