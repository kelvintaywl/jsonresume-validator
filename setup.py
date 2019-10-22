# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


VERSION = '0.1.5'

requires = [
    "colander==1.7.0",
    "pycountry==17.9.23"
]

extras_require = {
    "test": [
        "nose",
        "coverage",
        "flake8",
        "codeclimate-test-reporter"
    ]
}

setup(name='jsonresume-validator',
      version=VERSION,
      description='validates JSON resumes',
      author='Kelvin Tay',
      author_email='kelvintay@gmail.com',
      url='https://github.com/kelvintaywl/jsonresume-validator',
      download_url='https://github.com/kelvintaywl/jsonresume-validator/tarball/{}'.format(VERSION),
      keywords='jsonresume, validation, colander',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='jsonresume',
      install_requires=requires,
      extras_require=extras_require)
