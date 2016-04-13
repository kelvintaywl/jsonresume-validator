# -*- coding: utf-8 -*-

import colander

from jsonresume.schema.components.common import Keywords


class Language(colander.MappingSchema):
    language = colander.SchemaNode(colander.String())
    fluency = colander.SchemaNode(colander.String())


class Skill(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    level = colander.SchemaNode(colander.String(), missing=None)
    keywords = Keywords()
