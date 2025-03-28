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

class UpdateEscalationPolicyLevelDataAttributes(object):
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
        'delay': 'int',
        'position': 'int',
        'escalation_policy_path_id': 'str',
        'notification_target_params': 'list[UpdateEscalationPolicyLevelDataAttributesNotificationTargetParams]'
    }

    attribute_map = {
        'delay': 'delay',
        'position': 'position',
        'escalation_policy_path_id': 'escalation_policy_path_id',
        'notification_target_params': 'notification_target_params'
    }

    def __init__(self, delay=None, position=None, escalation_policy_path_id=None, notification_target_params=None):  # noqa: E501
        """UpdateEscalationPolicyLevelDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._delay = None
        self._position = None
        self._escalation_policy_path_id = None
        self._notification_target_params = None
        self.discriminator = None
        if delay is not None:
            self.delay = delay
        if position is not None:
            self.position = position
        if escalation_policy_path_id is not None:
            self.escalation_policy_path_id = escalation_policy_path_id
        if notification_target_params is not None:
            self.notification_target_params = notification_target_params

    @property
    def delay(self):
        """Gets the delay of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501

        Delay before notification targets will be alerted.  # noqa: E501

        :return: The delay of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :rtype: int
        """
        return self._delay

    @delay.setter
    def delay(self, delay):
        """Sets the delay of this UpdateEscalationPolicyLevelDataAttributes.

        Delay before notification targets will be alerted.  # noqa: E501

        :param delay: The delay of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :type: int
        """

        self._delay = delay

    @property
    def position(self):
        """Gets the position of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501

        Position of the escalation policy level  # noqa: E501

        :return: The position of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this UpdateEscalationPolicyLevelDataAttributes.

        Position of the escalation policy level  # noqa: E501

        :param position: The position of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def escalation_policy_path_id(self):
        """Gets the escalation_policy_path_id of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501

        The ID of the dynamic escalation policy path the level will belong to. If nothing is specified it will add the level to your default path.  # noqa: E501

        :return: The escalation_policy_path_id of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._escalation_policy_path_id

    @escalation_policy_path_id.setter
    def escalation_policy_path_id(self, escalation_policy_path_id):
        """Sets the escalation_policy_path_id of this UpdateEscalationPolicyLevelDataAttributes.

        The ID of the dynamic escalation policy path the level will belong to. If nothing is specified it will add the level to your default path.  # noqa: E501

        :param escalation_policy_path_id: The escalation_policy_path_id of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :type: str
        """

        self._escalation_policy_path_id = escalation_policy_path_id

    @property
    def notification_target_params(self):
        """Gets the notification_target_params of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501

        Escalation level's notification targets  # noqa: E501

        :return: The notification_target_params of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :rtype: list[UpdateEscalationPolicyLevelDataAttributesNotificationTargetParams]
        """
        return self._notification_target_params

    @notification_target_params.setter
    def notification_target_params(self, notification_target_params):
        """Sets the notification_target_params of this UpdateEscalationPolicyLevelDataAttributes.

        Escalation level's notification targets  # noqa: E501

        :param notification_target_params: The notification_target_params of this UpdateEscalationPolicyLevelDataAttributes.  # noqa: E501
        :type: list[UpdateEscalationPolicyLevelDataAttributesNotificationTargetParams]
        """

        self._notification_target_params = notification_target_params

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
        if issubclass(UpdateEscalationPolicyLevelDataAttributes, dict):
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
        if not isinstance(other, UpdateEscalationPolicyLevelDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
