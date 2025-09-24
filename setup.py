import io
import os

import setuptools

with io.open(os.path.join(os.path.dirname(__file__), "README.md"), encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name='moceansdk',
    version='1.2.0',
    description='Mocean Client Library for Python',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/MoceanAPI/mocean-sdk-python',
    author='Micro Ocean Technologies Sdn Bhd',
    author_email='support@moceanapi.com',
    license='MIT',
    install_requires=["requests>=2.20,<2.33", "urllib3>=1.26,<3",
                      "xmltodict>=0.12,<1.1", "dotmap~=1.3.0", "future>=0.18.2,<1.1.0"],
    extras_require={
        'test': ['requests-mock>=1.6,<1.13'],
    },
    packages=setuptools.find_packages(exclude=['tests', 'tests.*']),
    platforms=['any'],
    classifiers=[
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ]
)
