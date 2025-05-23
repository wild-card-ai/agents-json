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

class ImageRenditionObject(object):
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
        'url': 'str',
        'width': 'str',
        'height': 'str',
        'size': 'str',
        'mp4': 'str',
        'mp4_size': 'str',
        'webp': 'str',
        'webp_size': 'str',
        'frames': 'str'
    }

    attribute_map = {
        'url': 'url',
        'width': 'width',
        'height': 'height',
        'size': 'size',
        'mp4': 'mp4',
        'mp4_size': 'mp4_size',
        'webp': 'webp',
        'webp_size': 'webp_size',
        'frames': 'frames'
    }

    def __init__(self, url=None, width=None, height=None, size=None, mp4=None, mp4_size=None, webp=None, webp_size=None, frames=None):  # noqa: E501
        """ImageRenditionObject - a model defined in Swagger"""  # noqa: E501
        self._url = None
        self._width = None
        self._height = None
        self._size = None
        self._mp4 = None
        self._mp4_size = None
        self._webp = None
        self._webp_size = None
        self._frames = None
        self.discriminator = None
        if url is not None:
            self.url = url
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if size is not None:
            self.size = size
        if mp4 is not None:
            self.mp4 = mp4
        if mp4_size is not None:
            self.mp4_size = mp4_size
        if webp is not None:
            self.webp = webp
        if webp_size is not None:
            self.webp_size = webp_size
        if frames is not None:
            self.frames = frames

    @property
    def url(self):
        """Gets the url of this ImageRenditionObject.  # noqa: E501

        The publicly-accessible direct URL for this GIF.  # noqa: E501

        :return: The url of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageRenditionObject.

        The publicly-accessible direct URL for this GIF.  # noqa: E501

        :param url: The url of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def width(self):
        """Gets the width of this ImageRenditionObject.  # noqa: E501

        The width of this GIF in pixels.  # noqa: E501

        :return: The width of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this ImageRenditionObject.

        The width of this GIF in pixels.  # noqa: E501

        :param width: The width of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._width = width

    @property
    def height(self):
        """Gets the height of this ImageRenditionObject.  # noqa: E501

        The height of this GIF in pixels.  # noqa: E501

        :return: The height of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this ImageRenditionObject.

        The height of this GIF in pixels.  # noqa: E501

        :param height: The height of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def size(self):
        """Gets the size of this ImageRenditionObject.  # noqa: E501

        The size of this GIF in bytes.  # noqa: E501

        :return: The size of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this ImageRenditionObject.

        The size of this GIF in bytes.  # noqa: E501

        :param size: The size of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def mp4(self):
        """Gets the mp4 of this ImageRenditionObject.  # noqa: E501

        The URL for this GIF in .MP4 format.  # noqa: E501

        :return: The mp4 of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._mp4

    @mp4.setter
    def mp4(self, mp4):
        """Sets the mp4 of this ImageRenditionObject.

        The URL for this GIF in .MP4 format.  # noqa: E501

        :param mp4: The mp4 of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._mp4 = mp4

    @property
    def mp4_size(self):
        """Gets the mp4_size of this ImageRenditionObject.  # noqa: E501

        The size in bytes of the .MP4 file corresponding to this GIF.  # noqa: E501

        :return: The mp4_size of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._mp4_size

    @mp4_size.setter
    def mp4_size(self, mp4_size):
        """Sets the mp4_size of this ImageRenditionObject.

        The size in bytes of the .MP4 file corresponding to this GIF.  # noqa: E501

        :param mp4_size: The mp4_size of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._mp4_size = mp4_size

    @property
    def webp(self):
        """Gets the webp of this ImageRenditionObject.  # noqa: E501

        The URL for this GIF in .webp format.  # noqa: E501

        :return: The webp of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._webp

    @webp.setter
    def webp(self, webp):
        """Sets the webp of this ImageRenditionObject.

        The URL for this GIF in .webp format.  # noqa: E501

        :param webp: The webp of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._webp = webp

    @property
    def webp_size(self):
        """Gets the webp_size of this ImageRenditionObject.  # noqa: E501

        The size in bytes of the .webp file corresponding to this GIF.  # noqa: E501

        :return: The webp_size of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._webp_size

    @webp_size.setter
    def webp_size(self, webp_size):
        """Sets the webp_size of this ImageRenditionObject.

        The size in bytes of the .webp file corresponding to this GIF.  # noqa: E501

        :param webp_size: The webp_size of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._webp_size = webp_size

    @property
    def frames(self):
        """Gets the frames of this ImageRenditionObject.  # noqa: E501

        The number of frames in this GIF.  # noqa: E501

        :return: The frames of this ImageRenditionObject.  # noqa: E501
        :rtype: str
        """
        return self._frames

    @frames.setter
    def frames(self, frames):
        """Sets the frames of this ImageRenditionObject.

        The number of frames in this GIF.  # noqa: E501

        :param frames: The frames of this ImageRenditionObject.  # noqa: E501
        :type: str
        """

        self._frames = frames

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
        if issubclass(ImageRenditionObject, dict):
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
        if not isinstance(other, ImageRenditionObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
