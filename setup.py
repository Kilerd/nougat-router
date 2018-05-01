from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.1'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='nougat_router',
    version=__version__,
    description='Router for nougat web framework supported restful api and parameters\' validation',
    long_description=long_description,
    url='https://github.com/Kilerd/nougat_router',

    author='Kilerd Chan',
    author_mail='blove694@gmail.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
    ],

    keywords='web async router restful param',

    packages=find_packages(exclude=['docs', 'demo', 'tests*']),
    include_package_data=True,
    install_requires=[
        'nougat'
    ],
    python_requires='>=3.6',
)