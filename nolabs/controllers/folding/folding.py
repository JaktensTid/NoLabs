from typing import Annotated, List

from fastapi import APIRouter, Depends, UploadFile, File, Form

from nolabs.api_models.amino_acid.common_models import RunAminoAcidRequest
from nolabs.api_models.amino_acid.folding import RunFoldingResponse, GetExperimentResponse
from nolabs.controllers.folding.dependencies import run_folding_feature_dependency, \
    get_experiments_feature_dependency, \
    get_experiment_feature_dependency, delete_experiment_feature_dependency, change_experiment_name_dependency, \
    create_experiment_dependency
from nolabs.modules.experiment.create_experiment import CreateExperimentFeature
from nolabs.modules.experiment.get_experiments import GetExperimentsFeature
from nolabs.modules.experiment.delete_experiment import DeleteExperimentFeature
from nolabs.modules.experiment.change_experiment_name import ChangeExperimentNameFeature
from nolabs.api_models.experiment import ChangeExperimentNameRequest, ExperimentMetadataResponse
from nolabs.modules.amino_acid.folding.get_experiment import GetExperimentFeature
from nolabs.modules.amino_acid.folding.run_folding import RunFoldingFeature

router = APIRouter(
    prefix='/api/v1/folding',
    tags=['folding']
)


@router.post('/inference')
async def inference(
        feature: Annotated[RunFoldingFeature, Depends(run_folding_feature_dependency)],
        experiment_name: str = Form(),
        experiment_id: str = Form(None),
        amino_acid_sequence: str = Form(None),
        fastas: List[UploadFile] = File(default_factory=list)
) -> RunFoldingResponse:
        return await feature.handle(RunAminoAcidRequest(
            experiment_name=experiment_name,
            experiment_id=experiment_id,
            amino_acid_sequence=amino_acid_sequence,
            fastas=fastas
        ))


@router.get('/experiments')
async def experiments(feature: Annotated[GetExperimentsFeature, Depends(get_experiments_feature_dependency)]) -> List[ExperimentMetadataResponse]:
    return feature.handle()


@router.get('/get-experiment')
async def get_experiment(experiment_id: str, feature: Annotated[
    GetExperimentFeature, Depends(get_experiment_feature_dependency)]) -> GetExperimentResponse:
    return await feature.handle(experiment_id)


@router.delete('/delete-experiment')
async def delete_experiment(experiment_id: str, feature: Annotated[
    DeleteExperimentFeature, Depends(delete_experiment_feature_dependency)]):
    return feature.handle(experiment_id)



@router.post('/change-experiment-name')
async def change_experiment_name(request: ChangeExperimentNameRequest, feature: Annotated[
    ChangeExperimentNameFeature, Depends(change_experiment_name_dependency)]):
    return feature.handle(request)

@router.get('/create-experiment')
async def create_experiment(feature: Annotated[CreateExperimentFeature, Depends(create_experiment_dependency)]) -> ExperimentMetadataResponse:
    return await feature.handle()

