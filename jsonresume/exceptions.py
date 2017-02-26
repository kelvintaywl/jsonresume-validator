# -*- coding: utf-8 -*-

import colander


class InvalidResumeError(colander.Invalid):
    """Exception when a JSON resume (as python object) has invalid schema.

    Subclass of colander.Invalid.
     """
    pass
