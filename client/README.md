# esmfold-microservice
No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 0.1.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import esmfold_microservice
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import esmfold_microservice
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import esmfold_microservice
from esmfold_microservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = esmfold_microservice.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with esmfold_microservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = esmfold_microservice.DefaultApi(api_client)
    run_esm_fold_prediction_request = esmfold_microservice.RunEsmFoldPredictionRequest() # RunEsmFoldPredictionRequest | 

    try:
        # Predict
        api_response = api_instance.predict_run_folding_post(run_esm_fold_prediction_request)
        print("The response of DefaultApi->predict_run_folding_post:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->predict_run_folding_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**predict_run_folding_post**](docs/DefaultApi.md#predict_run_folding_post) | **POST** /run-folding | Predict


## Documentation For Models

 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [RunEsmFoldPredictionRequest](docs/RunEsmFoldPredictionRequest.md)
 - [RunEsmFoldPredictionResponse](docs/RunEsmFoldPredictionResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author



