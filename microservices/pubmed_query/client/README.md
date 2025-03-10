# pubmed-query-microservice
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
import pubmed_query_microservice
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import pubmed_query_microservice
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import pubmed_query_microservice
from pubmed_query_microservice.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = pubmed_query_microservice.Configuration(
    host = "http://localhost"
)



# Enter a context with an instance of the API client
with pubmed_query_microservice.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pubmed_query_microservice.DefaultApi(api_client)

    try:
        # Get Running Jobs
        api_response = api_instance.get_running_jobs_jobs_running_get()
        print("The response of DefaultApi->get_running_jobs_jobs_running_get:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling DefaultApi->get_running_jobs_jobs_running_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**get_running_jobs_jobs_running_get**](docs/DefaultApi.md#get_running_jobs_jobs_running_get) | **GET** /jobs/running | Get Running Jobs
*DefaultApi* | [**is_job_running_job_job_id_is_running_get**](docs/DefaultApi.md#is_job_running_job_job_id_is_running_get) | **GET** /job/{job_id}/is-running | Is Job Running
*DefaultApi* | [**search_search_pubmed_articles_post**](docs/DefaultApi.md#search_search_pubmed_articles_post) | **POST** /search_pubmed_articles | Search


## Documentation For Models

 - [ApiKey](docs/ApiKey.md)
 - [FetchedArticle](docs/FetchedArticle.md)
 - [HTTPValidationError](docs/HTTPValidationError.md)
 - [IsJobRunningResponse](docs/IsJobRunningResponse.md)
 - [JobId](docs/JobId.md)
 - [PubMedSearchRequest](docs/PubMedSearchRequest.md)
 - [PubMedSearchResponse](docs/PubMedSearchResponse.md)
 - [ValidationError](docs/ValidationError.md)
 - [ValidationErrorLocInner](docs/ValidationErrorLocInner.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization

Endpoints do not require authorization.


## Author




