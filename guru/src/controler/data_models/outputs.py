"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: outputs.py                                                             #
# Project: OrgGuardian                                                         #
# Last Modified: Thursday, 26th October 2023 12:13:42 am                       #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import fields
from guru.src.configuration import api


information_model = api.model(
    "Roger", {"name": fields.String, "linkedin": fields.String, "email": fields.String}
)

curriculum_model = api.model(
    "curriculum", {'url': fields.String}
)
