"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: information_by_id.py                                                   #
# Project: OrgGuardian                                                         #
# Last Modified: Thursday, 30th November 2023 1:04:09 am                       #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask_restx import Resource, Namespace
from guru.src.model.personal_information.roger import Roger
from guru.src.controler.data_models.outputs import information_model
from guru.src.controler.data_models.inputs import parser2


information_by_id = Namespace(
    "information", description="This endpoints manage the user informations"
)


@information_by_id.route("/<string:user_id>")
class InformationById(Resource):
    """
    This class represents an endpoint for retrieving personal information.
    """
    @information_by_id.marshal_with(information_model)
    def get(self, user_id=None):
        """
        Retrieve and return personal information.
        :return: Personal information as a json.
        """
        print(user_id)
        return Roger()

    @information_by_id.expect(information_model)
    def put(self):
        """
        Update personal information.
        :param name: Updated name of the user.
        :param other_field: Additional field to update.
        :return: JSON response with the updated information.
        """
        args = information_model.payload
        return args, 201

    @information_by_id.expect(parser2)
    def delete(self):
        """
        Delete personal information.
        :param id: ID of the user to delete.
        :return: JSON response with the deleted user information.
        """
        args = parser2.parse_args()
        return args, 200
