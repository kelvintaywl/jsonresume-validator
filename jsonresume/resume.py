# -*- coding: utf-8 -*-

import colander

from jsonresume.exceptions import InvalidResumeError
from jsonresume.schema.resume import Resume as ResumeSchema


class Resume(object):

    def __init__(self, data):
        self.original_data = data

    def validate(self):
        try:
            ResumeSchema().deserialize(self.original_data)
        except colander.Invalid as e:
            raise InvalidResumeError(e)
        else:
            pass

    def is_valid(self):
        try:
            self.validate()
        except InvalidResumeError:
            return False
        else:
            return True
