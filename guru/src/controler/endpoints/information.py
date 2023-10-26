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
from guru.src.model.personal_information.roger import Roger
from guru.src.controler.data_models.outputs import information_model


information = Namespace("information", description="This endpoint returns my information")


@information.route("/roger")
class FacialAttributes(Resource):
    """
    This class represents an endpoint for retrieving personal information.
    """

    @information.marshal_list_with(information_model)
    def get(self):
        """
        Retrieve and return personal information.

        :return: Personal information as a list.
        """
        return Roger()
