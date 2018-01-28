import codecs
import os
import re
from setuptools import setup, find_packages

_PACKAGE_FILE = os.path.join(os.path.dirname(__file__),
                             'aiourlshortener',
                             '__init__.py')
with codecs.open(_PACKAGE_FILE, 'r', 'utf-8') as package_reader:
    _RAW_PACKAGE_METADATA = package_reader.read()

PACKAGE_METADATA = dict(re.findall("(__[a-z]+__) = '([^']+)'",
                                    _RAW_PACKAGE_METADATA))
setup(
    name='aiourlshortener',
    version=PACKAGE_METADATA['__version__'],
    license=PACKAGE_METADATA['__license__'],
    author=PACKAGE_METADATA['__author__'],
    author_email='b.like.no.other@gmail.com',
    url='https://github.com/blikenoother/aiourlshortener',
    description='asynchronous python3 lib to short long url',
    long_description=open('README.md').read(),
    packages=find_packages(include=('*')),
    keywords='asynchronous url shortener',
    install_requires=['aiohttp'],
    classifiers=['Development Status :: 5 - Production/Stable', 'Intended Audience :: Developers',
                 'Operating System :: OS Independent', 'Programming Language :: Python :: 3',
                 'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
                 'Topic :: Software Development :: Libraries :: Python Modules']
)
