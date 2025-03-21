# coding: utf-8

# flake8: noqa

"""
    Linkup API

    The Linkup API allows you to retrieve web content. Use the `/search` endpoint to query the web for answers or search results, and the `/content` endpoint to retrieve webpage content from premium source partners.  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from .api.default_api import DefaultApi
# import ApiClient
from .api_client import ApiClient
from .configuration import Configuration
# import models into sdk package
from .models.search_request import SearchRequest
from .models.search_request1 import SearchRequest1
from .models.search_results import SearchResults
from .models.sourced_answer import SourcedAnswer
from .models.structured import Structured
