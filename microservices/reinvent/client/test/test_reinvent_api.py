# coding: utf-8

"""
    Reinvent4 API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from reinvent_microservice.api.reinvent_api import ReinventApi


class TestReinventApi(unittest.TestCase):
    """ReinventApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ReinventApi()

    def tearDown(self) -> None:
        pass

    def test_delete_api_reinvent_config_id_delete(self) -> None:
        """Test case for delete_api_reinvent_config_id_delete

        Delete
        """
        pass

    def test_get_all_configs_api_reinvent_get(self) -> None:
        """Test case for get_all_configs_api_reinvent_get

        Get All Configs
        """
        pass

    def test_get_config_api_reinvent_reinvent_config_id_get(self) -> None:
        """Test case for get_config_api_reinvent_reinvent_config_id_get

        Get Config
        """
        pass

    def test_learning_api_reinvent_config_id_start_learning_post(self) -> None:
        """Test case for learning_api_reinvent_config_id_start_learning_post

        Learning
        """
        pass

    def test_logs_api_reinvent_config_id_logs_get(self) -> None:
        """Test case for logs_api_reinvent_config_id_logs_get

        Logs
        """
        pass

    def test_params_api_reinvent_config_id_params_get(self) -> None:
        """Test case for params_api_reinvent_config_id_params_get

        Params
        """
        pass

    def test_sampling_api_reinvent_config_id_start_sampling_post(self) -> None:
        """Test case for sampling_api_reinvent_config_id_start_sampling_post

        Sampling
        """
        pass

    def test_save_params_api_reinvent_config_id_params_post(self) -> None:
        """Test case for save_params_api_reinvent_config_id_params_post

        Save Params
        """
        pass

    def test_smiles_api_reinvent_config_id_smiles_get(self) -> None:
        """Test case for smiles_api_reinvent_config_id_smiles_get

        Smiles
        """
        pass

    def test_stop_api_reinvent_config_id_jobs_stop_post(self) -> None:
        """Test case for stop_api_reinvent_config_id_jobs_stop_post

        Stop
        """
        pass


if __name__ == '__main__':
    unittest.main()