# coding: utf-8

"""
    Giphy API

    The Giphy API allows you to search, upload, and manage GIFs and stickers. It provides endpoints to access trending content, search for specific GIFs, translate phrases into GIFs, and more.   # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PaginationObject(object):
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
        'total_count': 'int',
        'count': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'total_count': 'total_count',
        'count': 'count',
        'offset': 'offset'
    }

    def __init__(self, total_count=None, count=None, offset=None):  # noqa: E501
        """PaginationObject - a model defined in Swagger"""  # noqa: E501
        self._total_count = None
        self._count = None
        self._offset = None
        self.discriminator = None
        if total_count is not None:
            self.total_count = total_count
        if count is not None:
            self.count = count
        if offset is not None:
            self.offset = offset

    @property
    def total_count(self):
        """Gets the total_count of this PaginationObject.  # noqa: E501

        Total number of items available (not returned on every endpoint).  # noqa: E501

        :return: The total_count of this PaginationObject.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this PaginationObject.

        Total number of items available (not returned on every endpoint).  # noqa: E501

        :param total_count: The total_count of this PaginationObject.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

    @property
    def count(self):
        """Gets the count of this PaginationObject.  # noqa: E501

        Total number of items returned.  # noqa: E501

        :return: The count of this PaginationObject.  # noqa: E501
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this PaginationObject.

        Total number of items returned.  # noqa: E501

        :param count: The count of this PaginationObject.  # noqa: E501
        :type: int
        """

        self._count = count

    @property
    def offset(self):
        """Gets the offset of this PaginationObject.  # noqa: E501

        Position in pagination.  # noqa: E501

        :return: The offset of this PaginationObject.  # noqa: E501
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this PaginationObject.

        Position in pagination.  # noqa: E501

        :param offset: The offset of this PaginationObject.  # noqa: E501
        :type: int
        """

        self._offset = offset

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
        if issubclass(PaginationObject, dict):
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
        if not isinstance(other, PaginationObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
