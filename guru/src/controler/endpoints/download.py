"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: download.py                                                            #
# Project: OrgGuardian                                                         #
# Last Modified: Sunday, 5th November 2023 12:05:03 pm                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from flask import request, send_from_directory
from flask_restx import Resource, Namespace

download = Namespace("download", description="This endpoints download the CV documents")


@download.route("")
class Download(Resource):
    """Defines download file method --> url"""

    def get(self):
        """Downloads file"""
        file_name = request.args["file_name"]
        print(file_name)
        a = "C:/Users/Roger/Documents/projects/developer_projects/JobApplyGuru/guru/files"
        return send_from_directory(directory=a, path=file_name, as_attachment=False)
