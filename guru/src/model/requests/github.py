"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: github.py                                                              #
# Project: OrgGuardian                                                         #
# Last Modified: Sunday, 10th December 2023 3:45:58 am                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


from os import getenv
import requests


bearer_token = getenv("GITHUB_TOKEN")


class Github:
    """github class"""

    def trigger(self):
        """Trigger a workfloew smoke testing"""
        url = "https://api.github.com/repos/Rogerrenjifo/ScreenPlayPythonFramework/actions/workflows/smoke_testing.yml/dispatches"

        headers = {
            "Accept": "application/vnd.github+json",
            "Authorization": bearer_token,
            "X-GitHub-Api-Version": "2022-11-28",
        }

        payload = {
            "ref": "main",
            "inputs": {
                "logLevel": "debug",
                "tags": True,
                "environment": "dev",
            },
        }
        print(bearer_token)
        response = requests.post(url, headers=headers, json=payload)

        return response.status_code
