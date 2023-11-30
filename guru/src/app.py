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
from guru.src.configuration import api, db, ODBC
from guru.src.controler.endpoints.information import information
from guru.src.controler.endpoints.curriculum import cv
from guru.src.controler.endpoints.download import download
from guru.src.controler.endpoints.information_by_id import information_by_id


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = ODBC
app.config.SWAGGER_UI_DOC_EXPANSION = "list"

api.init_app(app)
db.init_app(app)
api.add_namespace(cv)
api.add_namespace(information)
api.add_namespace(information_by_id)
api.add_namespace(download)


if __name__ == "__main__":
    app.run(port=80, host="0.0.0.0")
