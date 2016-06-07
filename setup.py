# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

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

setup(name='jsonresume-validator',
      version='0.1.3',
      description='validates JSON resumes',
      author='Kelvin Tay',
      author_email='kelvintay@gmail.com',
      url='https://github.com/kelvintaywl/jsonresume-validator',
      download_url='https://github.com/kelvintaywl/jsonresume-validator/tarball/0.1.3',
      keywords='jsonresume, validation, colander',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      test_suite='jsonresume',
      install_requires=requires,
      extras_require=extras_require)
