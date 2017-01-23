import os
import sys
from setuptools import setup, find_packages
from setuptools.command.install import install


version = '0.1.0'

description = 'An async command line utility for generating a sitemap within a text file'
current_dir = os.path.dirname(__file__)
try:
    long_description = open(os.path.join(current_dir, 'README.md')).read()
except:
    long_description = description


setup(
    name='sitemap3',
    version=version,
    packages=find_packages(),
    url='https://github.com/konstantinfarrell/sitemap3',
    license='MIT',
    description=description,
    long_description=long_description,
    author='Konstantin Farrell',
    author_email='konstantinfarrell@gmail.com',
    data_files=[
        ("", ['README.md', 'LICENSE'])
    ],
    install_requires=[
        'beautifulsoup4',
        'aiohttp'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Utilities',
        'Topic :: Internet'
    ],
    entry_points={
        'console_scripts': [
            'sitemap = sitemap:main',
        ]
    }
)
