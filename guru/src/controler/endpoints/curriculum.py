"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: curriculum.py                                                          #
# Project: OrgGuardian                                                         #
# Last Modified: Sunday, 5th November 2023 11:56:02 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask import request
from flask_restx import Resource, Namespace
from guru.src.controler.data_models.outputs import curriculum_model


cv = Namespace("information", description="This endpoints manage the user information")


@cv.route("/cv_download_link")
class Curriculum(Resource):
    """
    This class represents an endpoint for retrieving personal cv.
    """

    @cv.marshal_list_with(curriculum_model)
    def get(self):
        """
        Retrieve and return personal cv.
        :return: Personal cv
        """
        url = request.url_root + "download?file_name=" + "cv_rrrt.pdf"
        return {"url": url}
