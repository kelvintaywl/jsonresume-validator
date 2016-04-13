# -*- coding: utf-8 -*-

import colander


class Keywords(colander.SequenceSchema):
    keyword = colander.SchemaNode(colander.String())
