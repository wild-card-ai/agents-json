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

class NewFormFieldDataAttributes(object):
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
        'kind': 'str',
        'input_kind': 'str',
        'value_kind': 'str',
        'value_kind_catalog_id': 'str',
        'name': 'str',
        'description': 'str',
        'shown': 'list[str]',
        'required': 'list[str]',
        'show_on_incident_details': 'bool',
        'enabled': 'bool',
        'default_values': 'list[str]'
    }

    attribute_map = {
        'kind': 'kind',
        'input_kind': 'input_kind',
        'value_kind': 'value_kind',
        'value_kind_catalog_id': 'value_kind_catalog_id',
        'name': 'name',
        'description': 'description',
        'shown': 'shown',
        'required': 'required',
        'show_on_incident_details': 'show_on_incident_details',
        'enabled': 'enabled',
        'default_values': 'default_values'
    }

    def __init__(self, kind=None, input_kind=None, value_kind=None, value_kind_catalog_id=None, name=None, description=None, shown=None, required=None, show_on_incident_details=None, enabled=None, default_values=None):  # noqa: E501
        """NewFormFieldDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._kind = None
        self._input_kind = None
        self._value_kind = None
        self._value_kind_catalog_id = None
        self._name = None
        self._description = None
        self._shown = None
        self._required = None
        self._show_on_incident_details = None
        self._enabled = None
        self._default_values = None
        self.discriminator = None
        self.kind = kind
        if input_kind is not None:
            self.input_kind = input_kind
        if value_kind is not None:
            self.value_kind = value_kind
        if value_kind_catalog_id is not None:
            self.value_kind_catalog_id = value_kind_catalog_id
        self.name = name
        if description is not None:
            self.description = description
        if shown is not None:
            self.shown = shown
        if required is not None:
            self.required = required
        if show_on_incident_details is not None:
            self.show_on_incident_details = show_on_incident_details
        if enabled is not None:
            self.enabled = enabled
        if default_values is not None:
            self.default_values = default_values

    @property
    def kind(self):
        """Gets the kind of this NewFormFieldDataAttributes.  # noqa: E501

        The kind of the form field  # noqa: E501

        :return: The kind of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this NewFormFieldDataAttributes.

        The kind of the form field  # noqa: E501

        :param kind: The kind of this NewFormFieldDataAttributes.  # noqa: E501
        :type: str
        """
        if kind is None:
            raise ValueError("Invalid value for `kind`, must not be `None`")  # noqa: E501
        allowed_values = ["custom", "title", "summary", "mitigation_message", "resolution_message", "severity", "environments", "types", "services", "causes", "functionalities", "teams", "visibility", "mark_as_test", "mark_as_backfilled", "labels", "notify_emails", "trigger_manual_workflows", "show_ongoing_incidents", "attach_alerts", "mark_as_in_triage", "in_triage_at", "started_at", "detected_at", "acknowledged_at", "mitigated_at", "resolved_at", "closed_at", "manual_starting_datetime_field"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"  # noqa: E501
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def input_kind(self):
        """Gets the input_kind of this NewFormFieldDataAttributes.  # noqa: E501

        The input kind of the form field  # noqa: E501

        :return: The input_kind of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._input_kind

    @input_kind.setter
    def input_kind(self, input_kind):
        """Sets the input_kind of this NewFormFieldDataAttributes.

        The input kind of the form field  # noqa: E501

        :param input_kind: The input_kind of this NewFormFieldDataAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "textarea", "select", "multi_select", "date", "datetime", "number", "checkbox", "tags", "rich_text"]  # noqa: E501
        if input_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `input_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(input_kind, allowed_values)
            )

        self._input_kind = input_kind

    @property
    def value_kind(self):
        """Gets the value_kind of this NewFormFieldDataAttributes.  # noqa: E501

        The value kind of the form field  # noqa: E501

        :return: The value_kind of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._value_kind

    @value_kind.setter
    def value_kind(self, value_kind):
        """Sets the value_kind of this NewFormFieldDataAttributes.

        The value kind of the form field  # noqa: E501

        :param value_kind: The value_kind of this NewFormFieldDataAttributes.  # noqa: E501
        :type: str
        """
        allowed_values = ["inherit", "group", "service", "functionality", "user", "catalog_entity"]  # noqa: E501
        if value_kind not in allowed_values:
            raise ValueError(
                "Invalid value for `value_kind` ({0}), must be one of {1}"  # noqa: E501
                .format(value_kind, allowed_values)
            )

        self._value_kind = value_kind

    @property
    def value_kind_catalog_id(self):
        """Gets the value_kind_catalog_id of this NewFormFieldDataAttributes.  # noqa: E501

        The ID of the catalog used when value_kind is `catalog_entity`  # noqa: E501

        :return: The value_kind_catalog_id of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._value_kind_catalog_id

    @value_kind_catalog_id.setter
    def value_kind_catalog_id(self, value_kind_catalog_id):
        """Sets the value_kind_catalog_id of this NewFormFieldDataAttributes.

        The ID of the catalog used when value_kind is `catalog_entity`  # noqa: E501

        :param value_kind_catalog_id: The value_kind_catalog_id of this NewFormFieldDataAttributes.  # noqa: E501
        :type: str
        """

        self._value_kind_catalog_id = value_kind_catalog_id

    @property
    def name(self):
        """Gets the name of this NewFormFieldDataAttributes.  # noqa: E501

        The name of the form field  # noqa: E501

        :return: The name of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewFormFieldDataAttributes.

        The name of the form field  # noqa: E501

        :param name: The name of this NewFormFieldDataAttributes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this NewFormFieldDataAttributes.  # noqa: E501

        The description of the form field  # noqa: E501

        :return: The description of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewFormFieldDataAttributes.

        The description of the form field  # noqa: E501

        :param description: The description of this NewFormFieldDataAttributes.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def shown(self):
        """Gets the shown of this NewFormFieldDataAttributes.  # noqa: E501


        :return: The shown of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._shown

    @shown.setter
    def shown(self, shown):
        """Sets the shown of this NewFormFieldDataAttributes.


        :param shown: The shown of this NewFormFieldDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._shown = shown

    @property
    def required(self):
        """Gets the required of this NewFormFieldDataAttributes.  # noqa: E501


        :return: The required of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this NewFormFieldDataAttributes.


        :param required: The required of this NewFormFieldDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._required = required

    @property
    def show_on_incident_details(self):
        """Gets the show_on_incident_details of this NewFormFieldDataAttributes.  # noqa: E501

        Whether the form field is shown on the incident details panel  # noqa: E501

        :return: The show_on_incident_details of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._show_on_incident_details

    @show_on_incident_details.setter
    def show_on_incident_details(self, show_on_incident_details):
        """Sets the show_on_incident_details of this NewFormFieldDataAttributes.

        Whether the form field is shown on the incident details panel  # noqa: E501

        :param show_on_incident_details: The show_on_incident_details of this NewFormFieldDataAttributes.  # noqa: E501
        :type: bool
        """

        self._show_on_incident_details = show_on_incident_details

    @property
    def enabled(self):
        """Gets the enabled of this NewFormFieldDataAttributes.  # noqa: E501

        Whether the form field is enabled  # noqa: E501

        :return: The enabled of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NewFormFieldDataAttributes.

        Whether the form field is enabled  # noqa: E501

        :param enabled: The enabled of this NewFormFieldDataAttributes.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def default_values(self):
        """Gets the default_values of this NewFormFieldDataAttributes.  # noqa: E501


        :return: The default_values of this NewFormFieldDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._default_values

    @default_values.setter
    def default_values(self, default_values):
        """Sets the default_values of this NewFormFieldDataAttributes.


        :param default_values: The default_values of this NewFormFieldDataAttributes.  # noqa: E501
        :type: list[str]
        """

        self._default_values = default_values

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
        if issubclass(NewFormFieldDataAttributes, dict):
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
        if not isinstance(other, NewFormFieldDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
