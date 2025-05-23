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

class UpdateClickupTaskTaskParams(object):
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
        'task_id': 'str',
        'title': 'str',
        'description': 'str',
        'tags': 'str',
        'priority': 'CreateJiraIssueTaskParamsPriority',
        'due_date': 'str',
        'custom_fields_mapping': 'str',
        'task_payload': 'str'
    }

    attribute_map = {
        'task_type': 'task_type',
        'task_id': 'task_id',
        'title': 'title',
        'description': 'description',
        'tags': 'tags',
        'priority': 'priority',
        'due_date': 'due_date',
        'custom_fields_mapping': 'custom_fields_mapping',
        'task_payload': 'task_payload'
    }

    def __init__(self, task_type=None, task_id=None, title=None, description=None, tags=None, priority=None, due_date=None, custom_fields_mapping=None, task_payload=None):  # noqa: E501
        """UpdateClickupTaskTaskParams - a model defined in Swagger"""  # noqa: E501
        self._task_type = None
        self._task_id = None
        self._title = None
        self._description = None
        self._tags = None
        self._priority = None
        self._due_date = None
        self._custom_fields_mapping = None
        self._task_payload = None
        self.discriminator = None
        if task_type is not None:
            self.task_type = task_type
        self.task_id = task_id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if tags is not None:
            self.tags = tags
        if priority is not None:
            self.priority = priority
        if due_date is not None:
            self.due_date = due_date
        if custom_fields_mapping is not None:
            self.custom_fields_mapping = custom_fields_mapping
        if task_payload is not None:
            self.task_payload = task_payload

    @property
    def task_type(self):
        """Gets the task_type of this UpdateClickupTaskTaskParams.  # noqa: E501


        :return: The task_type of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this UpdateClickupTaskTaskParams.


        :param task_type: The task_type of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["update_clickup_task"]  # noqa: E501
        if task_type not in allowed_values:
            raise ValueError(
                "Invalid value for `task_type` ({0}), must be one of {1}"  # noqa: E501
                .format(task_type, allowed_values)
            )

        self._task_type = task_type

    @property
    def task_id(self):
        """Gets the task_id of this UpdateClickupTaskTaskParams.  # noqa: E501

        The task id  # noqa: E501

        :return: The task_id of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._task_id

    @task_id.setter
    def task_id(self, task_id):
        """Sets the task_id of this UpdateClickupTaskTaskParams.

        The task id  # noqa: E501

        :param task_id: The task_id of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """
        if task_id is None:
            raise ValueError("Invalid value for `task_id`, must not be `None`")  # noqa: E501

        self._task_id = task_id

    @property
    def title(self):
        """Gets the title of this UpdateClickupTaskTaskParams.  # noqa: E501

        The task title  # noqa: E501

        :return: The title of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this UpdateClickupTaskTaskParams.

        The task title  # noqa: E501

        :param title: The title of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this UpdateClickupTaskTaskParams.  # noqa: E501

        The task description  # noqa: E501

        :return: The description of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateClickupTaskTaskParams.

        The task description  # noqa: E501

        :param description: The description of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def tags(self):
        """Gets the tags of this UpdateClickupTaskTaskParams.  # noqa: E501

        The task tags  # noqa: E501

        :return: The tags of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this UpdateClickupTaskTaskParams.

        The task tags  # noqa: E501

        :param tags: The tags of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """

        self._tags = tags

    @property
    def priority(self):
        """Gets the priority of this UpdateClickupTaskTaskParams.  # noqa: E501


        :return: The priority of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: CreateJiraIssueTaskParamsPriority
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this UpdateClickupTaskTaskParams.


        :param priority: The priority of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: CreateJiraIssueTaskParamsPriority
        """

        self._priority = priority

    @property
    def due_date(self):
        """Gets the due_date of this UpdateClickupTaskTaskParams.  # noqa: E501

        The due date  # noqa: E501

        :return: The due_date of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this UpdateClickupTaskTaskParams.

        The due date  # noqa: E501

        :param due_date: The due_date of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def custom_fields_mapping(self):
        """Gets the custom_fields_mapping of this UpdateClickupTaskTaskParams.  # noqa: E501

        Custom field mappings. Can contain liquid markup and need to be valid JSON  # noqa: E501

        :return: The custom_fields_mapping of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._custom_fields_mapping

    @custom_fields_mapping.setter
    def custom_fields_mapping(self, custom_fields_mapping):
        """Sets the custom_fields_mapping of this UpdateClickupTaskTaskParams.

        Custom field mappings. Can contain liquid markup and need to be valid JSON  # noqa: E501

        :param custom_fields_mapping: The custom_fields_mapping of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """

        self._custom_fields_mapping = custom_fields_mapping

    @property
    def task_payload(self):
        """Gets the task_payload of this UpdateClickupTaskTaskParams.  # noqa: E501

        Additional ClickUp task attributes. Will be merged into whatever was specified in this tasks current parameters. Can contain liquid markup and need to be valid JSON  # noqa: E501

        :return: The task_payload of this UpdateClickupTaskTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._task_payload

    @task_payload.setter
    def task_payload(self, task_payload):
        """Sets the task_payload of this UpdateClickupTaskTaskParams.

        Additional ClickUp task attributes. Will be merged into whatever was specified in this tasks current parameters. Can contain liquid markup and need to be valid JSON  # noqa: E501

        :param task_payload: The task_payload of this UpdateClickupTaskTaskParams.  # noqa: E501
        :type: str
        """

        self._task_payload = task_payload

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
        if issubclass(UpdateClickupTaskTaskParams, dict):
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
        if not isinstance(other, UpdateClickupTaskTaskParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
