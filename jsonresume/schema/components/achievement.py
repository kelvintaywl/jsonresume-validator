# -*- coding: utf-8 -*-

import colander


class Award(colander.MappingSchema):
    title = colander.SchemaNode(colander.String())
    awarder = colander.SchemaNode(colander.String())
    date = colander.SchemaNode(colander.Date())
    summary = colander.SchemaNode(colander.String())


class Publication(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    publisher = colander.SchemaNode(colander.String())
    releaseDate = colander.SchemaNode(colander.Date())
    summary = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)
