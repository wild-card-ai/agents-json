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

class NewAlertDataAttributes(object):
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
        'source': 'str',
        'status': 'str',
        'summary': 'str',
        'description': 'str',
        'service_ids': 'list[str]',
        'group_ids': 'list[str]',
        'environment_ids': 'list[str]',
        'started_at': 'datetime',
        'ended_at': 'datetime',
        'external_id': 'str',
        'external_url': 'str',
        'alert_urgency_id': 'str',
        'notification_target_type': 'str',
        'notification_target_id': 'str',
        'labels': 'list[NewAlertDataAttributesLabels]',
        'data': 'object'
    }

    attribute_map = {
        'source': 'source',
        'status': 'status',
        'summary': 'summary',
        'description': 'description',
        'service_ids': 'service_ids',
        'group_ids': 'group_ids',
        'environment_ids': 'environment_ids',
        'started_at': 'started_at',
        'ended_at': 'ended_at',
        'external_id': 'external_id',
        'external_url': 'external_url',
        'alert_urgency_id': 'alert_urgency_id',
        'notification_target_type': 'notification_target_type',
        'notification_target_id': 'notification_target_id',
        'labels': 'labels',
        'data': 'data'
    }

    def __init__(self, source=None, status=None, summary=None, description=None, service_ids=None, group_ids=None, environment_ids=None, started_at=None, ended_at=None, external_id=None, external_url=None, alert_urgency_id=None, notification_target_type=None, notification_target_id=None, labels=None, data=None):  # noqa: E501
        """NewAlertDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._status = None
        self._summary = None
        self._description = None
        self._service_ids = None
        self._group_ids = None
        self._environment_ids = None
        self._started_at = None
        self._ended_at = None
        self._external_id = None
        self._external_url = None
        self._alert_urgency_id = None
        self._notification_target_type = None
        self._notification_target_id = None
        self._labels = None
        self._data = None
        self.discriminator = None
        self.source = source
        if status is not None:
            self.status = status
        self.summary = summary
        if description is not None:
            self.description = description
        if service_ids is not None:
            self.service_ids = service_ids
        if group_ids is not None:
            self.group_ids = group_ids
        if environment_ids is not None:
            self.environment_ids = environment_ids
        if started_at is not None:
            self.started_at = started_at
        if ended_at is not None:
            self.ended_at = ended_at
        if external_id is not None:
            self.external_id = external_id
        if external_url is not None:
            self.external_url = external_url
        if alert_urgency_id is not None:
            self.alert_urgency_id = alert_urgency_id
        if notification_target_type is not None:
            self.notification_target_type = notification_target_type
        if notification_target_id is not None:
            self.notification_target_id = notification_target_id
        if labels is not None:
            self.labels = labels
        if data is not None:
            self.data = data

    @property
    def source(self):
        """Gets the source of this NewAlertDataAttributes.  # noqa: E501

        The source of the alert  # noqa: E501

        :return: The source of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this NewAlertDataAttributes.

        The source of the alert  # noqa: E501

        :param source: The source of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """
        if source is None:
            raise ValueError("Invalid value for `source`, must not be `None`")  # noqa: E501
        allowed_values = ["rootly", "manual", "web", "slack", "email", "workflow", "live_call_routing", "pagerduty", "opsgenie", "victorops", "pagertree", "datadog", "nobl9", "zendesk", "asana", "clickup", "sentry", "rollbar", "jira", "honeycomb", "service_now", "linear", "grafana", "alertmanager", "google_cloud", "generic_webhook", "cloud_watch", "azure", "splunk", "chronosphere", "app_optics", "bug_snag", "monte_carlo", "nagios", "prtg", "catchpoint", "app_dynamics"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def status(self):
        """Gets the status of this NewAlertDataAttributes.  # noqa: E501

        Only available for organizations with Rootly On-Call enabled. Can be one of open, triggered, acknowledged or resolved.  # noqa: E501

        :return: The status of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this NewAlertDataAttributes.

        Only available for organizations with Rootly On-Call enabled. Can be one of open, triggered, acknowledged or resolved.  # noqa: E501

        :param status: The status of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["open", "triggered", "acknowledged", "resolved"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def summary(self):
        """Gets the summary of this NewAlertDataAttributes.  # noqa: E501

        The summary of the alert  # noqa: E501

        :return: The summary of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this NewAlertDataAttributes.

        The summary of the alert  # noqa: E501

        :param summary: The summary of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this NewAlertDataAttributes.  # noqa: E501

        The description of the alert  # noqa: E501

        :return: The description of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewAlertDataAttributes.

        The description of the alert  # noqa: E501

        :param description: The description of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def service_ids(self):
        """Gets the service_ids of this NewAlertDataAttributes.  # noqa: E501

        The Service ID's to attach to the alert. If your organization has On-Call enabled and your notification target is a Service. This field will be automatically set for you.  # noqa: E501

        :return: The service_ids of this NewAlertDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._service_ids

    @service_ids.setter
    def service_ids(self, service_ids):
        """Sets the service_ids of this NewAlertDataAttributes.

        The Service ID's to attach to the alert. If your organization has On-Call enabled and your notification target is a Service. This field will be automatically set for you.  # noqa: E501

        :param service_ids: The service_ids of this NewAlertDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._service_ids = service_ids

    @property
    def group_ids(self):
        """Gets the group_ids of this NewAlertDataAttributes.  # noqa: E501

        The Group ID's to attach to the alert. If your organization has On-Call enabled and your notification target is a Group. This field will be automatically set for you.  # noqa: E501

        :return: The group_ids of this NewAlertDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._group_ids

    @group_ids.setter
    def group_ids(self, group_ids):
        """Sets the group_ids of this NewAlertDataAttributes.

        The Group ID's to attach to the alert. If your organization has On-Call enabled and your notification target is a Group. This field will be automatically set for you.  # noqa: E501

        :param group_ids: The group_ids of this NewAlertDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._group_ids = group_ids

    @property
    def environment_ids(self):
        """Gets the environment_ids of this NewAlertDataAttributes.  # noqa: E501

        The Environment ID's to attach to the alert  # noqa: E501

        :return: The environment_ids of this NewAlertDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._environment_ids

    @environment_ids.setter
    def environment_ids(self, environment_ids):
        """Sets the environment_ids of this NewAlertDataAttributes.

        The Environment ID's to attach to the alert  # noqa: E501

        :param environment_ids: The environment_ids of this NewAlertDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._environment_ids = environment_ids

    @property
    def started_at(self):
        """Gets the started_at of this NewAlertDataAttributes.  # noqa: E501

        Alert start datetime  # noqa: E501

        :return: The started_at of this NewAlertDataAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this NewAlertDataAttributes.

        Alert start datetime  # noqa: E501

        :param started_at: The started_at of this NewAlertDataAttributes.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def ended_at(self):
        """Gets the ended_at of this NewAlertDataAttributes.  # noqa: E501

        Alert end datetime  # noqa: E501

        :return: The ended_at of this NewAlertDataAttributes.  # noqa: E501
        :rtype: datetime
        """
        return self._ended_at

    @ended_at.setter
    def ended_at(self, ended_at):
        """Sets the ended_at of this NewAlertDataAttributes.

        Alert end datetime  # noqa: E501

        :param ended_at: The ended_at of this NewAlertDataAttributes.  # noqa: E501
        :type: datetime
        """

        self._ended_at = ended_at

    @property
    def external_id(self):
        """Gets the external_id of this NewAlertDataAttributes.  # noqa: E501

        External ID  # noqa: E501

        :return: The external_id of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this NewAlertDataAttributes.

        External ID  # noqa: E501

        :param external_id: The external_id of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def external_url(self):
        """Gets the external_url of this NewAlertDataAttributes.  # noqa: E501

        External Url  # noqa: E501

        :return: The external_url of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """Sets the external_url of this NewAlertDataAttributes.

        External Url  # noqa: E501

        :param external_url: The external_url of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """

        self._external_url = external_url

    @property
    def alert_urgency_id(self):
        """Gets the alert_urgency_id of this NewAlertDataAttributes.  # noqa: E501

        The ID of the alert urgency  # noqa: E501

        :return: The alert_urgency_id of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._alert_urgency_id

    @alert_urgency_id.setter
    def alert_urgency_id(self, alert_urgency_id):
        """Sets the alert_urgency_id of this NewAlertDataAttributes.

        The ID of the alert urgency  # noqa: E501

        :param alert_urgency_id: The alert_urgency_id of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """

        self._alert_urgency_id = alert_urgency_id

    @property
    def notification_target_type(self):
        """Gets the notification_target_type of this NewAlertDataAttributes.  # noqa: E501

        Only available for organizations with Rootly On-Call enabled. Can be one of Group, Service, EscalationPolicy, User.  # noqa: E501

        :return: The notification_target_type of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._notification_target_type

    @notification_target_type.setter
    def notification_target_type(self, notification_target_type):
        """Sets the notification_target_type of this NewAlertDataAttributes.

        Only available for organizations with Rootly On-Call enabled. Can be one of Group, Service, EscalationPolicy, User.  # noqa: E501

        :param notification_target_type: The notification_target_type of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["User", "Group", "EscalationPolicy", "Service"]  # noqa: E501
        if notification_target_type not in allowed_values:
            raise ValueError(
                "Invalid value for `notification_target_type` ({0}), must be one of {1}"  # noqa: E501
                .format(notification_target_type, allowed_values)
            )

        self._notification_target_type = notification_target_type

    @property
    def notification_target_id(self):
        """Gets the notification_target_id of this NewAlertDataAttributes.  # noqa: E501

        Only available for organizations with Rootly On-Call enabled. The _identifier_ of the notification target object.  # noqa: E501

        :return: The notification_target_id of this NewAlertDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._notification_target_id

    @notification_target_id.setter
    def notification_target_id(self, notification_target_id):
        """Sets the notification_target_id of this NewAlertDataAttributes.

        Only available for organizations with Rootly On-Call enabled. The _identifier_ of the notification target object.  # noqa: E501

        :param notification_target_id: The notification_target_id of this NewAlertDataAttributes.  # noqa: E501
        :type: str
        """

        self._notification_target_id = notification_target_id

    @property
    def labels(self):
        """Gets the labels of this NewAlertDataAttributes.  # noqa: E501


        :return: The labels of this NewAlertDataAttributes.  # noqa: E501
        :rtype: list[NewAlertDataAttributesLabels]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NewAlertDataAttributes.


        :param labels: The labels of this NewAlertDataAttributes.  # noqa: E501
        :type: list[NewAlertDataAttributesLabels]
        """

        self._labels = labels

    @property
    def data(self):
        """Gets the data of this NewAlertDataAttributes.  # noqa: E501

        Additional data  # noqa: E501

        :return: The data of this NewAlertDataAttributes.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this NewAlertDataAttributes.

        Additional data  # noqa: E501

        :param data: The data of this NewAlertDataAttributes.  # noqa: E501
        :type: object
        """

        self._data = data

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
        if issubclass(NewAlertDataAttributes, dict):
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
        if not isinstance(other, NewAlertDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
