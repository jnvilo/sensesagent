import os

from setuptools import setup, find_packages, Command
from __future__ import division, absolute_import, print_function, unicode_literals
import os
import sys

PACKAGE = os.path.basename(os.path.dirname(os.path.abspath(__file__))).replace('-', '_')

VERSION_STRING="0.0.1"
PACKAGE_ROOT = os.path.dirname(os.path.abspath(__file__))

URL = "https://github.com/jnvilo/sensesagent"
DOWNLOAD_URL="{}/archive/{}.tar.gz".format(URL, VERSION_STRING)

def get_authors():
    try:
        f = file(os.path.join(PACKAGE_ROOT, "AUTHORS"), "r")
        authors = [l.strip(" *\r\n") for l in f if l.strip().startswith("*")]
        f.close()
    except Exception:
        evalue = sys.exc_info()[1]
        authors = "[Error: %s]" % evalue
    return authors


def get_requirements():
    reqs = []
    try:
        f = file("requirements.txt", "r")
        l = f.readlines()
        for e in l:
            reqs.append(e.strip("\n"))
    except Exception:
        print("Failed to install requirements") 

    return reqs

setup(
    name=PACKAGE,
    packages=[PACKAGE],
    test_suite='tests',
    version=VERSION_STRING,
    description='A system metric gathering and processing tool and IOT metrics simulator.',
    author=get_authors(),
    author_email="jnvilo@gmail.com",
    maintainer="Jason Viloria",
    url=URL,
    download_url = DOWNLOAD_URL, 
    packages=find_packages(),
    install_requires=get_requirements(), 
    include_package_data=True, # include package data under svn source control
    
    ## Sample entry point
    
    #entry_points = {
    #    'console_scripts': ['my_command=packageskel.packageskel:make_template']
    #},
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
