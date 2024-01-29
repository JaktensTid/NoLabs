from nolabs.features.drug_discovery.data_models.result import JobId
from nolabs.features.drug_discovery.services.ligand_file_management import LigandsFileManagement
from nolabs.features.drug_discovery.services.result_file_management import ResultsFileManagement
from nolabs.api_models.drug_discovery import GetResultDataRequest, GetResultDataResponse, \
    GetResultsListRequest, GetResultsListResponse, ResultMetaData, \
    CheckResultDataAvailableRequest, CheckResultDataAvailableResponse
from nolabs.domain.experiment import ExperimentId
from nolabs.features.drug_discovery.data_models.target import TargetId
from nolabs.features.drug_discovery.data_models.ligand import LigandId
from nolabs.features.drug_discovery.services.target_file_management import TargetsFileManagement


class GetResultDataFeature:
    def __init__(self, file_management: ResultsFileManagement):
        self._file_management = file_management

    def handle(self, request: GetResultDataRequest) -> GetResultDataResponse:
        experiment_id = ExperimentId(request.experiment_id)
        target_id = TargetId(request.target_id)
        ligand_id = LigandId(request.ligand_id)
        job_id = JobId(request.job_id)

        result_data = self._file_management.get_docking_result_data(experiment_id,
                                                                    target_id,
                                                                    ligand_id,
                                                                    job_id)

        return GetResultDataResponse(predicted_pdb=result_data.predicted_pdb,
                                     predicted_sdf=result_data.predicted_sdf,
                                     plddt_array=result_data.plddt_array,
                                     job_id=job_id.value)


class GetResultsListFeature:
    def __init__(self, results_file_management: ResultsFileManagement,
                 targets_file_management: TargetsFileManagement,
                 ligand_file_management: LigandsFileManagement):
        self._results_file_management = results_file_management
        self._targets_file_management = targets_file_management
        self._ligands_file_management = ligand_file_management

    def handle(self, request: GetResultsListRequest) -> GetResultsListResponse:
        experiment_id = ExperimentId(request.experiment_id)

        results_list = []

        for target in self._targets_file_management.get_targets_list(experiment_id):
            target_id = TargetId(target.target_id)
            for ligand in self._ligands_file_management.get_ligands_list(experiment_id, target_id):
                ligand_id = LigandId(ligand.ligand_id)
                for result in self._results_file_management.get_results_list(experiment_id, target_id, ligand_id):
                    results_list.append(ResultMetaData(job_id=result.job_id,
                                                       target_id=target_id.value,
                                                       ligand_id=ligand_id.value))

        return GetResultsListResponse(results_list=results_list)


class CheckResultAvailable:
    def __init__(self, file_management: ResultsFileManagement):
        self._file_management = file_management

    def handle(self, request: CheckResultDataAvailableRequest) -> CheckResultDataAvailableResponse:
        experiment_id = ExperimentId(request.experiment_id)
        target_id = TargetId(request.target_id)
        ligand_id = LigandId(request.ligand_id)
        job_id = JobId(request.job_id)

        is_available = self._file_management.check_result_data_available(experiment_id,
                                                                         target_id,
                                                                         ligand_id,
                                                                         job_id)

        return CheckResultDataAvailableResponse(result_available=is_available)