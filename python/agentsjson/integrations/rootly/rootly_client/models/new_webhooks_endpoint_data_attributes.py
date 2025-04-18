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

class NewWebhooksEndpointDataAttributes(object):
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
        'url': 'str',
        'secret': 'str',
        'event_types': 'list[str]',
        'enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'url': 'url',
        'secret': 'secret',
        'event_types': 'event_types',
        'enabled': 'enabled'
    }

    def __init__(self, name=None, url=None, secret=None, event_types=None, enabled=None):  # noqa: E501
        """NewWebhooksEndpointDataAttributes - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._url = None
        self._secret = None
        self._event_types = None
        self._enabled = None
        self.discriminator = None
        self.name = name
        self.url = url
        if secret is not None:
            self.secret = secret
        if event_types is not None:
            self.event_types = event_types
        if enabled is not None:
            self.enabled = enabled

    @property
    def name(self):
        """Gets the name of this NewWebhooksEndpointDataAttributes.  # noqa: E501

        The name of the endpoint  # noqa: E501

        :return: The name of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NewWebhooksEndpointDataAttributes.

        The name of the endpoint  # noqa: E501

        :param name: The name of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def url(self):
        """Gets the url of this NewWebhooksEndpointDataAttributes.  # noqa: E501

        The URL of the endpoint.  # noqa: E501

        :return: The url of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this NewWebhooksEndpointDataAttributes.

        The URL of the endpoint.  # noqa: E501

        :param url: The url of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :type: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def secret(self):
        """Gets the secret of this NewWebhooksEndpointDataAttributes.  # noqa: E501

        The webhook signing secret used to verify webhook requests.  # noqa: E501

        :return: The secret of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :rtype: str
        """
        return self._secret

    @secret.setter
    def secret(self, secret):
        """Sets the secret of this NewWebhooksEndpointDataAttributes.

        The webhook signing secret used to verify webhook requests.  # noqa: E501

        :param secret: The secret of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :type: str
        """

        self._secret = secret

    @property
    def event_types(self):
        """Gets the event_types of this NewWebhooksEndpointDataAttributes.  # noqa: E501


        :return: The event_types of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :rtype: list[str]
        """
        return self._event_types

    @event_types.setter
    def event_types(self, event_types):
        """Sets the event_types of this NewWebhooksEndpointDataAttributes.


        :param event_types: The event_types of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["incident.created", "incident.updated", "incident.in_triage", "incident.mitigated", "incident.resolved", "incident.cancelled", "incident.deleted", "incident.scheduled.created", "incident.scheduled.updated", "incident.scheduled.in_progress", "incident.scheduled.completed", "incident.scheduled.deleted", "incident_post_mortem.created", "incident_post_mortem.updated", "incident_post_mortem.published", "incident_post_mortem.deleted", "alert.created", "pulse.created", "genius_workflow_run.queued", "genius_workflow_run.started", "genius_workflow_run.completed", "genius_workflow_run.failed", "genius_workflow_run.canceled"]  # noqa: E501
        if not set(event_types).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `event_types` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(event_types) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._event_types = event_types

    @property
    def enabled(self):
        """Gets the enabled of this NewWebhooksEndpointDataAttributes.  # noqa: E501


        :return: The enabled of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this NewWebhooksEndpointDataAttributes.


        :param enabled: The enabled of this NewWebhooksEndpointDataAttributes.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

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
        if issubclass(NewWebhooksEndpointDataAttributes, dict):
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
        if not isinstance(other, NewWebhooksEndpointDataAttributes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
