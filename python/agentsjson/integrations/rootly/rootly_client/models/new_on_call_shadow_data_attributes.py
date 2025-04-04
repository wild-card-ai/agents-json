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

class NewOnCallShadowDataAttributes(object):
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
        'shadowable_type': 'str',
        'shadowable_id': 'str',
        'shadow_user_id': 'int',
        'starts_at': 'datetime',
        'ends_at': 'datetime'
    }

    attribute_map = {
        'shadowable_type': 'shadowable_type',
        'shadowable_id': 'shadowable_id',
        'shadow_user_id': 'shadow_user_id',
        'starts_at': 'starts_at',
        'ends_at': 'ends_at'
    }

    def __init__(self, shadowable_type=None, shadowable_id=None, shadow_user_id=None, starts_at=None, ends_at=None):  # noqa: E501
        """NewOnCallShadowDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._shadowable_type = None
        self._shadowable_id = None
        self._shadow_user_id = None
        self._starts_at = None
        self._ends_at = None
        self.discriminator = None
        self.shadowable_type = shadowable_type
        self.shadowable_id = shadowable_id
        self.shadow_user_id = shadow_user_id
        self.starts_at = starts_at
        self.ends_at = ends_at

    @property
    def shadowable_type(self):
        """Gets the shadowable_type of this NewOnCallShadowDataAttributes.  # noqa: E501


        :return: The shadowable_type of this NewOnCallShadowDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._shadowable_type

    @shadowable_type.setter
    def shadowable_type(self, shadowable_type):
        """Sets the shadowable_type of this NewOnCallShadowDataAttributes.


        :param shadowable_type: The shadowable_type of this NewOnCallShadowDataAttributes.  # noqa: E501
        :type: str
        """
        if shadowable_type is None:
            raise ValueError("Invalid value for `shadowable_type`, must not be `None`")  # noqa: E501
        allowed_values = ["User", "Schedule"]  # noqa: E501
        if shadowable_type not in allowed_values:
            raise ValueError(
                "Invalid value for `shadowable_type` ({0}), must be one of {1}"  # noqa: E501
                .format(shadowable_type, allowed_values)
            )

        self._shadowable_type = shadowable_type

    @property
    def shadowable_id(self):
        """Gets the shadowable_id of this NewOnCallShadowDataAttributes.  # noqa: E501

        ID of schedule or user the shadow user is shadowing  # noqa: E501

        :return: The shadowable_id of this NewOnCallShadowDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._shadowable_id

    @shadowable_id.setter
    def shadowable_id(self, shadowable_id):
        """Sets the shadowable_id of this NewOnCallShadowDataAttributes.

        ID of schedule or user the shadow user is shadowing  # noqa: E501

        :param shadowable_id: The shadowable_id of this NewOnCallShadowDataAttributes.  # noqa: E501
        :type: str
        """
        if shadowable_id is None:
            raise ValueError("Invalid value for `shadowable_id`, must not be `None`")  # noqa: E501

        self._shadowable_id = shadowable_id

    @property
    def shadow_user_id(self):
        """Gets the shadow_user_id of this NewOnCallShadowDataAttributes.  # noqa: E501

        Which user the shadow shift belongs to.  # noqa: E501

        :return: The shadow_user_id of this NewOnCallShadowDataAttributes.  # noqa: E501
        :rtype: int
        """
        return self._shadow_user_id

    @shadow_user_id.setter
    def shadow_user_id(self, shadow_user_id):
        """Sets the shadow_user_id of this NewOnCallShadowDataAttributes.

        Which user the shadow shift belongs to.  # noqa: E501

        :param shadow_user_id: The shadow_user_id of this NewOnCallShadowDataAttributes.  # noqa: E501
        :type: int
        """
        if shadow_user_id is None:
            raise ValueError("Invalid value for `shadow_user_id`, must not be `None`")  # noqa: E501

        self._shadow_user_id = shadow_user_id

    @property
    def starts_at(self):
        """Gets the starts_at of this NewOnCallShadowDataAttributes.  # noqa: E501

        Start datetime of shadow shift  # noqa: E501

        :return: The starts_at of this NewOnCallShadowDataAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this NewOnCallShadowDataAttributes.

        Start datetime of shadow shift  # noqa: E501

        :param starts_at: The starts_at of this NewOnCallShadowDataAttributes.  # noqa: E501
        :type: datetime
        """
        if starts_at is None:
            raise ValueError("Invalid value for `starts_at`, must not be `None`")  # noqa: E501

        self._starts_at = starts_at

    @property
    def ends_at(self):
        """Gets the ends_at of this NewOnCallShadowDataAttributes.  # noqa: E501

        End datetime for shadow shift  # noqa: E501

        :return: The ends_at of this NewOnCallShadowDataAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this NewOnCallShadowDataAttributes.

        End datetime for shadow shift  # noqa: E501

        :param ends_at: The ends_at of this NewOnCallShadowDataAttributes.  # noqa: E501
        :type: datetime
        """
        if ends_at is None:
            raise ValueError("Invalid value for `ends_at`, must not be `None`")  # noqa: E501

        self._ends_at = ends_at

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
        if issubclass(NewOnCallShadowDataAttributes, dict):
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
        if not isinstance(other, NewOnCallShadowDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
