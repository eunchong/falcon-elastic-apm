import imp
import io
from os import path

from setuptools import find_packages, setup

VERSION = imp.load_source('version', path.join('.', 'falcon_elastic_apm', 'version.py'))
VERSION = VERSION.__version__


def read(fname):
    return open(path.join(path.dirname(__file__), fname)).read()


setup(
    name='falcon-elastic-apm',
    version=VERSION,
    description='Falcon middleware for application performance monitoring.',
    long_description_content_type='text/markdown',
    long_description=read('README.md'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Natural Language :: English',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Application Frameworks',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='wsgi web api framework rest elastic apm performance monitoring',
    author='eunchong',
    url='https://github.com/eunchong/falcon-elastic-apm',
    license='MIT',
    packages=['falcon_elastic_apm'],
    install_requires=read('requirements.txt')
)
