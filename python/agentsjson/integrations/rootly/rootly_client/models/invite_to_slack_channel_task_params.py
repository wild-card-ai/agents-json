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

class InviteToSlackChannelTaskParams(object):
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
        'task_type': 'str',
        'channel': 'AddActionItemTaskParamsPostToSlackChannels',
        'slack_users': 'list[AddActionItemTaskParamsPostToSlackChannels]',
        'slack_user_groups': 'list[AddActionItemTaskParamsPostToSlackChannels]'
    }

    attribute_map = {
        'task_type': 'task_type',
        'channel': 'channel',
        'slack_users': 'slack_users',
        'slack_user_groups': 'slack_user_groups'
    }

    def __init__(self, task_type=None, channel=None, slack_users=None, slack_user_groups=None):  # noqa: E501
        """InviteToSlackChannelTaskParams - a model defined in Swagger"""  # noqa: E501
        self._task_type = None
        self._channel = None
        self._slack_users = None
        self._slack_user_groups = None
        self.discriminator = None
        if task_type is not None:
            self.task_type = task_type
        self.channel = channel
        if slack_users is not None:
            self.slack_users = slack_users
        if slack_user_groups is not None:
            self.slack_user_groups = slack_user_groups

    @property
    def task_type(self):
        """Gets the task_type of this InviteToSlackChannelTaskParams.  # noqa: E501


        :return: The task_type of this InviteToSlackChannelTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this InviteToSlackChannelTaskParams.


        :param task_type: The task_type of this InviteToSlackChannelTaskParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["invite_to_slack_channel"]  # noqa: E501
        if task_type not in allowed_values:
            raise ValueError(
                "Invalid value for `task_type` ({0}), must be one of {1}"  # noqa: E501
                .format(task_type, allowed_values)
            )

        self._task_type = task_type

    @property
    def channel(self):
        """Gets the channel of this InviteToSlackChannelTaskParams.  # noqa: E501


        :return: The channel of this InviteToSlackChannelTaskParams.  # noqa: E501
        :rtype: AddActionItemTaskParamsPostToSlackChannels
        """
        return self._channel

    @channel.setter
    def channel(self, channel):
        """Sets the channel of this InviteToSlackChannelTaskParams.


        :param channel: The channel of this InviteToSlackChannelTaskParams.  # noqa: E501
        :type: AddActionItemTaskParamsPostToSlackChannels
        """
        if channel is None:
            raise ValueError("Invalid value for `channel`, must not be `None`")  # noqa: E501

        self._channel = channel

    @property
    def slack_users(self):
        """Gets the slack_users of this InviteToSlackChannelTaskParams.  # noqa: E501


        :return: The slack_users of this InviteToSlackChannelTaskParams.  # noqa: E501
        :rtype: list[AddActionItemTaskParamsPostToSlackChannels]
        """
        return self._slack_users

    @slack_users.setter
    def slack_users(self, slack_users):
        """Sets the slack_users of this InviteToSlackChannelTaskParams.


        :param slack_users: The slack_users of this InviteToSlackChannelTaskParams.  # noqa: E501
        :type: list[AddActionItemTaskParamsPostToSlackChannels]
        """

        self._slack_users = slack_users

    @property
    def slack_user_groups(self):
        """Gets the slack_user_groups of this InviteToSlackChannelTaskParams.  # noqa: E501


        :return: The slack_user_groups of this InviteToSlackChannelTaskParams.  # noqa: E501
        :rtype: list[AddActionItemTaskParamsPostToSlackChannels]
        """
        return self._slack_user_groups

    @slack_user_groups.setter
    def slack_user_groups(self, slack_user_groups):
        """Sets the slack_user_groups of this InviteToSlackChannelTaskParams.


        :param slack_user_groups: The slack_user_groups of this InviteToSlackChannelTaskParams.  # noqa: E501
        :type: list[AddActionItemTaskParamsPostToSlackChannels]
        """

        self._slack_user_groups = slack_user_groups

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
        if issubclass(InviteToSlackChannelTaskParams, dict):
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
        if not isinstance(other, InviteToSlackChannelTaskParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
