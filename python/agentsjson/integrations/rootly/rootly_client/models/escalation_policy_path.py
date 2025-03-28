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

class EscalationPolicyPath(object):
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
        'default': 'bool',
        'notification_type': 'str',
        'escalation_policy_id': 'str',
        'match_mode': 'str',
        'position': 'int',
        'repeat': 'bool',
        'repeat_count': 'int',
        'created_at': 'str',
        'updated_at': 'str',
        'rules': 'list[AnyOfescalationPolicyPathRulesItems]'
    }

    attribute_map = {
        'name': 'name',
        'default': 'default',
        'notification_type': 'notification_type',
        'escalation_policy_id': 'escalation_policy_id',
        'match_mode': 'match_mode',
        'position': 'position',
        'repeat': 'repeat',
        'repeat_count': 'repeat_count',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'rules': 'rules'
    }

    def __init__(self, name=None, default=None, notification_type=None, escalation_policy_id=None, match_mode=None, position=None, repeat=None, repeat_count=None, created_at=None, updated_at=None, rules=None):  # noqa: E501
        """EscalationPolicyPath - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._default = None
        self._notification_type = None
        self._escalation_policy_id = None
        self._match_mode = None
        self._position = None
        self._repeat = None
        self._repeat_count = None
        self._created_at = None
        self._updated_at = None
        self._rules = None
        self.discriminator = None
        self.name = name
        self.default = default
        self.notification_type = notification_type
        self.escalation_policy_id = escalation_policy_id
        if match_mode is not None:
            self.match_mode = match_mode
        if position is not None:
            self.position = position
        self.repeat = repeat
        self.repeat_count = repeat_count
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if rules is not None:
            self.rules = rules

    @property
    def name(self):
        """Gets the name of this EscalationPolicyPath.  # noqa: E501

        The name of the escalation path  # noqa: E501

        :return: The name of this EscalationPolicyPath.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EscalationPolicyPath.

        The name of the escalation path  # noqa: E501

        :param name: The name of this EscalationPolicyPath.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def default(self):
        """Gets the default of this EscalationPolicyPath.  # noqa: E501

        Whether this escalation path is the default path  # noqa: E501

        :return: The default of this EscalationPolicyPath.  # noqa: E501
        :rtype: bool
        """
        return self._default

    @default.setter
    def default(self, default):
        """Sets the default of this EscalationPolicyPath.

        Whether this escalation path is the default path  # noqa: E501

        :param default: The default of this EscalationPolicyPath.  # noqa: E501
        :type: bool
        """
        if default is None:
            raise ValueError("Invalid value for `default`, must not be `None`")  # noqa: E501

        self._default = default

    @property
    def notification_type(self):
        """Gets the notification_type of this EscalationPolicyPath.  # noqa: E501

        Notification rule type  # noqa: E501

        :return: The notification_type of this EscalationPolicyPath.  # noqa: E501
        :rtype: str
        """
        return self._notification_type

    @notification_type.setter
    def notification_type(self, notification_type):
        """Sets the notification_type of this EscalationPolicyPath.

        Notification rule type  # noqa: E501

        :param notification_type: The notification_type of this EscalationPolicyPath.  # noqa: E501
        :type: str
        """
        if notification_type is None:
            raise ValueError("Invalid value for `notification_type`, must not be `None`")  # noqa: E501

        self._notification_type = notification_type

    @property
    def escalation_policy_id(self):
        """Gets the escalation_policy_id of this EscalationPolicyPath.  # noqa: E501

        The ID of the escalation policy  # noqa: E501

        :return: The escalation_policy_id of this EscalationPolicyPath.  # noqa: E501
        :rtype: str
        """
        return self._escalation_policy_id

    @escalation_policy_id.setter
    def escalation_policy_id(self, escalation_policy_id):
        """Sets the escalation_policy_id of this EscalationPolicyPath.

        The ID of the escalation policy  # noqa: E501

        :param escalation_policy_id: The escalation_policy_id of this EscalationPolicyPath.  # noqa: E501
        :type: str
        """
        if escalation_policy_id is None:
            raise ValueError("Invalid value for `escalation_policy_id`, must not be `None`")  # noqa: E501

        self._escalation_policy_id = escalation_policy_id

    @property
    def match_mode(self):
        """Gets the match_mode of this EscalationPolicyPath.  # noqa: E501

        How path rules are matched.  # noqa: E501

        :return: The match_mode of this EscalationPolicyPath.  # noqa: E501
        :rtype: str
        """
        return self._match_mode

    @match_mode.setter
    def match_mode(self, match_mode):
        """Sets the match_mode of this EscalationPolicyPath.

        How path rules are matched.  # noqa: E501

        :param match_mode: The match_mode of this EscalationPolicyPath.  # noqa: E501
        :type: str
        """
        allowed_values = ["match-all-rules", "match-any-rule"]  # noqa: E501
        if match_mode not in allowed_values:
            raise ValueError(
                "Invalid value for `match_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(match_mode, allowed_values)
            )

        self._match_mode = match_mode

    @property
    def position(self):
        """Gets the position of this EscalationPolicyPath.  # noqa: E501

        The position of this path in the paths for this EP.  # noqa: E501

        :return: The position of this EscalationPolicyPath.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this EscalationPolicyPath.

        The position of this path in the paths for this EP.  # noqa: E501

        :param position: The position of this EscalationPolicyPath.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def repeat(self):
        """Gets the repeat of this EscalationPolicyPath.  # noqa: E501

        Whether this path should be repeated until someone acknowledges the alert  # noqa: E501

        :return: The repeat of this EscalationPolicyPath.  # noqa: E501
        :rtype: bool
        """
        return self._repeat

    @repeat.setter
    def repeat(self, repeat):
        """Sets the repeat of this EscalationPolicyPath.

        Whether this path should be repeated until someone acknowledges the alert  # noqa: E501

        :param repeat: The repeat of this EscalationPolicyPath.  # noqa: E501
        :type: bool
        """
        if repeat is None:
            raise ValueError("Invalid value for `repeat`, must not be `None`")  # noqa: E501

        self._repeat = repeat

    @property
    def repeat_count(self):
        """Gets the repeat_count of this EscalationPolicyPath.  # noqa: E501

        The number of times this path will be executed until someone acknowledges the alert  # noqa: E501

        :return: The repeat_count of this EscalationPolicyPath.  # noqa: E501
        :rtype: int
        """
        return self._repeat_count

    @repeat_count.setter
    def repeat_count(self, repeat_count):
        """Sets the repeat_count of this EscalationPolicyPath.

        The number of times this path will be executed until someone acknowledges the alert  # noqa: E501

        :param repeat_count: The repeat_count of this EscalationPolicyPath.  # noqa: E501
        :type: int
        """
        if repeat_count is None:
            raise ValueError("Invalid value for `repeat_count`, must not be `None`")  # noqa: E501

        self._repeat_count = repeat_count

    @property
    def created_at(self):
        """Gets the created_at of this EscalationPolicyPath.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The created_at of this EscalationPolicyPath.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EscalationPolicyPath.

        Date of creation  # noqa: E501

        :param created_at: The created_at of this EscalationPolicyPath.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EscalationPolicyPath.  # noqa: E501

        Date of last update  # noqa: E501

        :return: The updated_at of this EscalationPolicyPath.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EscalationPolicyPath.

        Date of last update  # noqa: E501

        :param updated_at: The updated_at of this EscalationPolicyPath.  # noqa: E501
        :type: str
        """

        self._updated_at = updated_at

    @property
    def rules(self):
        """Gets the rules of this EscalationPolicyPath.  # noqa: E501

        Escalation path rules  # noqa: E501

        :return: The rules of this EscalationPolicyPath.  # noqa: E501
        :rtype: list[AnyOfescalationPolicyPathRulesItems]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        """Sets the rules of this EscalationPolicyPath.

        Escalation path rules  # noqa: E501

        :param rules: The rules of this EscalationPolicyPath.  # noqa: E501
        :type: list[AnyOfescalationPolicyPathRulesItems]
        """

        self._rules = rules

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
        if issubclass(EscalationPolicyPath, dict):
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
        if not isinstance(other, EscalationPolicyPath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
