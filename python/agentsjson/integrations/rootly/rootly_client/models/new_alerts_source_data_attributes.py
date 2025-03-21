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

class NewAlertsSourceDataAttributes(object):
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
        'source_type': 'str',
        'alert_urgency_id': 'str',
        'alert_template_attributes': 'NewAlertsSourceDataAttributesAlertTemplateAttributes',
        'alert_source_urgency_rules_attributes': 'list[NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributes]',
        'sourceable_attributes': 'NewAlertsSourceDataAttributesSourceableAttributes'
    }

    attribute_map = {
        'name': 'name',
        'source_type': 'source_type',
        'alert_urgency_id': 'alert_urgency_id',
        'alert_template_attributes': 'alert_template_attributes',
        'alert_source_urgency_rules_attributes': 'alert_source_urgency_rules_attributes',
        'sourceable_attributes': 'sourceable_attributes'
    }

    def __init__(self, name=None, source_type=None, alert_urgency_id=None, alert_template_attributes=None, alert_source_urgency_rules_attributes=None, sourceable_attributes=None):  # noqa: E501
        """NewAlertsSourceDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._source_type = None
        self._alert_urgency_id = None
        self._alert_template_attributes = None
        self._alert_source_urgency_rules_attributes = None
        self._sourceable_attributes = None
        self.discriminator = None
        self.name = name
        if source_type is not None:
            self.source_type = source_type
        if alert_urgency_id is not None:
            self.alert_urgency_id = alert_urgency_id
        if alert_template_attributes is not None:
            self.alert_template_attributes = alert_template_attributes
        if alert_source_urgency_rules_attributes is not None:
            self.alert_source_urgency_rules_attributes = alert_source_urgency_rules_attributes
        if sourceable_attributes is not None:
            self.sourceable_attributes = sourceable_attributes

    @property
    def name(self):
        """Gets the name of this NewAlertsSourceDataAttributes.  # noqa: E501

        The name of the alert source  # noqa: E501

        :return: The name of this NewAlertsSourceDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewAlertsSourceDataAttributes.

        The name of the alert source  # noqa: E501

        :param name: The name of this NewAlertsSourceDataAttributes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def source_type(self):
        """Gets the source_type of this NewAlertsSourceDataAttributes.  # noqa: E501

        The alert source type  # noqa: E501

        :return: The source_type of this NewAlertsSourceDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        """Sets the source_type of this NewAlertsSourceDataAttributes.

        The alert source type  # noqa: E501

        :param source_type: The source_type of this NewAlertsSourceDataAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["app_dynamics", "catchpoint", "datadog", "alertmanager", "google_cloud", "grafana", "sentry", "generic_webhook", "cloud_watch", "checkly", "azure", "new_relic", "splunk", "chronosphere", "app_optics", "bug_snag", "honeycomb", "monte_carlo", "nagios", "prtg"]  # noqa: E501
        if source_type not in allowed_values:
            raise ValueError(
                "Invalid value for `source_type` ({0}), must be one of {1}"  # noqa: E501
                .format(source_type, allowed_values)
            )

        self._source_type = source_type

    @property
    def alert_urgency_id(self):
        """Gets the alert_urgency_id of this NewAlertsSourceDataAttributes.  # noqa: E501

        ID for the default alert urgency assigned to this alert source  # noqa: E501

        :return: The alert_urgency_id of this NewAlertsSourceDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._alert_urgency_id

    @alert_urgency_id.setter
    def alert_urgency_id(self, alert_urgency_id):
        """Sets the alert_urgency_id of this NewAlertsSourceDataAttributes.

        ID for the default alert urgency assigned to this alert source  # noqa: E501

        :param alert_urgency_id: The alert_urgency_id of this NewAlertsSourceDataAttributes.  # noqa: E501
        :type: str
        """

        self._alert_urgency_id = alert_urgency_id

    @property
    def alert_template_attributes(self):
        """Gets the alert_template_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501


        :return: The alert_template_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501
        :rtype: NewAlertsSourceDataAttributesAlertTemplateAttributes
        """
        return self._alert_template_attributes

    @alert_template_attributes.setter
    def alert_template_attributes(self, alert_template_attributes):
        """Sets the alert_template_attributes of this NewAlertsSourceDataAttributes.


        :param alert_template_attributes: The alert_template_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501
        :type: NewAlertsSourceDataAttributesAlertTemplateAttributes
        """

        self._alert_template_attributes = alert_template_attributes

    @property
    def alert_source_urgency_rules_attributes(self):
        """Gets the alert_source_urgency_rules_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501

        List of rules that define the conditions under which the alert urgency will be set automatically based on the alert payload  # noqa: E501

        :return: The alert_source_urgency_rules_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501
        :rtype: list[NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributes]
        """
        return self._alert_source_urgency_rules_attributes

    @alert_source_urgency_rules_attributes.setter
    def alert_source_urgency_rules_attributes(self, alert_source_urgency_rules_attributes):
        """Sets the alert_source_urgency_rules_attributes of this NewAlertsSourceDataAttributes.

        List of rules that define the conditions under which the alert urgency will be set automatically based on the alert payload  # noqa: E501

        :param alert_source_urgency_rules_attributes: The alert_source_urgency_rules_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501
        :type: list[NewAlertsSourceDataAttributesAlertSourceUrgencyRulesAttributes]
        """

        self._alert_source_urgency_rules_attributes = alert_source_urgency_rules_attributes

    @property
    def sourceable_attributes(self):
        """Gets the sourceable_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501


        :return: The sourceable_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501
        :rtype: NewAlertsSourceDataAttributesSourceableAttributes
        """
        return self._sourceable_attributes

    @sourceable_attributes.setter
    def sourceable_attributes(self, sourceable_attributes):
        """Sets the sourceable_attributes of this NewAlertsSourceDataAttributes.


        :param sourceable_attributes: The sourceable_attributes of this NewAlertsSourceDataAttributes.  # noqa: E501
        :type: NewAlertsSourceDataAttributesSourceableAttributes
        """

        self._sourceable_attributes = sourceable_attributes

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
        if issubclass(NewAlertsSourceDataAttributes, dict):
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
        if not isinstance(other, NewAlertsSourceDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
