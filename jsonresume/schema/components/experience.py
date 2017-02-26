# -*- coding: utf-8 -*-

import colander


class Experience(colander.MappingSchema):
    startDate = colander.SchemaNode(colander.Date())
    endDate = colander.SchemaNode(colander.Date(), missing=None)


class Highlights(colander.SequenceSchema):
    highlight = colander.SchemaNode(colander.String(), missing=None)


class Courses(colander.SequenceSchema):
    course = colander.SchemaNode(colander.String())


class Career(Experience):
    position = colander.SchemaNode(colander.String())
    summary = colander.SchemaNode(colander.String())
    website = colander.SchemaNode(colander.String(), validator=colander.url, missing=None)
    highlights = Highlights()


class Work(Career):
    company = colander.SchemaNode(colander.String())


class Volunteer(Career):
    organization = colander.SchemaNode(colander.String())


class Education(Experience):
    institution = colander.SchemaNode(colander.String())
    studyType = colander.SchemaNode(colander.String())
    area = colander.SchemaNode(colander.String())
    gpa = colander.SchemaNode(colander.Decimal())
    courses = Courses()
