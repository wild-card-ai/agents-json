# coding: utf-8

"""
    Resend

    Resend is the email platform for developers.  # noqa: E501

    OpenAPI spec version: 1.1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class InlineResponse20010(object):
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
        'object': 'str',
        'data': 'list[ListAudiencesResponseSuccessData]'
    }

    attribute_map = {
        'object': 'object',
        'data': 'data'
    }

    def __init__(self, object=None, data=None):  # noqa: E501
        """InlineResponse20010 - a model defined in Swagger"""  # noqa: E501
        self._object = None
        self._data = None
        self.discriminator = None
        if object is not None:
            self.object = object
        if data is not None:
            self.data = data

    @property
    def object(self):
        """Gets the object of this InlineResponse20010.  # noqa: E501

        Type of the response object.  # noqa: E501

        :return: The object of this InlineResponse20010.  # noqa: E501
        :rtype: str
        """
        return self._object

    @object.setter
    def object(self, object):
        """Sets the object of this InlineResponse20010.

        Type of the response object.  # noqa: E501

        :param object: The object of this InlineResponse20010.  # noqa: E501
        :type: str
        """

        self._object = object

    @property
    def data(self):
        """Gets the data of this InlineResponse20010.  # noqa: E501

        Array containing audience information.  # noqa: E501

        :return: The data of this InlineResponse20010.  # noqa: E501
        :rtype: list[ListAudiencesResponseSuccessData]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this InlineResponse20010.

        Array containing audience information.  # noqa: E501

        :param data: The data of this InlineResponse20010.  # noqa: E501
        :type: list[ListAudiencesResponseSuccessData]
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
        if issubclass(InlineResponse20010, dict):
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
        if not isinstance(other, InlineResponse20010):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
