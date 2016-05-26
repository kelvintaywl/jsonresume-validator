# -*- coding: utf-8 -*-

from __future__ import absolute_import

import colander


def is_valid_country_code(_, value):
    # TODO: check country code for actual validity
    if len(value) == 2:
        return None
    raise colander.Invalid('invalid country code: {}'.format(value))
