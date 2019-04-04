'''
Created on , 2019
@author: Jonas Wallin
'''
try:
	from setuptools import setup, Extension
except ImportError:
	try:
		from setuptools.core import setup, Extension
	except ImportError:
		from distutils.core import setup, Extension
		
metadata = dict(name='linkingAWS',
	packages         = ['linkingAWS'],
	package_dir      = {'linkingAWS': 'linkingAWS'},
	version          = '0.1',
	description      = 'wrapper for various ssh into EC2',
	author           = 'Jonas Wallin',
	maintainer_email = 'jonas.wallin81@gmail.com',
	url              = 'https://github.com/JonasWallin/linkingAWS',
	author_email     = 'jonas.wallin81@gmail.com',
	install_requires = ['boto3'])
setup(**metadata)