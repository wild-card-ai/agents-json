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

class NewDashboardPanelDataAttributesParams(object):
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
        'display': 'str',
        'description': 'str',
        'table_fields': 'list[str]',
        'legend': 'NewDashboardPanelDataAttributesParamsLegend',
        'datalabels': 'NewDashboardPanelDataAttributesParamsDatalabels',
        'datasets': 'list[NewDashboardPanelDataAttributesParamsDatasets]'
    }

    attribute_map = {
        'display': 'display',
        'description': 'description',
        'table_fields': 'table_fields',
        'legend': 'legend',
        'datalabels': 'datalabels',
        'datasets': 'datasets'
    }

    def __init__(self, display=None, description=None, table_fields=None, legend=None, datalabels=None, datasets=None):  # noqa: E501
        """NewDashboardPanelDataAttributesParams - a model defined in Swagger"""  # noqa: E501
        self._display = None
        self._description = None
        self._table_fields = None
        self._legend = None
        self._datalabels = None
        self._datasets = None
        self.discriminator = None
        if display is not None:
            self.display = display
        if description is not None:
            self.description = description
        if table_fields is not None:
            self.table_fields = table_fields
        if legend is not None:
            self.legend = legend
        if datalabels is not None:
            self.datalabels = datalabels
        if datasets is not None:
            self.datasets = datasets

    @property
    def display(self):
        """Gets the display of this NewDashboardPanelDataAttributesParams.  # noqa: E501


        :return: The display of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """Sets the display of this NewDashboardPanelDataAttributesParams.


        :param display: The display of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :type: str
        """
        allowed_values = ["line_chart", "line_stepped_chart", "column_chart", "stacked_column_chart", "pie_chart", "table", "aggregate_value"]  # noqa: E501
        if display not in allowed_values:
            raise ValueError(
                "Invalid value for `display` ({0}), must be one of {1}"  # noqa: E501
                .format(display, allowed_values)
            )

        self._display = display

    @property
    def description(self):
        """Gets the description of this NewDashboardPanelDataAttributesParams.  # noqa: E501


        :return: The description of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this NewDashboardPanelDataAttributesParams.


        :param description: The description of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def table_fields(self):
        """Gets the table_fields of this NewDashboardPanelDataAttributesParams.  # noqa: E501


        :return: The table_fields of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :rtype: list[str]
        """
        return self._table_fields

    @table_fields.setter
    def table_fields(self, table_fields):
        """Sets the table_fields of this NewDashboardPanelDataAttributesParams.


        :param table_fields: The table_fields of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :type: list[str]
        """

        self._table_fields = table_fields

    @property
    def legend(self):
        """Gets the legend of this NewDashboardPanelDataAttributesParams.  # noqa: E501


        :return: The legend of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :rtype: NewDashboardPanelDataAttributesParamsLegend
        """
        return self._legend

    @legend.setter
    def legend(self, legend):
        """Sets the legend of this NewDashboardPanelDataAttributesParams.


        :param legend: The legend of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :type: NewDashboardPanelDataAttributesParamsLegend
        """

        self._legend = legend

    @property
    def datalabels(self):
        """Gets the datalabels of this NewDashboardPanelDataAttributesParams.  # noqa: E501


        :return: The datalabels of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :rtype: NewDashboardPanelDataAttributesParamsDatalabels
        """
        return self._datalabels

    @datalabels.setter
    def datalabels(self, datalabels):
        """Sets the datalabels of this NewDashboardPanelDataAttributesParams.


        :param datalabels: The datalabels of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :type: NewDashboardPanelDataAttributesParamsDatalabels
        """

        self._datalabels = datalabels

    @property
    def datasets(self):
        """Gets the datasets of this NewDashboardPanelDataAttributesParams.  # noqa: E501


        :return: The datasets of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :rtype: list[NewDashboardPanelDataAttributesParamsDatasets]
        """
        return self._datasets

    @datasets.setter
    def datasets(self, datasets):
        """Sets the datasets of this NewDashboardPanelDataAttributesParams.


        :param datasets: The datasets of this NewDashboardPanelDataAttributesParams.  # noqa: E501
        :type: list[NewDashboardPanelDataAttributesParamsDatasets]
        """

        self._datasets = datasets

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
        if issubclass(NewDashboardPanelDataAttributesParams, dict):
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
        if not isinstance(other, NewDashboardPanelDataAttributesParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
