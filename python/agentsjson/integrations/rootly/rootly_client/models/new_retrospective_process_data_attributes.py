# coding: utf-8

"""
    Rootly API v1

    # How to generate an API Key? - **Account** > **Manage API keys** > **Generate New API Key**  # JSON:API Specification Rootly is using **JSON:API** (https://jsonapi.org) specification: - JSON:API is a specification for how a client should request that resources be fetched or modified, and how a server should respond to those requests. - JSON:API is designed to minimize both the number of requests and the amount of data transmitted between clients and servers. This efficiency is achieved without compromising readability, flexibility, or discoverability. - JSON:API requires use of the JSON:API media type (**application/vnd.api+json**) for exchanging data.  # Authentication and Requests We use standard HTTP Authentication over HTTPS to authorize your requests. ```   curl --request GET \\ --header 'Content-Type: application/vnd.api+json' \\ --header 'Authorization: Bearer YOUR-TOKEN' \\ --url https://api.rootly.com/v1/incidents ```  <br/>  # Rate limiting - There is a default limit of approximately **3000** **GET** calls **per API key** every **60 seconds**. The limit is calculated over a **60-second sliding window** looking back from the current time. While the limit can be configured to support higher thresholds, you must first contact your **Rootly Customer Success Manager** to make any adjustments. - There is a default limit of approximately **3000** **PUT**, **POST**, **PATCH** or **DELETE** calls **per API key** every **60 seconds**. The limit is calculated over a **60-second sliding window** looking back from the current time. While the limit can be configured to support higher thresholds, you must first contact your **Rootly Customer Success Manager** to make any adjustments. - The response to the API call will return 429 HTTP status code - Request Limit Exceeded and Rootly will not ingest the event. - Additional headers will be returned giving you information about the limit:   - **RateLimit-Limit** - The maximum number of requests that the consumer is permitted to make.   - **RateLimit-Remaining** - The number of requests remaining in the current rate limit window.   - **RateLimit-Reset** - The time at which the current rate limit window resets in UTC epoch seconds.  # Pagination - Pagination is supported for all endpoints that return a collection of items. - Pagination is controlled by the **page** query parameter  ## Example ```   curl --request GET \\ --header 'Content-Type: application/vnd.api+json' \\ --header 'Authorization: Bearer YOUR-TOKEN' \\ --url https://api.rootly.com/v1/incidents?page[number]=1&page[size]=10 ```    # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class NewRetrospectiveProcessDataAttributes(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'copy_from': 'str',
        'description': 'str',
        'retrospective_process_matching_criteria': 'OneOfnewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteria'
    }

    attribute_map = {
        'name': 'name',
        'copy_from': 'copy_from',
        'description': 'description',
        'retrospective_process_matching_criteria': 'retrospective_process_matching_criteria'
    }

    def __init__(self, name=None, copy_from=None, description=None, retrospective_process_matching_criteria=None):  # noqa: E501
        """NewRetrospectiveProcessDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._copy_from = None
        self._description = None
        self._retrospective_process_matching_criteria = None
        self.discriminator = None
        self.name = name
        self.copy_from = copy_from
        if description is not None:
            self.description = description
        if retrospective_process_matching_criteria is not None:
            self.retrospective_process_matching_criteria = retrospective_process_matching_criteria

    @property
    def name(self):
        """Gets the name of this NewRetrospectiveProcessDataAttributes.  # noqa: E501

        The name of the retrospective process  # noqa: E501

        :return: The name of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewRetrospectiveProcessDataAttributes.

        The name of the retrospective process  # noqa: E501

        :param name: The name of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def copy_from(self):
        """Gets the copy_from of this NewRetrospectiveProcessDataAttributes.  # noqa: E501

        Retrospective process ID from which retrospective steps have to be copied. To use starter template for retrospective steps provide value: 'starter_template'  # noqa: E501

        :return: The copy_from of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._copy_from

    @copy_from.setter
    def copy_from(self, copy_from):
        """Sets the copy_from of this NewRetrospectiveProcessDataAttributes.

        Retrospective process ID from which retrospective steps have to be copied. To use starter template for retrospective steps provide value: 'starter_template'  # noqa: E501

        :param copy_from: The copy_from of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :type: str
        """
        if copy_from is None:
            raise ValueError("Invalid value for `copy_from`, must not be `None`")  # noqa: E501

        self._copy_from = copy_from

    @property
    def description(self):
        """Gets the description of this NewRetrospectiveProcessDataAttributes.  # noqa: E501

        The description of the retrospective process  # noqa: E501

        :return: The description of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewRetrospectiveProcessDataAttributes.

        The description of the retrospective process  # noqa: E501

        :param description: The description of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def retrospective_process_matching_criteria(self):
        """Gets the retrospective_process_matching_criteria of this NewRetrospectiveProcessDataAttributes.  # noqa: E501


        :return: The retrospective_process_matching_criteria of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :rtype: OneOfnewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteria
        """
        return self._retrospective_process_matching_criteria

    @retrospective_process_matching_criteria.setter
    def retrospective_process_matching_criteria(self, retrospective_process_matching_criteria):
        """Sets the retrospective_process_matching_criteria of this NewRetrospectiveProcessDataAttributes.


        :param retrospective_process_matching_criteria: The retrospective_process_matching_criteria of this NewRetrospectiveProcessDataAttributes.  # noqa: E501
        :type: OneOfnewRetrospectiveProcessDataAttributesRetrospectiveProcessMatchingCriteria
        """

        self._retrospective_process_matching_criteria = retrospective_process_matching_criteria

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(NewRetrospectiveProcessDataAttributes, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, NewRetrospectiveProcessDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
