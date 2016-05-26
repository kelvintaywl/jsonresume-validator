# -*- coding: utf-8 -*-

import unittest

from colander import Invalid

from jsonresume.schema.validators import is_valid_country_code


class TestCountryCodeValidation(unittest.TestCase):

    def test_all(self):
        for country_code, exc_class in [
            ('JP', None),
            ('FR', None),
            ('MEX', Invalid)
        ]:
            if isinstance(exc_class, Exception):
                self.assertRaises(
                    exc_class,
                    is_valid_country_code, '', country_code
                )
            elif exc_class is None:
                self.assertIsNone(is_valid_country_code('', country_code))
