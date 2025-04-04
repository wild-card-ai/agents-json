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

class CreateConfluencePageTaskParams(object):
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
        'integration': 'CreateConfluencePageTaskParamsIntegration',
        'space': 'AddActionItemTaskParamsPostToSlackChannels',
        'ancestor': 'AddActionItemTaskParamsPostToSlackChannels',
        'template': 'AddActionItemTaskParamsPostToSlackChannels',
        'title': 'str',
        'content': 'str',
        'post_mortem_template_id': 'str',
        'mark_post_mortem_as_published': 'bool'
    }

    attribute_map = {
        'task_type': 'task_type',
        'integration': 'integration',
        'space': 'space',
        'ancestor': 'ancestor',
        'template': 'template',
        'title': 'title',
        'content': 'content',
        'post_mortem_template_id': 'post_mortem_template_id',
        'mark_post_mortem_as_published': 'mark_post_mortem_as_published'
    }

    def __init__(self, task_type=None, integration=None, space=None, ancestor=None, template=None, title=None, content=None, post_mortem_template_id=None, mark_post_mortem_as_published=True):  # noqa: E501
        """CreateConfluencePageTaskParams - a model defined in Swagger"""  # noqa: E501
        self._task_type = None
        self._integration = None
        self._space = None
        self._ancestor = None
        self._template = None
        self._title = None
        self._content = None
        self._post_mortem_template_id = None
        self._mark_post_mortem_as_published = None
        self.discriminator = None
        if task_type is not None:
            self.task_type = task_type
        if integration is not None:
            self.integration = integration
        self.space = space
        if ancestor is not None:
            self.ancestor = ancestor
        if template is not None:
            self.template = template
        self.title = title
        if content is not None:
            self.content = content
        if post_mortem_template_id is not None:
            self.post_mortem_template_id = post_mortem_template_id
        if mark_post_mortem_as_published is not None:
            self.mark_post_mortem_as_published = mark_post_mortem_as_published

    @property
    def task_type(self):
        """Gets the task_type of this CreateConfluencePageTaskParams.  # noqa: E501


        :return: The task_type of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._task_type

    @task_type.setter
    def task_type(self, task_type):
        """Sets the task_type of this CreateConfluencePageTaskParams.


        :param task_type: The task_type of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["create_confluence_page"]  # noqa: E501
        if task_type not in allowed_values:
            raise ValueError(
                "Invalid value for `task_type` ({0}), must be one of {1}"  # noqa: E501
                .format(task_type, allowed_values)
            )

        self._task_type = task_type

    @property
    def integration(self):
        """Gets the integration of this CreateConfluencePageTaskParams.  # noqa: E501


        :return: The integration of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: CreateConfluencePageTaskParamsIntegration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this CreateConfluencePageTaskParams.


        :param integration: The integration of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: CreateConfluencePageTaskParamsIntegration
        """

        self._integration = integration

    @property
    def space(self):
        """Gets the space of this CreateConfluencePageTaskParams.  # noqa: E501


        :return: The space of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: AddActionItemTaskParamsPostToSlackChannels
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this CreateConfluencePageTaskParams.


        :param space: The space of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: AddActionItemTaskParamsPostToSlackChannels
        """
        if space is None:
            raise ValueError("Invalid value for `space`, must not be `None`")  # noqa: E501

        self._space = space

    @property
    def ancestor(self):
        """Gets the ancestor of this CreateConfluencePageTaskParams.  # noqa: E501


        :return: The ancestor of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: AddActionItemTaskParamsPostToSlackChannels
        """
        return self._ancestor

    @ancestor.setter
    def ancestor(self, ancestor):
        """Sets the ancestor of this CreateConfluencePageTaskParams.


        :param ancestor: The ancestor of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: AddActionItemTaskParamsPostToSlackChannels
        """

        self._ancestor = ancestor

    @property
    def template(self):
        """Gets the template of this CreateConfluencePageTaskParams.  # noqa: E501


        :return: The template of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: AddActionItemTaskParamsPostToSlackChannels
        """
        return self._template

    @template.setter
    def template(self, template):
        """Sets the template of this CreateConfluencePageTaskParams.


        :param template: The template of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: AddActionItemTaskParamsPostToSlackChannels
        """

        self._template = template

    @property
    def title(self):
        """Gets the title of this CreateConfluencePageTaskParams.  # noqa: E501

        The page title  # noqa: E501

        :return: The title of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CreateConfluencePageTaskParams.

        The page title  # noqa: E501

        :param title: The title of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def content(self):
        """Gets the content of this CreateConfluencePageTaskParams.  # noqa: E501

        The page content  # noqa: E501

        :return: The content of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this CreateConfluencePageTaskParams.

        The page content  # noqa: E501

        :param content: The content of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: str
        """

        self._content = content

    @property
    def post_mortem_template_id(self):
        """Gets the post_mortem_template_id of this CreateConfluencePageTaskParams.  # noqa: E501

        The Retrospective template to use  # noqa: E501

        :return: The post_mortem_template_id of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: str
        """
        return self._post_mortem_template_id

    @post_mortem_template_id.setter
    def post_mortem_template_id(self, post_mortem_template_id):
        """Sets the post_mortem_template_id of this CreateConfluencePageTaskParams.

        The Retrospective template to use  # noqa: E501

        :param post_mortem_template_id: The post_mortem_template_id of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: str
        """

        self._post_mortem_template_id = post_mortem_template_id

    @property
    def mark_post_mortem_as_published(self):
        """Gets the mark_post_mortem_as_published of this CreateConfluencePageTaskParams.  # noqa: E501


        :return: The mark_post_mortem_as_published of this CreateConfluencePageTaskParams.  # noqa: E501
        :rtype: bool
        """
        return self._mark_post_mortem_as_published

    @mark_post_mortem_as_published.setter
    def mark_post_mortem_as_published(self, mark_post_mortem_as_published):
        """Sets the mark_post_mortem_as_published of this CreateConfluencePageTaskParams.


        :param mark_post_mortem_as_published: The mark_post_mortem_as_published of this CreateConfluencePageTaskParams.  # noqa: E501
        :type: bool
        """

        self._mark_post_mortem_as_published = mark_post_mortem_as_published

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
        if issubclass(CreateConfluencePageTaskParams, dict):
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
        if not isinstance(other, CreateConfluencePageTaskParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
