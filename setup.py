from setuptools import setup

from datagovsg_api import __name__, __version__, __author__, __author_email__,\
    __url__, __license__, __description__, __long_description__


setup(
    name=__name__,
    version=__version__,
    author=__author__,
    author_email=__author_email__,
    packages=['datagovsg_api'],
    url=__url__,
    license=__license__,
    description=__description__,
    long_description=__long_description__,
    install_requires=[
        "requests >= 2.13.0",
    ],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
    ],
    keywords='data.gov.sg sgdata singapore',
)
