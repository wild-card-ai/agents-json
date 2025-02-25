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

class AnalyticsObject(object):
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
        'onload': 'GIFObjectAnalyticsOnload',
        'onclick': 'GIFObjectAnalyticsOnclick',
        'onsent': 'GIFObjectAnalyticsOnsent'
    }

    attribute_map = {
        'onload': 'onload',
        'onclick': 'onclick',
        'onsent': 'onsent'
    }

    def __init__(self, onload=None, onclick=None, onsent=None):  # noqa: E501
        """AnalyticsObject - a model defined in Swagger"""  # noqa: E501
        self._onload = None
        self._onclick = None
        self._onsent = None
        self.discriminator = None
        if onload is not None:
            self.onload = onload
        if onclick is not None:
            self.onclick = onclick
        if onsent is not None:
            self.onsent = onsent

    @property
    def onload(self):
        """Gets the onload of this AnalyticsObject.  # noqa: E501


        :return: The onload of this AnalyticsObject.  # noqa: E501
        :rtype: GIFObjectAnalyticsOnload
        """
        return self._onload

    @onload.setter
    def onload(self, onload):
        """Sets the onload of this AnalyticsObject.


        :param onload: The onload of this AnalyticsObject.  # noqa: E501
        :type: GIFObjectAnalyticsOnload
        """

        self._onload = onload

    @property
    def onclick(self):
        """Gets the onclick of this AnalyticsObject.  # noqa: E501


        :return: The onclick of this AnalyticsObject.  # noqa: E501
        :rtype: GIFObjectAnalyticsOnclick
        """
        return self._onclick

    @onclick.setter
    def onclick(self, onclick):
        """Sets the onclick of this AnalyticsObject.


        :param onclick: The onclick of this AnalyticsObject.  # noqa: E501
        :type: GIFObjectAnalyticsOnclick
        """

        self._onclick = onclick

    @property
    def onsent(self):
        """Gets the onsent of this AnalyticsObject.  # noqa: E501


        :return: The onsent of this AnalyticsObject.  # noqa: E501
        :rtype: GIFObjectAnalyticsOnsent
        """
        return self._onsent

    @onsent.setter
    def onsent(self, onsent):
        """Sets the onsent of this AnalyticsObject.


        :param onsent: The onsent of this AnalyticsObject.  # noqa: E501
        :type: GIFObjectAnalyticsOnsent
        """

        self._onsent = onsent

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
        if issubclass(AnalyticsObject, dict):
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
        if not isinstance(other, AnalyticsObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
