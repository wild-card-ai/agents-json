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

class IncidentRetrospectiveStep(object):
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
        'retrospective_step_id': 'str',
        'incident_id': 'str',
        'title': 'str',
        'description': 'str',
        'status': 'str',
        'kind': 'str',
        'due_date': 'str',
        'position': 'int',
        'skippable': 'bool',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'retrospective_step_id': 'retrospective_step_id',
        'incident_id': 'incident_id',
        'title': 'title',
        'description': 'description',
        'status': 'status',
        'kind': 'kind',
        'due_date': 'due_date',
        'position': 'position',
        'skippable': 'skippable',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, retrospective_step_id=None, incident_id=None, title=None, description=None, status=None, kind=None, due_date=None, position=None, skippable=None, created_at=None, updated_at=None):  # noqa: E501
        """IncidentRetrospectiveStep - a model defined in Swagger"""  # noqa: E501
        self._retrospective_step_id = None
        self._incident_id = None
        self._title = None
        self._description = None
        self._status = None
        self._kind = None
        self._due_date = None
        self._position = None
        self._skippable = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.retrospective_step_id = retrospective_step_id
        self.incident_id = incident_id
        self.title = title
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if kind is not None:
            self.kind = kind
        if due_date is not None:
            self.due_date = due_date
        if position is not None:
            self.position = position
        if skippable is not None:
            self.skippable = skippable
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def retrospective_step_id(self):
        """Gets the retrospective_step_id of this IncidentRetrospectiveStep.  # noqa: E501


        :return: The retrospective_step_id of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._retrospective_step_id

    @retrospective_step_id.setter
    def retrospective_step_id(self, retrospective_step_id):
        """Sets the retrospective_step_id of this IncidentRetrospectiveStep.


        :param retrospective_step_id: The retrospective_step_id of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """
        if retrospective_step_id is None:
            raise ValueError("Invalid value for `retrospective_step_id`, must not be `None`")  # noqa: E501

        self._retrospective_step_id = retrospective_step_id

    @property
    def incident_id(self):
        """Gets the incident_id of this IncidentRetrospectiveStep.  # noqa: E501


        :return: The incident_id of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._incident_id

    @incident_id.setter
    def incident_id(self, incident_id):
        """Sets the incident_id of this IncidentRetrospectiveStep.


        :param incident_id: The incident_id of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """
        if incident_id is None:
            raise ValueError("Invalid value for `incident_id`, must not be `None`")  # noqa: E501

        self._incident_id = incident_id

    @property
    def title(self):
        """Gets the title of this IncidentRetrospectiveStep.  # noqa: E501

        The name of the step  # noqa: E501

        :return: The title of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this IncidentRetrospectiveStep.

        The name of the step  # noqa: E501

        :param title: The title of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def description(self):
        """Gets the description of this IncidentRetrospectiveStep.  # noqa: E501

        The description of the step  # noqa: E501

        :return: The description of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this IncidentRetrospectiveStep.

        The description of the step  # noqa: E501

        :param description: The description of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this IncidentRetrospectiveStep.  # noqa: E501

        Status of the incident retrospective step  # noqa: E501

        :return: The status of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this IncidentRetrospectiveStep.

        Status of the incident retrospective step  # noqa: E501

        :param status: The status of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """
        allowed_values = ["todo", "in_progress", "completed", "skipped"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def kind(self):
        """Gets the kind of this IncidentRetrospectiveStep.  # noqa: E501

        Due date  # noqa: E501

        :return: The kind of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this IncidentRetrospectiveStep.

        Due date  # noqa: E501

        :param kind: The kind of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """

        self._kind = kind

    @property
    def due_date(self):
        """Gets the due_date of this IncidentRetrospectiveStep.  # noqa: E501

        Due date  # noqa: E501

        :return: The due_date of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this IncidentRetrospectiveStep.

        Due date  # noqa: E501

        :param due_date: The due_date of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """

        self._due_date = due_date

    @property
    def position(self):
        """Gets the position of this IncidentRetrospectiveStep.  # noqa: E501

        Position of the step  # noqa: E501

        :return: The position of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this IncidentRetrospectiveStep.

        Position of the step  # noqa: E501

        :param position: The position of this IncidentRetrospectiveStep.  # noqa: E501
        :type: int
        """

        self._position = position

    @property
    def skippable(self):
        """Gets the skippable of this IncidentRetrospectiveStep.  # noqa: E501

        Is the step skippable?  # noqa: E501

        :return: The skippable of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: bool
        """
        return self._skippable

    @skippable.setter
    def skippable(self, skippable):
        """Sets the skippable of this IncidentRetrospectiveStep.

        Is the step skippable?  # noqa: E501

        :param skippable: The skippable of this IncidentRetrospectiveStep.  # noqa: E501
        :type: bool
        """

        self._skippable = skippable

    @property
    def created_at(self):
        """Gets the created_at of this IncidentRetrospectiveStep.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The created_at of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this IncidentRetrospectiveStep.

        Date of creation  # noqa: E501

        :param created_at: The created_at of this IncidentRetrospectiveStep.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this IncidentRetrospectiveStep.  # noqa: E501

        Date of last update  # noqa: E501

        :return: The updated_at of this IncidentRetrospectiveStep.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this IncidentRetrospectiveStep.

        Date of last update  # noqa: E501

        :param updated_at: The updated_at of this IncidentRetrospectiveStep.  # noqa: E501
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
        if issubclass(IncidentRetrospectiveStep, dict):
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
        if not isinstance(other, IncidentRetrospectiveStep):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
