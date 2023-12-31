"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: information.py                                                         #
# Project: OrgGuardian                                                         #
# Last Modified: Thursday, 26th October 2023 12:12:25 am                       #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import Resource, Namespace
from guru.src.model.personal_information.fabian import Fabian
from guru.src.model.personal_information.roger import Roger
from guru.src.model.personal_information.telma import Telma
from guru.src.controler.data_models.outputs import information_model
from guru.src.controler.data_models.inputs import parser

information = Namespace(
    "information", description="This endpoints manage the user information"
)



@information.route("")
class Information(Resource):
    """
    This class represents an endpoint for retrieving personal information.
    """

    @information.marshal_list_with(information_model)
    def get(self):
        """
        Retrieve and return personal information.
        :return: Personal information as a list.
        """
        # result = Roger() + Telma()
        return [Roger(), Telma(), Fabian()]

    @information.expect(parser, information_model)
    def post(self):
        """
        Add new personal information.
        :param name: Name of the user.
        :param files: CV file to upload.
        :return: JSON response with the name and CV filename.
        """
        args = parser.parse_args()
        name = args["name"]
        cv_file = args["files"]
        cv_filename = cv_file.filename
        cv_file.save(f"guru/files/{cv_filename}")

        return {"name": name, "cv_filename": "cv_filename"}, 201
