import io
import os

import setuptools

with io.open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='moceansdk',
    version='1.0.2',
    description='Mocean Client Library for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MoceanAPI/mocean-sdk-python',
    author='Micro Ocean Technologies Sdn Bhd',
    author_email='support@moceanapi.com',
    license='MIT',
    install_requires=["requests>=2.20,<2.23", "xmltodict~=0.12.0", "dotmap~=1.3.0"],
    extras_require={
        'test': ['requests-mock~=1.6.0'],
    },
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
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
