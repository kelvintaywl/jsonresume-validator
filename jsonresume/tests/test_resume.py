# -*- coding: utf-8 -*-

import unittest

from jsonresume import Resume
from jsonresume.exceptions import InvalidResumeError
from jsonresume.tests.fixtures.load import (
    get_invalid_resumes,
    get_valid_resumes
)


class TestResume(unittest.TestCase):

    def test_validate(self):
        for resume_data in get_invalid_resumes():
            resume = Resume(resume_data.json)
            self.assertRaises(
                InvalidResumeError,
                resume.validate
            )

        for resume_data in get_valid_resumes():
            resume = Resume(resume_data.json)
            resume.validate()  # should not raise any error for valid resumes

    def test_is_valid(self):
        for resume_data in get_invalid_resumes():
            resume = Resume(resume_data.json)
            self.assertFalse(resume.is_valid())

        for resume_data in get_valid_resumes():
            resume = Resume(resume_data.json)
            self.assertTrue(resume.is_valid())
