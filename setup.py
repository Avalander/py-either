from setuptools import setup, find_packages


setup(
	name='PyEither',
	version='0.1.0',
	description='Implementation of the Either monad.',
	url='https://github.com/Avalander/py-either',
	author='Avalander',
	classifiers=[
		'Development Status :: 3 - Alpha',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4'
	],
	keywords='either functional',
	packages=find_packages(exclude='test'),
	install_requires=[]
)
