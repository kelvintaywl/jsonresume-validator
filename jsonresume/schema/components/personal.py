# -*- coding: utf-8 -*-

import colander

from jsonresume.schema.components.common import Keywords
from jsonresume.schema.validators import is_valid_country_code


class Profile(colander.MappingSchema):
    network = colander.SchemaNode(colander.String())
    username = colander.SchemaNode(colander.String())
    url = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)


class Profiles(colander.SequenceSchema):
    profile = Profile()


class Reference(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    reference = colander.SchemaNode(colander.String())


class References(colander.SequenceSchema):
    reference = Reference()


class Location(colander.MappingSchema):
    address = colander.SchemaNode(colander.String())
    city = colander.SchemaNode(colander.String())
    postalCode = colander.SchemaNode(colander.String())
    countryCode = colander.SchemaNode(colander.String(), validator=is_valid_country_code)
    region = colander.SchemaNode(colander.String())


class BasicInfo(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    label = colander.SchemaNode(colander.String())
    picture = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)
    email = colander.SchemaNode(colander.String(), validator=colander.Email())
    phone = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)
    summary = colander.SchemaNode(colander.String())
    location = Location()
    profiles = Profiles()


class Interest(colander.MappingSchema):
    name = colander.SchemaNode(colander.String())
    keywords = Keywords()
