from setuptools import setup, find_packages
import aiourlshortener

setup(
    name='aiourlshortener',
    version=aiourlshortener.__version__,
    license=aiourlshortener.__license__,
    author=aiourlshortener.__author__,
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
