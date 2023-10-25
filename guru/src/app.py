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
from guru.src.configuration import api, PORT, HOST

# from guardian.src.controller.endpoints.facial_attributes import ns as facial_attributes
# from guardian.src.controller.endpoints.information import ns as information

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
api.init_app(app)

# api.add_namespace(information)
# api.add_namespace(facial_attributes)

if __name__ == "__main__":
    app.run(host=HOST, port=PORT)
