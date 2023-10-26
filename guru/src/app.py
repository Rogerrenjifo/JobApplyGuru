"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: app.py                                                                 #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 8:03:17 pm                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask import Flask
from guru.src.configuration import api
from guru.src.controler.endpoints.information import information

app = Flask(__name__)
api.init_app(app)

api.add_namespace(information)
if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
