# -*- coding: utf-8 -*-

import unittest

import colander

from jsonresume.schema.resume import Resume as JSONResumeSchema
from jsonresume.tests.fixtures.load import (
    get_invalid_resumes,
    get_valid_resumes
)


class TestInvalidSchema(unittest.TestCase):

    def test_invalid_resumes(self):
        for resume in get_invalid_resumes():
            self.assertRaises(
                colander.Invalid,
                JSONResumeSchema().deserialize, resume.json
            )


class TestValidSchema(unittest.TestCase):

    def test_valid_resumes(self):
        for resume in get_valid_resumes():
            valid_json = JSONResumeSchema().deserialize(resume.json)
            self.assertIsNotNone(valid_json)
