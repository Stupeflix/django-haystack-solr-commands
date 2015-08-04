import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "django-haystack-solr-commands",
    version = "0.1",
    author = "Elias Showk",
    author_email = "elias@showk.me",
    description = ("django management command 'solr' all-in-one for Solr 5"),
    license = "BSD",
    keywords = "solr haystack django management",
    url = "https://github.com/elishowk/django-haystack-solr-commands",
    packages=['haystack_solr_commands'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
    ],
    dependency_links=[
        "git+https://github.com/Stupeflix/django-haystack.git@master#egg=django-haystack"
    ],
    install_requires=[
        "Django>=1.4"
    ]
)
