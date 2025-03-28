# coding: utf-8

"""
    Rootly API v1

    # How to generate an API Key? - **Account** > **Manage API keys** > **Generate New API Key**  # JSON:API Specification Rootly is using **JSON:API** (https://jsonapi.org) specification: - JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests. - JSON:API is designed to minimize both the number of requests and the amount of data transmitted between clients and servers. This efficiency is achieved without compromising readability, flexibility, or discoverability. - JSON:API requires use of the JSON:API media type (**application/vnd.api+json**) for exchanging data.  # Authentication and Requests We use standard HTTP Authentication over HTTPS to authorize your requests. ```   curl --request GET \\ --header 'Content-Type: application/vnd.api+json' \\ --header 'Authorization: Bearer YOUR-TOKEN' \\ --url https://api.rootly.com/v1/incidents ```  <br/>  # Rate limiting - There is a default limit of approximately **3000** **GET** calls **per API key** every **60 seconds**. The limit is calculated over a **60-second sliding window** looking back from the current time. While the limit can be configured to support higher thresholds, you must first contact your **Rootly Customer Success Manager** to make any adjustments. - There is a default limit of approximately **3000** **PUT**, **POST**, **PATCH** or **DELETE** calls **per API key** every **60 seconds**. The limit is calculated over a **60-second sliding window** looking back from the current time. While the limit can be configured to support higher thresholds, you must first contact your **Rootly Customer Success Manager** to make any adjustments. - The response to the API call will return 429 HTTP status code - Request Limit Exceeded and Rootly will not ingest the event. - Additional headers will be returned giving you information about the limit:   - **RateLimit-Limit** - The maximum number of requests that the consumer is permitted to make.   - **RateLimit-Remaining** - The number of requests remaining in the current rate limit window.   - **RateLimit-Reset** - The time at which the current rate limit window resets in UTC epoch seconds.  # Pagination - Pagination is supported for all endpoints that return a collection of items. - Pagination is controlled by the **page** query parameter  ## Example ```   curl --request GET \\ --header 'Content-Type: application/vnd.api+json' \\ --header 'Authorization: Bearer YOUR-TOKEN' \\ --url https://api.rootly.com/v1/incidents?page[number]=1&page[size]=10 ```    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import ApiClient


class IncidentRetrospectivesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def list_incident_post_mortems(self, **kwargs):  # noqa: E501
        """List incident retrospectives  # noqa: E501

        List incident retrospectives  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_incident_post_mortems(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str include:
        :param int page_number:
        :param int page_size:
        :param str filter_search:
        :param str filter_status:
        :param str filter_severity:
        :param str filter_type:
        :param int filter_user_id:
        :param str filter_environments:
        :param str filter_functionalities:
        :param str filter_services:
        :param str filter_teams:
        :param str filter_created_at_gt:
        :param str filter_created_at_gte:
        :param str filter_created_at_lt:
        :param str filter_created_at_lte:
        :param str filter_started_at_gt:
        :param str filter_started_at_gte:
        :param str filter_started_at_lt:
        :param str filter_started_at_lte:
        :param str filter_mitigated_at_gt:
        :param str filter_mitigated_at_gte:
        :param str filter_mitigated_at_lt:
        :param str filter_mitigated_at_lte:
        :param str filter_resolved_at_gt:
        :param str filter_resolved_at_gte:
        :param str filter_resolved_at_lt:
        :param str filter_resolved_at_lte:
        :param str sort:
        :return: IncidentPostMortemList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_incident_post_mortems_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_incident_post_mortems_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_incident_post_mortems_with_http_info(self, **kwargs):  # noqa: E501
        """List incident retrospectives  # noqa: E501

        List incident retrospectives  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_incident_post_mortems_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str include:
        :param int page_number:
        :param int page_size:
        :param str filter_search:
        :param str filter_status:
        :param str filter_severity:
        :param str filter_type:
        :param int filter_user_id:
        :param str filter_environments:
        :param str filter_functionalities:
        :param str filter_services:
        :param str filter_teams:
        :param str filter_created_at_gt:
        :param str filter_created_at_gte:
        :param str filter_created_at_lt:
        :param str filter_created_at_lte:
        :param str filter_started_at_gt:
        :param str filter_started_at_gte:
        :param str filter_started_at_lt:
        :param str filter_started_at_lte:
        :param str filter_mitigated_at_gt:
        :param str filter_mitigated_at_gte:
        :param str filter_mitigated_at_lt:
        :param str filter_mitigated_at_lte:
        :param str filter_resolved_at_gt:
        :param str filter_resolved_at_gte:
        :param str filter_resolved_at_lt:
        :param str filter_resolved_at_lte:
        :param str sort:
        :return: IncidentPostMortemList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['include', 'page_number', 'page_size', 'filter_search', 'filter_status', 'filter_severity', 'filter_type', 'filter_user_id', 'filter_environments', 'filter_functionalities', 'filter_services', 'filter_teams', 'filter_created_at_gt', 'filter_created_at_gte', 'filter_created_at_lt', 'filter_created_at_lte', 'filter_started_at_gt', 'filter_started_at_gte', 'filter_started_at_lt', 'filter_started_at_lte', 'filter_mitigated_at_gt', 'filter_mitigated_at_gte', 'filter_mitigated_at_lt', 'filter_mitigated_at_lte', 'filter_resolved_at_gt', 'filter_resolved_at_gte', 'filter_resolved_at_lt', 'filter_resolved_at_lte', 'sort']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_incident_post_mortems" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'include' in params:
            query_params.append(('include', params['include']))  # noqa: E501
        if 'page_number' in params:
            query_params.append(('page[number]', params['page_number']))  # noqa: E501
        if 'page_size' in params:
            query_params.append(('page[size]', params['page_size']))  # noqa: E501
        if 'filter_search' in params:
            query_params.append(('filter[search]', params['filter_search']))  # noqa: E501
        if 'filter_status' in params:
            query_params.append(('filter[status]', params['filter_status']))  # noqa: E501
        if 'filter_severity' in params:
            query_params.append(('filter[severity]', params['filter_severity']))  # noqa: E501
        if 'filter_type' in params:
            query_params.append(('filter[type]', params['filter_type']))  # noqa: E501
        if 'filter_user_id' in params:
            query_params.append(('filter[user_id]', params['filter_user_id']))  # noqa: E501
        if 'filter_environments' in params:
            query_params.append(('filter[environments]', params['filter_environments']))  # noqa: E501
        if 'filter_functionalities' in params:
            query_params.append(('filter[functionalities]', params['filter_functionalities']))  # noqa: E501
        if 'filter_services' in params:
            query_params.append(('filter[services]', params['filter_services']))  # noqa: E501
        if 'filter_teams' in params:
            query_params.append(('filter[teams]', params['filter_teams']))  # noqa: E501
        if 'filter_created_at_gt' in params:
            query_params.append(('filter[created_at][gt]', params['filter_created_at_gt']))  # noqa: E501
        if 'filter_created_at_gte' in params:
            query_params.append(('filter[created_at][gte]', params['filter_created_at_gte']))  # noqa: E501
        if 'filter_created_at_lt' in params:
            query_params.append(('filter[created_at][lt]', params['filter_created_at_lt']))  # noqa: E501
        if 'filter_created_at_lte' in params:
            query_params.append(('filter[created_at][lte]', params['filter_created_at_lte']))  # noqa: E501
        if 'filter_started_at_gt' in params:
            query_params.append(('filter[started_at][gt]', params['filter_started_at_gt']))  # noqa: E501
        if 'filter_started_at_gte' in params:
            query_params.append(('filter[started_at][gte]', params['filter_started_at_gte']))  # noqa: E501
        if 'filter_started_at_lt' in params:
            query_params.append(('filter[started_at][lt]', params['filter_started_at_lt']))  # noqa: E501
        if 'filter_started_at_lte' in params:
            query_params.append(('filter[started_at][lte]', params['filter_started_at_lte']))  # noqa: E501
        if 'filter_mitigated_at_gt' in params:
            query_params.append(('filter[mitigated_at][gt]', params['filter_mitigated_at_gt']))  # noqa: E501
        if 'filter_mitigated_at_gte' in params:
            query_params.append(('filter[mitigated_at][gte]', params['filter_mitigated_at_gte']))  # noqa: E501
        if 'filter_mitigated_at_lt' in params:
            query_params.append(('filter[mitigated_at][lt]', params['filter_mitigated_at_lt']))  # noqa: E501
        if 'filter_mitigated_at_lte' in params:
            query_params.append(('filter[mitigated_at][lte]', params['filter_mitigated_at_lte']))  # noqa: E501
        if 'filter_resolved_at_gt' in params:
            query_params.append(('filter[resolved_at][gt]', params['filter_resolved_at_gt']))  # noqa: E501
        if 'filter_resolved_at_gte' in params:
            query_params.append(('filter[resolved_at][gte]', params['filter_resolved_at_gte']))  # noqa: E501
        if 'filter_resolved_at_lt' in params:
            query_params.append(('filter[resolved_at][lt]', params['filter_resolved_at_lt']))  # noqa: E501
        if 'filter_resolved_at_lte' in params:
            query_params.append(('filter[resolved_at][lte]', params['filter_resolved_at_lte']))  # noqa: E501
        if 'sort' in params:
            query_params.append(('sort', params['sort']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/post_mortems', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IncidentPostMortemList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_incident_postmortem(self, id, **kwargs):  # noqa: E501
        """Retrieves a incident retrospective  # noqa: E501

        List incidents retrospectives  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_incident_postmortem(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: IncidentPostMortemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_incident_postmortem_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_incident_postmortem_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def list_incident_postmortem_with_http_info(self, id, **kwargs):  # noqa: E501
        """Retrieves a incident retrospective  # noqa: E501

        List incidents retrospectives  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_incident_postmortem_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: (required)
        :return: IncidentPostMortemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_incident_postmortem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `list_incident_postmortem`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/post_mortems/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IncidentPostMortemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_incident_postmortem(self, body, id, **kwargs):  # noqa: E501
        """Update a incident retrospective  # noqa: E501

        Update a specific incident retrospective by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_incident_postmortem(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateIncidentPostMortem body: (required)
        :param str id: (required)
        :return: IncidentPostMortemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_incident_postmortem_with_http_info(body, id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_incident_postmortem_with_http_info(body, id, **kwargs)  # noqa: E501
            return data

    def update_incident_postmortem_with_http_info(self, body, id, **kwargs):  # noqa: E501
        """Update a incident retrospective  # noqa: E501

        Update a specific incident retrospective by id  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_incident_postmortem_with_http_info(body, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param UpdateIncidentPostMortem body: (required)
        :param str id: (required)
        :return: IncidentPostMortemResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_incident_postmortem" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_incident_postmortem`")  # noqa: E501
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_incident_postmortem`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/vnd.api+json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/vnd.api+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer_auth']  # noqa: E501

        return self.api_client.call_api(
            '/v1/post_mortems/{id}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IncidentPostMortemResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
