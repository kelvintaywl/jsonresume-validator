# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def read_file(filename):
    with open(filename, 'r') as infile:
        return infile.read()

requires = [
    "colander==1.2"
]

extras_require = {
    "test": [
        "nose",
        "coverage",
        "flake8",
    ]
}

setup(name='jsonresume_validator',
      version='0.0.1',
      description='validates JSON resumes',
      long_description=read_file('README.md'),
      author='Kelvin Tay',
      author_email='kelvintay@gmail.com',
      url='https://github.com/kelvintaywl/jsonresume-validator',
      download_url='https://github.com/kelvintaywl/jsonresume-validator/tarball/0.0.1',
      keywords='jsonresume, validation, colander',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='jsonresume_validator',
      install_requires=requires,
      extras_require=extras_require)
