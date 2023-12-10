"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: inputs.py                                                              #
# Project: OrgGuardian                                                         #
# Last Modified: Thursday, 30th November 2023 1:07:00 am                       #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from werkzeug.datastructures import FileStorage
from flask_restx import reqparse


parser = reqparse.RequestParser()
parser.add_argument("rate", type=int, help="Rate cannot be converted", location="form")
parser.add_argument("name", location="form")
parser.add_argument("files", type=FileStorage, location="files")
parser2 = reqparse.RequestParser()
parser2.add_argument("id", help="the id of the user to be deleted ")


slack_request = reqparse.RequestParser()
slack_request.add_argument("token", help="token ", location="form")
slack_request.add_argument("team_id", help="team_id ", location="form")
slack_request.add_argument("team_domain", help="team_domain ", location="form")
slack_request.add_argument("channel_id", help="channel_id ", location="form")
slack_request.add_argument("channel_name", help="channel_name ", location="form")
slack_request.add_argument("user_id", help="user_id ", location="form")
slack_request.add_argument("command", help="command ", location="form")
slack_request.add_argument("text", help="text ", location="form")
slack_request.add_argument("response_url", help="response_url ", location="form")
