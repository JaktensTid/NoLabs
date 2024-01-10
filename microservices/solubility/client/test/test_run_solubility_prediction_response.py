# coding: utf-8

"""
    Solubility api

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from solubility_microservice.models.run_solubility_prediction_response import RunSolubilityPredictionResponse

class TestRunSolubilityPredictionResponse(unittest.TestCase):
    """RunSolubilityPredictionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunSolubilityPredictionResponse:
        """Test RunSolubilityPredictionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunSolubilityPredictionResponse`
        """
        model = RunSolubilityPredictionResponse()
        if include_optional:
            return RunSolubilityPredictionResponse(
                errors = [
                    ''
                    ],
                soluble_confidence = 1.337
            )
        else:
            return RunSolubilityPredictionResponse(
                errors = [
                    ''
                    ],
                soluble_confidence = 1.337,
        )
        """

    def testRunSolubilityPredictionResponse(self):
        """Test RunSolubilityPredictionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()