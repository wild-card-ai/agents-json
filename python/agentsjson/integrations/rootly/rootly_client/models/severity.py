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

class Severity(object):
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
        'slug': 'str',
        'description': 'str',
        'severity': 'str',
        'color': 'str',
        'position': 'int',
        'notify_emails': 'list[str]',
        'slack_channels': 'list[NewEnvironmentDataAttributesSlackChannels]',
        'slack_aliases': 'list[NewEnvironmentDataAttributesSlackAliases]',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'name': 'name',
        'slug': 'slug',
        'description': 'description',
        'severity': 'severity',
        'color': 'color',
        'position': 'position',
        'notify_emails': 'notify_emails',
        'slack_channels': 'slack_channels',
        'slack_aliases': 'slack_aliases',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, name=None, slug=None, description=None, severity=None, color=None, position=None, notify_emails=None, slack_channels=None, slack_aliases=None, created_at=None, updated_at=None):  # noqa: E501
        """Severity - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._slug = None
        self._description = None
        self._severity = None
        self._color = None
        self._position = None
        self._notify_emails = None
        self._slack_channels = None
        self._slack_aliases = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.name = name
        if slug is not None:
            self.slug = slug
        if description is not None:
            self.description = description
        if severity is not None:
            self.severity = severity
        if color is not None:
            self.color = color
        if position is not None:
            self.position = position
        if notify_emails is not None:
            self.notify_emails = notify_emails
        if slack_channels is not None:
            self.slack_channels = slack_channels
        if slack_aliases is not None:
            self.slack_aliases = slack_aliases
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def name(self):
        """Gets the name of this Severity.  # noqa: E501

        The name of the severity  # noqa: E501

        :return: The name of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Severity.

        The name of the severity  # noqa: E501

        :param name: The name of this Severity.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Severity.  # noqa: E501

        The slug of the severity  # noqa: E501

        :return: The slug of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Severity.

        The slug of the severity  # noqa: E501

        :param slug: The slug of this Severity.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def description(self):
        """Gets the description of this Severity.  # noqa: E501

        The description of the severity  # noqa: E501

        :return: The description of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Severity.

        The description of the severity  # noqa: E501

        :param description: The description of this Severity.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def severity(self):
        """Gets the severity of this Severity.  # noqa: E501

        The severity of the severity  # noqa: E501

        :return: The severity of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this Severity.

        The severity of the severity  # noqa: E501

        :param severity: The severity of this Severity.  # noqa: E501
        :type: str
        """
        allowed_values = ["critical", "high", "medium", "low"]  # noqa: E501
        if severity not in allowed_values:
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def color(self):
        """Gets the color of this Severity.  # noqa: E501

        The hex color of the severity  # noqa: E501

        :return: The color of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this Severity.

        The hex color of the severity  # noqa: E501

        :param color: The color of this Severity.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def position(self):
        """Gets the position of this Severity.  # noqa: E501

        Position of the severity  # noqa: E501

        :return: The position of this Severity.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Severity.

        Position of the severity  # noqa: E501

        :param position: The position of this Severity.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def notify_emails(self):
        """Gets the notify_emails of this Severity.  # noqa: E501

        Emails to attach to the severity  # noqa: E501

        :return: The notify_emails of this Severity.  # noqa: E501
        :rtype: list[str]
        """
        return self._notify_emails

    @notify_emails.setter
    def notify_emails(self, notify_emails):
        """Sets the notify_emails of this Severity.

        Emails to attach to the severity  # noqa: E501

        :param notify_emails: The notify_emails of this Severity.  # noqa: E501
        :type: list[str]
        """

        self._notify_emails = notify_emails

    @property
    def slack_channels(self):
        """Gets the slack_channels of this Severity.  # noqa: E501

        Slack Channels associated with this severity  # noqa: E501

        :return: The slack_channels of this Severity.  # noqa: E501
        :rtype: list[NewEnvironmentDataAttributesSlackChannels]
        """
        return self._slack_channels

    @slack_channels.setter
    def slack_channels(self, slack_channels):
        """Sets the slack_channels of this Severity.

        Slack Channels associated with this severity  # noqa: E501

        :param slack_channels: The slack_channels of this Severity.  # noqa: E501
        :type: list[NewEnvironmentDataAttributesSlackChannels]
        """

        self._slack_channels = slack_channels

    @property
    def slack_aliases(self):
        """Gets the slack_aliases of this Severity.  # noqa: E501

        Slack Aliases associated with this severity  # noqa: E501

        :return: The slack_aliases of this Severity.  # noqa: E501
        :rtype: list[NewEnvironmentDataAttributesSlackAliases]
        """
        return self._slack_aliases

    @slack_aliases.setter
    def slack_aliases(self, slack_aliases):
        """Sets the slack_aliases of this Severity.

        Slack Aliases associated with this severity  # noqa: E501

        :param slack_aliases: The slack_aliases of this Severity.  # noqa: E501
        :type: list[NewEnvironmentDataAttributesSlackAliases]
        """

        self._slack_aliases = slack_aliases

    @property
    def created_at(self):
        """Gets the created_at of this Severity.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The created_at of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Severity.

        Date of creation  # noqa: E501

        :param created_at: The created_at of this Severity.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Severity.  # noqa: E501

        Date of last update  # noqa: E501

        :return: The updated_at of this Severity.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Severity.

        Date of last update  # noqa: E501

        :param updated_at: The updated_at of this Severity.  # noqa: E501
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
        if issubclass(Severity, dict):
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
        if not isinstance(other, Severity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
