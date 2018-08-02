from distutils.core import setup

setup(
	name='drugs',
	version='0.1dev',
	packages=['drug'],
	author='d.wolf',
	license='MIT',
	author_email='bruceleroy409@gmail.com',
	url='http://docs.python-requests.org/en/master/',
	install_requires=[
	'bs4',
	'requests',
	],
	classifiers=[
	'Development Status :: 1 - Beta',
	'license :: OSI Approved :: MIT license',
	'Operating System :: MacOS :: MacOS X',
	'Programming Language :: Python'],
	long_descritpion=open('README.txt').read()
	)