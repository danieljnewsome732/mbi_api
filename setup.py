"""Setup for MBI API."""
from setuptools import setup, find_packages
from mbi_api import __version__

with open('requirements.txt') as f:
    required_packages = f.read().splitlines()

setup(
    name='mbi-api',
    description='API to handle all creating MBIs.',
    version=__version__,
    author='Daniel Newsome',
    author_email='support@100plus.com',
    url='http://100plus.mbiapi.com',
    packages=find_packages(exclude=['tests*']),
    entry_points={
        'console_scripts': []
    },
    include_package_data=True,
    install_requires=required_packages,
    classifiers=[
        "Private :: Do Not Upload"
    ]
)
