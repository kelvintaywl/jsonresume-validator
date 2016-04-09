# -*- coding: utf-8 -*-

import json
import os


FIXTURE_DIR = os.path.dirname(os.path.realpath(__file__))
RESUME_DIR = os.path.join(FIXTURE_DIR, 'resumes')


class TestSchemaFile(object):

    def __init__(self, filename, json, remarks=None, valid=True):
        self.filename = filename
        self.json = json
        self.remarks = remarks
        self.valid = valid


def get_invalid_resumes():
    """ Loads invalid json resumes for unit tests, returning a list of TestSchemaFile """
    folder = os.path.join(RESUME_DIR, 'invalid')
    return [
        TestSchemaFile(
            invalid_resume_filename,
            json.load(
                open(os.path.join(folder, invalid_resume_filename), 'r')
            ),
            remarks=os.path.splitext(invalid_resume_filename)[0],
            valid=False
        )
        for invalid_resume_filename in os.listdir(folder)
    ]


def get_valid_resumes():
    """ Loads valid json resumes for unit tests, returning a list of TestSchemaFile """
    folder = os.path.join(RESUME_DIR, 'valid')
    return [
        TestSchemaFile(
            valid_resume_filename,
            json.load(
                open(os.path.join(folder, valid_resume_filename), 'r')
            ),
            remarks='',
            valid=True
        )
        for valid_resume_filename in os.listdir(folder)
    ]
