# Change Log

## [Unreleased]
- added codeclimate test coverage reporting

## [0.1.3] - 2016-06-07
- cleaned up fixture files

## [0.1.2] - 2016-06-04
### Changed
- made end dates not compulsory / required (e.g., in work experiences)
- made urls not compulsory / required

## [0.1.1] - 2016-05-27
### Added
- added MIT license
- added links to sample Flask app using this library

## [0.1.0] - 2016-05-26
### Added
- added new Resume class wrapped on Resume Schema for easier interface on validation
- added custom Exception class raised when invalid resume format

### Changed
- shifted validators to schema directory for housekeeping
- updated with more examples on Resume class usage in README

## [0.0.2] - 2016-05-25
### Changed
- updated README to include example code

## [0.0.1b] - 2016-05-24
### Changed
- fixed setup.py in order to upload package to PyPI

## [0.0.1] - 2016-04-13
### Added
- created Resume Schema object for use with colander (validation)
- included unit tests on valid and invalid JSON resume files
