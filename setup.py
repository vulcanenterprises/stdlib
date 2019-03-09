from setuptools import setup, find_packages
from os import path

from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='sre_libs',
    version='0.0.1',
    description='SRE Module and Classes Project',
    long_description=long_description,
    long_description_conent_type='text/x-rst',
    url='https://git.corp.adobe.com/analytics-techops/sre_libs',
    author='Analytics SRE',
    author_email='@adobe.com',
    classifiers=[],  # i shouldn't need this since it's just local but we'll see
    keywords="",  # once again shouldn't need this but i'll leave it for now
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    python_requires='>=3.5',
    install_requires=['requests', 'six', 'urllib3'],
    license='GNU GPLv3'
)
