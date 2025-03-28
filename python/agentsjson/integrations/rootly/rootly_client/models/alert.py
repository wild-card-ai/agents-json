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

class Alert(object):
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
        'summary': 'str',
        'description': 'str',
        'services': 'list[AllOfalertServicesItems]',
        'groups': 'list[AllOfalertGroupsItems]',
        'environments': 'list[AllOfalertEnvironmentsItems]',
        'external_id': 'str',
        'external_url': 'str',
        'alert_urgency_id': 'str',
        'labels': 'list[NewAlertDataAttributesLabels]',
        'data': 'object',
        'created_at': 'str',
        'updated_at': 'str'
    }

    attribute_map = {
        'source': 'source',
        'summary': 'summary',
        'description': 'description',
        'services': 'services',
        'groups': 'groups',
        'environments': 'environments',
        'external_id': 'external_id',
        'external_url': 'external_url',
        'alert_urgency_id': 'alert_urgency_id',
        'labels': 'labels',
        'data': 'data',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, source=None, summary=None, description=None, services=None, groups=None, environments=None, external_id=None, external_url=None, alert_urgency_id=None, labels=None, data=None, created_at=None, updated_at=None):  # noqa: E501
        """Alert - a model defined in Swagger"""  # noqa: E501
        self._source = None
        self._summary = None
        self._description = None
        self._services = None
        self._groups = None
        self._environments = None
        self._external_id = None
        self._external_url = None
        self._alert_urgency_id = None
        self._labels = None
        self._data = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        self.source = source
        self.summary = summary
        if description is not None:
            self.description = description
        if services is not None:
            self.services = services
        if groups is not None:
            self.groups = groups
        if environments is not None:
            self.environments = environments
        if external_id is not None:
            self.external_id = external_id
        if external_url is not None:
            self.external_url = external_url
        if alert_urgency_id is not None:
            self.alert_urgency_id = alert_urgency_id
        if labels is not None:
            self.labels = labels
        if data is not None:
            self.data = data
        self.created_at = created_at
        self.updated_at = updated_at

    @property
    def source(self):
        """Gets the source of this Alert.  # noqa: E501

        The source of the alert  # noqa: E501

        :return: The source of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Alert.

        The source of the alert  # noqa: E501

        :param source: The source of this Alert.  # noqa: E501
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
    def summary(self):
        """Gets the summary of this Alert.  # noqa: E501

        The summary of the alert  # noqa: E501

        :return: The summary of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """Sets the summary of this Alert.

        The summary of the alert  # noqa: E501

        :param summary: The summary of this Alert.  # noqa: E501
        :type: str
        """
        if summary is None:
            raise ValueError("Invalid value for `summary`, must not be `None`")  # noqa: E501

        self._summary = summary

    @property
    def description(self):
        """Gets the description of this Alert.  # noqa: E501

        The description of the alert  # noqa: E501

        :return: The description of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Alert.

        The description of the alert  # noqa: E501

        :param description: The description of this Alert.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def services(self):
        """Gets the services of this Alert.  # noqa: E501

        Services attached to the alert  # noqa: E501

        :return: The services of this Alert.  # noqa: E501
        :rtype: list[AllOfalertServicesItems]
        """
        return self._services

    @services.setter
    def services(self, services):
        """Sets the services of this Alert.

        Services attached to the alert  # noqa: E501

        :param services: The services of this Alert.  # noqa: E501
        :type: list[AllOfalertServicesItems]
        """

        self._services = services

    @property
    def groups(self):
        """Gets the groups of this Alert.  # noqa: E501

        Groups attached to the alert  # noqa: E501

        :return: The groups of this Alert.  # noqa: E501
        :rtype: list[AllOfalertGroupsItems]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Alert.

        Groups attached to the alert  # noqa: E501

        :param groups: The groups of this Alert.  # noqa: E501
        :type: list[AllOfalertGroupsItems]
        """

        self._groups = groups

    @property
    def environments(self):
        """Gets the environments of this Alert.  # noqa: E501

        Environments attached to the alert  # noqa: E501

        :return: The environments of this Alert.  # noqa: E501
        :rtype: list[AllOfalertEnvironmentsItems]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        """Sets the environments of this Alert.

        Environments attached to the alert  # noqa: E501

        :param environments: The environments of this Alert.  # noqa: E501
        :type: list[AllOfalertEnvironmentsItems]
        """

        self._environments = environments

    @property
    def external_id(self):
        """Gets the external_id of this Alert.  # noqa: E501

        External ID  # noqa: E501

        :return: The external_id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Alert.

        External ID  # noqa: E501

        :param external_id: The external_id of this Alert.  # noqa: E501
        :type: str
        """

        self._external_id = external_id

    @property
    def external_url(self):
        """Gets the external_url of this Alert.  # noqa: E501

        External Url  # noqa: E501

        :return: The external_url of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._external_url

    @external_url.setter
    def external_url(self, external_url):
        """Sets the external_url of this Alert.

        External Url  # noqa: E501

        :param external_url: The external_url of this Alert.  # noqa: E501
        :type: str
        """

        self._external_url = external_url

    @property
    def alert_urgency_id(self):
        """Gets the alert_urgency_id of this Alert.  # noqa: E501

        The ID of the alert urgency  # noqa: E501

        :return: The alert_urgency_id of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._alert_urgency_id

    @alert_urgency_id.setter
    def alert_urgency_id(self, alert_urgency_id):
        """Sets the alert_urgency_id of this Alert.

        The ID of the alert urgency  # noqa: E501

        :param alert_urgency_id: The alert_urgency_id of this Alert.  # noqa: E501
        :type: str
        """

        self._alert_urgency_id = alert_urgency_id

    @property
    def labels(self):
        """Gets the labels of this Alert.  # noqa: E501


        :return: The labels of this Alert.  # noqa: E501
        :rtype: list[NewAlertDataAttributesLabels]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Alert.


        :param labels: The labels of this Alert.  # noqa: E501
        :type: list[NewAlertDataAttributesLabels]
        """

        self._labels = labels

    @property
    def data(self):
        """Gets the data of this Alert.  # noqa: E501

        Additional data  # noqa: E501

        :return: The data of this Alert.  # noqa: E501
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this Alert.

        Additional data  # noqa: E501

        :param data: The data of this Alert.  # noqa: E501
        :type: object
        """

        self._data = data

    @property
    def created_at(self):
        """Gets the created_at of this Alert.  # noqa: E501

        Date of creation  # noqa: E501

        :return: The created_at of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Alert.

        Date of creation  # noqa: E501

        :param created_at: The created_at of this Alert.  # noqa: E501
        :type: str
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")  # noqa: E501

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Alert.  # noqa: E501

        Date of last update  # noqa: E501

        :return: The updated_at of this Alert.  # noqa: E501
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Alert.

        Date of last update  # noqa: E501

        :param updated_at: The updated_at of this Alert.  # noqa: E501
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
        if issubclass(Alert, dict):
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
        if not isinstance(other, Alert):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
