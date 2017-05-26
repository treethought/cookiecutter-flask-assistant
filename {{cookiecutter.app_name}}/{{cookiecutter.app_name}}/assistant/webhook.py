# -*- coding: utf-8 -*-

# {{ cookiecutter.app_name }}
# By {{ cookiecutter.author_name }} <{{ cookiecutter.author_email }}>
#
# {{ cookiecutter.project_short_description }}

import logging

from flask import Blueprint
from flask_assistant import Assistant, ask, tell

blueprint = Blueprint('assist', __name__, url_prefix='/assist')
assist = Assistant(blueprint=blueprint)

logging.getLogger('flask_assistant').setLevel(logging.DEBUG)


@assist.action('Greetings')
def welcome():
    speech = 'Welcome, to {}!'.format({{ cookiecutter.app_name }})
    return ask(speech)

