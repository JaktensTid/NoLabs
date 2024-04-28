# coding: utf-8

"""
    NoLabs

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest
import datetime

from nolabs_microservice.models.experiment_metadata_response import ExperimentMetadataResponse

class TestExperimentMetadataResponse(unittest.TestCase):
    """ExperimentMetadataResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ExperimentMetadataResponse:
        """Test ExperimentMetadataResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ExperimentMetadataResponse`
        """
        model = ExperimentMetadataResponse()
        if include_optional:
            return ExperimentMetadataResponse(
                id = None,
                name = None,
                var_date = None
            )
        else:
            return ExperimentMetadataResponse(
                id = None,
                name = None,
                var_date = None,
        )
        """

    def testExperimentMetadataResponse(self):
        """Test ExperimentMetadataResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()