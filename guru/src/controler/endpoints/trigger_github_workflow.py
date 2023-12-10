"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: trigger_github_workflow.py                                             #
# Project: OrgGuardian                                                         #
# Last Modified: Sunday, 10th December 2023 2:29:22 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from os import getenv
from flask_restx import Resource, Namespace
from guru.src.controler.data_models.inputs import slack_request
from guru.src.model.requests.github import Github

trigger = Namespace(
    "trigger", description="This endpointstriger a GitHub Actions Workflow"
)

@trigger.route("")
class TriggerGitHubWorkflow(Resource):
    """
    Represents an endpoint for triggering a GitHub workflow based on a Slack request.
    """
    @trigger.expect(slack_request)
    def post(self):
        """
        Triggers a GitHub workflow based on a Slack request.

        :param token: Slack verification token.
        :return: JSON response indicating the success of the GitHub workflow trigger.
        :rtype: dict
        """
        args = slack_request.parse_args()
        token = args.get("token")
        result = Github().trigger()
        if token == getenv("SLACK_TOKEN"):
            return {"message": result}, 201
        return {"message": result}, 201
