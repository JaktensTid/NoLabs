# coding: utf-8

"""
    ESM Fold

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from esmfold_microservice.models.run_esm_fold_prediction_response import RunEsmFoldPredictionResponse

class TestRunEsmFoldPredictionResponse(unittest.TestCase):
    """RunEsmFoldPredictionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RunEsmFoldPredictionResponse:
        """Test RunEsmFoldPredictionResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RunEsmFoldPredictionResponse`
        """
        model = RunEsmFoldPredictionResponse()
        if include_optional:
            return RunEsmFoldPredictionResponse(
                errors = [
                    ''
                    ],
                pdb_content = ''
            )
        else:
            return RunEsmFoldPredictionResponse(
                errors = [
                    ''
                    ],
        )
        """

    def testRunEsmFoldPredictionResponse(self):
        """Test RunEsmFoldPredictionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
