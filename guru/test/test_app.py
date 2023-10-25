"""
# ############################################################################ #
#                                                                              #
# MIT License                                                                  #
#                                                                              #
# Copyright (c) 2023, Roger Renjifo Tarquino                                   #
#                                                                              #
#                                                                              #
# File: test_app.py                                                            #
# Project: OrgGuardian                                                         #
# Last Modified: Tuesday, 24th October 2023 8:26:19 pm                         #
# Modified By: Roger Renjifo (rrrenjifo@gmail.com>)                            #
#                                                                              #
# ############################################################################ #
"""


import unittest
from guru.src.app import app


class TestFlaskApp(unittest.TestCase):
    """
    This test suite contains unit tests for the Flask app.
    """

    def setUp(self):
        """
        Set up the test client for the Flask app.
        """
        self.app = app.test_client()

    def test_run_the_app(self):
        """
        Test if the Flask app runs successfully.

        This test sends a GET request to the root URL ('/') and checks if the
        response status code is 200, indicating a successful response.
        """
        response = self.app.get("/")
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()
