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
from flask_sqlalchemy import SQLAlchemy

load_dotenv()

PORT = int(getenv("PORT_ML", "5000"))
HOST = str(getenv("HOST_ML", "0.0.0.0"))


api = Api(
    version="1.0.0",
    title="Job Apply Guru API",
    description='<h3 style="color: #007bff; text-align: center; margin-bottom: 20px;"> \
        JobApplyGuru streamlines job applications by offering CV storage, \
        modification, and dynamic cover letter generation based on job offer input.\
        Elevate your career prospects with this innovative API (It is still in progress)</h3>',
    license="MIT",
    license_url="https://opensource.org/licenses/MIT",
    contact="Roger Renjifo",
    contact_url="https://github.com/Rogerrenjifo/JobApplyGuru",
    contact_email="john.doe@example.com",
    authorizations={
        "apiKey": {"type": "apiKey", "in": "header", "name": "Authorization"}
    },
    security="apiKey",
)


db = SQLAlchemy()
user = getenv("DB_USERNAME")
key = getenv("DB_PASSWORD")
server = getenv("DB_SERVER")
database = getenv("DB_DATABASE")
driver = getenv("DB_DRIVER")

ODBC = f"mssql+pyodbc://{user}:{key}@{server}/{database}?{driver}"
