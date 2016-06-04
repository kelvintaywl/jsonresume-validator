# -*- coding: utf-8 -*-

import colander


class Experience(colander.MappingSchema):
    startDate = colander.SchemaNode(colander.Date())
    endDate = colander.SchemaNode(colander.Date(), missing=None)


class Highlights(colander.SequenceSchema):
    highlight = colander.SchemaNode(colander.String(), missing=None)


class Courses(colander.SequenceSchema):
    course = colander.SchemaNode(colander.String())


class Work(Experience):
    company = colander.SchemaNode(colander.String())
    position = colander.SchemaNode(colander.String())
    summary = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)
    highlights = Highlights()


class Volunteer(Experience):
    organization = colander.SchemaNode(colander.String())
    position = colander.SchemaNode(colander.String())
    summary = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)
    highlights = Highlights()


class Education(Experience):
    institution = colander.SchemaNode(colander.String())
    studyType = colander.SchemaNode(colander.String())
    area = colander.SchemaNode(colander.String())
    gpa = colander.SchemaNode(colander.Decimal())
    courses = Courses()
