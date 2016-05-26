[![Build Status](https://travis-ci.org/kelvintaywl/jsonresume-validator.svg?branch=master)](https://travis-ci.org/kelvintaywl/jsonresume-validator)

# JSON Resume Validator

Python tool to validate JSON resumes to ensure that they are according to the [defined schema](https://jsonresume.org/schema/)

> For more information on JSON resumes, please see the [official JSON Resume initiative](https://jsonresume.org)


## Installing

```
$ pip install jsonresume-validator
```

## Example uses

1. Using Resume class

```python
import json

from jsonresume import Resume
from jsonresume.exceptions import InvalidResumeError

MY_RESUME_JSON_FILEPATH = ""

with open(MY_RESUME_JSON_FILEPATH, 'r') as json_file:
	data = json.load(json_file)
	r = Resume(data)
	if r.is_valid():
		print("Yay! We're good")
	else:
		print("Houston, we have a problem")

	# if we prefer catching exceptions...
	try:
		r.validate()
	except InvalidResumeError:
		# deal with invalid resume
		pass

```

2. Using Schemas (colander)

```python

import json
import logging

import colander

from jsonresume.schema.resume import Resume as ResumeSchema

RESUME_JSON_FILEPATH = "put your resume.json file path here"

try:
	with open(RESUME_JSON_FILEPATH, 'r') as fil:
		resume_json = json.load(fil)
except (IOError, ValueError):
	logging.exception("json file could not be loaded. Perhaps file path [{}] is incorrect".format(RESUME_JSON_FILEPATH))
else:
	try:
		resume = ResumeSchema().deserialize(resume_json)
	except colander.Invalid:
		logging.exception("resume has invalid JSON format")
	else:
		logging.info("Resume structure: {}".format(resume))

```

