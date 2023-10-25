"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: configuration.py                                                       #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 7:42:14 pm                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from os import getenv
from dotenv import load_dotenv
from flask_restx import Api


load_dotenv()

PORT = int(getenv("PORT_ML", "5000"))
HOST = str(getenv("HOST_ML", "0.0.0.0"))


api = Api(version="1.0", title="Sample API", description="A sample API")
