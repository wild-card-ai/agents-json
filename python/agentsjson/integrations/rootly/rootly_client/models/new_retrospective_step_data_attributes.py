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

class NewRetrospectiveStepDataAttributes(object):
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
        'title': 'str',
        'description': 'str',
        'due_after_days': 'int',
        'incident_role_id': 'str',
        'position': 'int',
        'skippable': 'bool'
    }

    attribute_map = {
        'title': 'title',
        'description': 'description',
        'due_after_days': 'due_after_days',
        'incident_role_id': 'incident_role_id',
        'position': 'position',
        'skippable': 'skippable'
    }

    def __init__(self, title=None, description=None, due_after_days=None, incident_role_id=None, position=None, skippable=None):  # noqa: E501
        """NewRetrospectiveStepDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._title = None
        self._description = None
        self._due_after_days = None
        self._incident_role_id = None
        self._position = None
        self._skippable = None
        self.discriminator = None
        self.title = title
        if description is not None:
            self.description = description
        if due_after_days is not None:
            self.due_after_days = due_after_days
        if incident_role_id is not None:
            self.incident_role_id = incident_role_id
        if position is not None:
            self.position = position
        if skippable is not None:
            self.skippable = skippable

    @property
    def title(self):
        """Gets the title of this NewRetrospectiveStepDataAttributes.  # noqa: E501

        The name of the step  # noqa: E501

        :return: The title of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this NewRetrospectiveStepDataAttributes.

        The name of the step  # noqa: E501

        :param title: The title of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this NewRetrospectiveStepDataAttributes.  # noqa: E501

        The description of the step  # noqa: E501

        :return: The description of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewRetrospectiveStepDataAttributes.

        The description of the step  # noqa: E501

        :param description: The description of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def due_after_days(self):
        """Gets the due_after_days of this NewRetrospectiveStepDataAttributes.  # noqa: E501

        Due date in days  # noqa: E501

        :return: The due_after_days of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :rtype: int
        """
        return self._due_after_days

    @due_after_days.setter
    def due_after_days(self, due_after_days):
        """Sets the due_after_days of this NewRetrospectiveStepDataAttributes.

        Due date in days  # noqa: E501

        :param due_after_days: The due_after_days of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :type: int
        """

        self._due_after_days = due_after_days

    @property
    def incident_role_id(self):
        """Gets the incident_role_id of this NewRetrospectiveStepDataAttributes.  # noqa: E501

        Users assigned to the selected incident role will be the default owners for this step  # noqa: E501

        :return: The incident_role_id of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._incident_role_id

    @incident_role_id.setter
    def incident_role_id(self, incident_role_id):
        """Sets the incident_role_id of this NewRetrospectiveStepDataAttributes.

        Users assigned to the selected incident role will be the default owners for this step  # noqa: E501

        :param incident_role_id: The incident_role_id of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :type: str
        """

        self._incident_role_id = incident_role_id

    @property
    def position(self):
        """Gets the position of this NewRetrospectiveStepDataAttributes.  # noqa: E501

        Position of the step  # noqa: E501

        :return: The position of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this NewRetrospectiveStepDataAttributes.

        Position of the step  # noqa: E501

        :param position: The position of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def skippable(self):
        """Gets the skippable of this NewRetrospectiveStepDataAttributes.  # noqa: E501

        Is the step skippable?  # noqa: E501

        :return: The skippable of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._skippable

    @skippable.setter
    def skippable(self, skippable):
        """Sets the skippable of this NewRetrospectiveStepDataAttributes.

        Is the step skippable?  # noqa: E501

        :param skippable: The skippable of this NewRetrospectiveStepDataAttributes.  # noqa: E501
        :type: bool
        """

        self._skippable = skippable

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
        if issubclass(NewRetrospectiveStepDataAttributes, dict):
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
        if not isinstance(other, NewRetrospectiveStepDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
