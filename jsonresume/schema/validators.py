# -*- coding: utf-8 -*-

from __future__ import absolute_import

import pycountry

import colander

# COUNTRY_CODES stores the alpha-2 code reprsentation of countries
# in accordance to ISO 3166-1
# see https://en.wikipedia.org/wiki/ISO_3166-1
COUNTRY_CODES = [c.alpha_2 for c in pycountry.countries]


def is_valid_country_code(_, value):
    if value not in COUNTRY_CODES:
        raise colander.Invalid(
            'invalid ISO 3166-1 country code: [{}].' +
            ' Please see https://en.wikipedia.org/wiki/ISO_3166-1'.format(value)
        )
