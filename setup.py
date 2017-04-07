from setuptools import setup

from datagovsg_api import __version__


setup(
    name='datagovsg_api',
    version=__version__,
    author='Ray Chen',
    author_email='ray@half0wl.com',
    packages=['datagovsg_api'],
    url='http://pypi.python.org/pypi/datagovsg_api/',
    license='MIT',
    description='Unofficial API wrapper for public APIs at developers.data.gov.sg',
    long_description='Visit https://github.com/half0wl/datagovsg_api for info.',
    install_requires=[
        "requests >= 2.13.0",
    ],
)
