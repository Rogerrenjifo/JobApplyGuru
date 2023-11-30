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
