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

class User(object):
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
        'email': 'str',
        'full_name': 'str',
        'full_name_with_team': 'str',
        'time_zone': 'str',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'email': 'email',
        'full_name': 'full_name',
        'full_name_with_team': 'full_name_with_team',
        'time_zone': 'time_zone',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, email=None, full_name=None, full_name_with_team=None, time_zone=None, created_at=None, updated_at=None):  # noqa: E501
        """User - a model defined in Swagger"""  # noqa: E501
        self._email = None
        self._full_name = None
        self._full_name_with_team = None
        self._time_zone = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.email = email
        if full_name is not None:
            self.full_name = full_name
        if full_name_with_team is not None:
            self.full_name_with_team = full_name_with_team
        if time_zone is not None:
            self.time_zone = time_zone
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def email(self):
        """Gets the email of this User.  # noqa: E501

        The email of the user  # noqa: E501

        :return: The email of this User.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this User.

        The email of the user  # noqa: E501

        :param email: The email of this User.  # noqa: E501
        :type: str
        """
        if email is None:
            raise ValueError("Invalid value for `email`, must not be `None`")  # noqa: E501

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this User.  # noqa: E501

        The full name of the user  # noqa: E501

        :return: The full_name of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this User.

        The full name of the user  # noqa: E501

        :param full_name: The full_name of this User.  # noqa: E501
        :type: str
        """

        self._full_name = full_name

    @property
    def full_name_with_team(self):
        """Gets the full_name_with_team of this User.  # noqa: E501

        The full name with team of the user  # noqa: E501

        :return: The full_name_with_team of this User.  # noqa: E501
        :rtype: str
        """
        return self._full_name_with_team

    @full_name_with_team.setter
    def full_name_with_team(self, full_name_with_team):
        """Sets the full_name_with_team of this User.

        The full name with team of the user  # noqa: E501

        :param full_name_with_team: The full_name_with_team of this User.  # noqa: E501
        :type: str
        """

        self._full_name_with_team = full_name_with_team

    @property
    def time_zone(self):
        """Gets the time_zone of this User.  # noqa: E501

        Configured time zone  # noqa: E501

        :return: The time_zone of this User.  # noqa: E501
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this User.

        Configured time zone  # noqa: E501

        :param time_zone: The time_zone of this User.  # noqa: E501
        :type: str
        """

        self._time_zone = time_zone

    @property
    def created_at(self):
        """Gets the created_at of this User.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The created_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this User.

        Date of creation  # noqa: E501

        :param created_at: The created_at of this User.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this User.  # noqa: E501

        Date of last update  # noqa: E501

        :return: The updated_at of this User.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this User.

        Date of last update  # noqa: E501

        :param updated_at: The updated_at of this User.  # noqa: E501
        :type: str
        """
        if updated_at is None:
            raise ValueError("Invalid value for `updated_at`, must not be `None`")  # noqa: E501

        self._updated_at = updated_at

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
        if issubclass(User, dict):
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
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
