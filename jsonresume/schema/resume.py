# -*- coding: utf-8 -*-

import colander

from jsonresume.schema.components import (
    ability,
    achievement,
    experience,
    personal
)


class WorkExperiences(colander.SequenceSchema):
    work = experience.Work()


class VolunteerExperiences(colander.SequenceSchema):
    volunteer = experience.Volunteer()


class EducationExperiences(colander.SequenceSchema):
    education = experience.Education()


class Awards(colander.SequenceSchema):
    award = achievement.Award()


class Publications(colander.SequenceSchema):
    publication = achievement.Publication()


class Skills(colander.SequenceSchema):
    skill = ability.Skill()


class Languages(colander.SequenceSchema):
    language = ability.Language()


class Interests(colander.SequenceSchema):
    interest = personal.Interest()


class Resume(colander.MappingSchema):
    """ Schema that maps all necessary information required in the JSON resume """
    basics = personal.BasicInfo()
    work = WorkExperiences()
    volunteer = VolunteerExperiences()
    education = EducationExperiences()
    awards = Awards()
    publications = Publications()
    references = personal.References()
    skills = Skills()
    languages = Languages()
    interests = Interests()
