import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
	name='moceansdk',
    version='0.1.18',
	description='Nexmo Client Library for Python',
	long_description='This is a Mocean SDK written in python, to use it you will need a mocean account. Signup for free at https://moceanapi.com',
	url='https://github.com/MoceanAPI/mocean-sdk-python',
	author='Micro Ocean Technologies Sdn Bhd',
	author_email='support@moceanapi.com',
	license='MIT',
	packages= setuptools.find_packages(),
	platforms=['any'],
	classifiers=[
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: 3.6',
	]
)