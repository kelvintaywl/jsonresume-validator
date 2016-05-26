# -*- coding: utf-8 -*-

import colander


class InvalidResumeError(colander.Invalid):
    """ Raised when a JSON resume (as python object) has invalid schema """
