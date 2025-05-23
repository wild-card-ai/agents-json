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

class AllOfEmojiResponseDataItems(object):
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
        'type': 'str',
        'id': 'str',
        'url': 'str',
        'slug': 'str',
        'bitly_url': 'str',
        'embed_url': 'str',
        'username': 'str',
        'source': 'str',
        'title': 'str',
        'alt_text': 'str',
        'rating': 'str',
        'content_url': 'str',
        'source_tld': 'str',
        'source_post_url': 'str',
        'is_sticker': 'int',
        'import_datetime': 'str',
        'trending_datetime': 'str',
        'images': 'dict(str, object)',
        'user': 'object',
        'analytics_response_payload': 'str',
        'analytics': 'object',
        'variation_count': 'int'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'url': 'url',
        'slug': 'slug',
        'bitly_url': 'bitly_url',
        'embed_url': 'embed_url',
        'username': 'username',
        'source': 'source',
        'title': 'title',
        'alt_text': 'alt_text',
        'rating': 'rating',
        'content_url': 'content_url',
        'source_tld': 'source_tld',
        'source_post_url': 'source_post_url',
        'is_sticker': 'is_sticker',
        'import_datetime': 'import_datetime',
        'trending_datetime': 'trending_datetime',
        'images': 'images',
        'user': 'user',
        'analytics_response_payload': 'analytics_response_payload',
        'analytics': 'analytics',
        'variation_count': 'variation_count'
    }

    def __init__(self, type=None, id=None, url=None, slug=None, bitly_url=None, embed_url=None, username=None, source=None, title=None, alt_text=None, rating=None, content_url=None, source_tld=None, source_post_url=None, is_sticker=None, import_datetime=None, trending_datetime=None, images=None, user=None, analytics_response_payload=None, analytics=None, variation_count=None):  # noqa: E501
        """AllOfEmojiResponseDataItems - a model defined in Swagger"""  # noqa: E501
        self._type = None
        self._id = None
        self._url = None
        self._slug = None
        self._bitly_url = None
        self._embed_url = None
        self._username = None
        self._source = None
        self._title = None
        self._alt_text = None
        self._rating = None
        self._content_url = None
        self._source_tld = None
        self._source_post_url = None
        self._is_sticker = None
        self._import_datetime = None
        self._trending_datetime = None
        self._images = None
        self._user = None
        self._analytics_response_payload = None
        self._analytics = None
        self._variation_count = None
        self.discriminator = None
        if type is not None:
            self.type = type
        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if slug is not None:
            self.slug = slug
        if bitly_url is not None:
            self.bitly_url = bitly_url
        if embed_url is not None:
            self.embed_url = embed_url
        if username is not None:
            self.username = username
        if source is not None:
            self.source = source
        if title is not None:
            self.title = title
        if alt_text is not None:
            self.alt_text = alt_text
        if rating is not None:
            self.rating = rating
        if content_url is not None:
            self.content_url = content_url
        if source_tld is not None:
            self.source_tld = source_tld
        if source_post_url is not None:
            self.source_post_url = source_post_url
        if is_sticker is not None:
            self.is_sticker = is_sticker
        if import_datetime is not None:
            self.import_datetime = import_datetime
        if trending_datetime is not None:
            self.trending_datetime = trending_datetime
        if images is not None:
            self.images = images
        if user is not None:
            self.user = user
        if analytics_response_payload is not None:
            self.analytics_response_payload = analytics_response_payload
        if analytics is not None:
            self.analytics = analytics
        if variation_count is not None:
            self.variation_count = variation_count

    @property
    def type(self):
        """Gets the type of this AllOfEmojiResponseDataItems.  # noqa: E501

        Type of the object.  # noqa: E501

        :return: The type of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AllOfEmojiResponseDataItems.

        Type of the object.  # noqa: E501

        :param type: The type of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def id(self):
        """Gets the id of this AllOfEmojiResponseDataItems.  # noqa: E501

        This GIF's unique ID.  # noqa: E501

        :return: The id of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AllOfEmojiResponseDataItems.

        This GIF's unique ID.  # noqa: E501

        :param id: The id of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this AllOfEmojiResponseDataItems.  # noqa: E501

        The unique URL for this GIF.  # noqa: E501

        :return: The url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AllOfEmojiResponseDataItems.

        The unique URL for this GIF.  # noqa: E501

        :param url: The url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def slug(self):
        """Gets the slug of this AllOfEmojiResponseDataItems.  # noqa: E501

        The unique slug used in this GIF's URL.  # noqa: E501

        :return: The slug of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this AllOfEmojiResponseDataItems.

        The unique slug used in this GIF's URL.  # noqa: E501

        :param slug: The slug of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._slug = slug

    @property
    def bitly_url(self):
        """Gets the bitly_url of this AllOfEmojiResponseDataItems.  # noqa: E501

        The unique bit.ly URL for this GIF.  # noqa: E501

        :return: The bitly_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._bitly_url

    @bitly_url.setter
    def bitly_url(self, bitly_url):
        """Sets the bitly_url of this AllOfEmojiResponseDataItems.

        The unique bit.ly URL for this GIF.  # noqa: E501

        :param bitly_url: The bitly_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._bitly_url = bitly_url

    @property
    def embed_url(self):
        """Gets the embed_url of this AllOfEmojiResponseDataItems.  # noqa: E501

        A URL used for embedding this GIF.  # noqa: E501

        :return: The embed_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._embed_url

    @embed_url.setter
    def embed_url(self, embed_url):
        """Sets the embed_url of this AllOfEmojiResponseDataItems.

        A URL used for embedding this GIF.  # noqa: E501

        :param embed_url: The embed_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._embed_url = embed_url

    @property
    def username(self):
        """Gets the username of this AllOfEmojiResponseDataItems.  # noqa: E501

        The username this GIF is attached to, if applicable.  # noqa: E501

        :return: The username of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this AllOfEmojiResponseDataItems.

        The username this GIF is attached to, if applicable.  # noqa: E501

        :param username: The username of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def source(self):
        """Gets the source of this AllOfEmojiResponseDataItems.  # noqa: E501

        The page on which this GIF was found.  # noqa: E501

        :return: The source of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this AllOfEmojiResponseDataItems.

        The page on which this GIF was found.  # noqa: E501

        :param source: The source of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._source = source

    @property
    def title(self):
        """Gets the title of this AllOfEmojiResponseDataItems.  # noqa: E501

        The title that appears on giphy.com for this GIF.  # noqa: E501

        :return: The title of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this AllOfEmojiResponseDataItems.

        The title that appears on giphy.com for this GIF.  # noqa: E501

        :param title: The title of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def alt_text(self):
        """Gets the alt_text of this AllOfEmojiResponseDataItems.  # noqa: E501

        Alt text enables assistive programs to read descriptions of GIFs.  # noqa: E501

        :return: The alt_text of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._alt_text

    @alt_text.setter
    def alt_text(self, alt_text):
        """Sets the alt_text of this AllOfEmojiResponseDataItems.

        Alt text enables assistive programs to read descriptions of GIFs.  # noqa: E501

        :param alt_text: The alt_text of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._alt_text = alt_text

    @property
    def rating(self):
        """Gets the rating of this AllOfEmojiResponseDataItems.  # noqa: E501

        The MPAA-style rating for this content.  # noqa: E501

        :return: The rating of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._rating

    @rating.setter
    def rating(self, rating):
        """Sets the rating of this AllOfEmojiResponseDataItems.

        The MPAA-style rating for this content.  # noqa: E501

        :param rating: The rating of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._rating = rating

    @property
    def content_url(self):
        """Gets the content_url of this AllOfEmojiResponseDataItems.  # noqa: E501

        Currently unused.  # noqa: E501

        :return: The content_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._content_url

    @content_url.setter
    def content_url(self, content_url):
        """Sets the content_url of this AllOfEmojiResponseDataItems.

        Currently unused.  # noqa: E501

        :param content_url: The content_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._content_url = content_url

    @property
    def source_tld(self):
        """Gets the source_tld of this AllOfEmojiResponseDataItems.  # noqa: E501

        The top-level domain of the source URL.  # noqa: E501

        :return: The source_tld of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._source_tld

    @source_tld.setter
    def source_tld(self, source_tld):
        """Sets the source_tld of this AllOfEmojiResponseDataItems.

        The top-level domain of the source URL.  # noqa: E501

        :param source_tld: The source_tld of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._source_tld = source_tld

    @property
    def source_post_url(self):
        """Gets the source_post_url of this AllOfEmojiResponseDataItems.  # noqa: E501

        The URL of the webpage on which this GIF was found.  # noqa: E501

        :return: The source_post_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._source_post_url

    @source_post_url.setter
    def source_post_url(self, source_post_url):
        """Sets the source_post_url of this AllOfEmojiResponseDataItems.

        The URL of the webpage on which this GIF was found.  # noqa: E501

        :param source_post_url: The source_post_url of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._source_post_url = source_post_url

    @property
    def is_sticker(self):
        """Gets the is_sticker of this AllOfEmojiResponseDataItems.  # noqa: E501

        Whether the GIF is a sticker (1) or not (0).  # noqa: E501

        :return: The is_sticker of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._is_sticker

    @is_sticker.setter
    def is_sticker(self, is_sticker):
        """Sets the is_sticker of this AllOfEmojiResponseDataItems.

        Whether the GIF is a sticker (1) or not (0).  # noqa: E501

        :param is_sticker: The is_sticker of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: int
        """

        self._is_sticker = is_sticker

    @property
    def import_datetime(self):
        """Gets the import_datetime of this AllOfEmojiResponseDataItems.  # noqa: E501

        The creation or upload date from this GIF's source.  # noqa: E501

        :return: The import_datetime of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._import_datetime

    @import_datetime.setter
    def import_datetime(self, import_datetime):
        """Sets the import_datetime of this AllOfEmojiResponseDataItems.

        The creation or upload date from this GIF's source.  # noqa: E501

        :param import_datetime: The import_datetime of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._import_datetime = import_datetime

    @property
    def trending_datetime(self):
        """Gets the trending_datetime of this AllOfEmojiResponseDataItems.  # noqa: E501

        The date on which this GIF was marked trending, if applicable.  # noqa: E501

        :return: The trending_datetime of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._trending_datetime

    @trending_datetime.setter
    def trending_datetime(self, trending_datetime):
        """Sets the trending_datetime of this AllOfEmojiResponseDataItems.

        The date on which this GIF was marked trending, if applicable.  # noqa: E501

        :param trending_datetime: The trending_datetime of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._trending_datetime = trending_datetime

    @property
    def images(self):
        """Gets the images of this AllOfEmojiResponseDataItems.  # noqa: E501

        An object containing data for various available formats and sizes of this GIF.  # noqa: E501

        :return: The images of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this AllOfEmojiResponseDataItems.

        An object containing data for various available formats and sizes of this GIF.  # noqa: E501

        :param images: The images of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: dict(str, object)
        """

        self._images = images

    @property
    def user(self):
        """Gets the user of this AllOfEmojiResponseDataItems.  # noqa: E501


        :return: The user of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: object
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this AllOfEmojiResponseDataItems.


        :param user: The user of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: object
        """

        self._user = user

    @property
    def analytics_response_payload(self):
        """Gets the analytics_response_payload of this AllOfEmojiResponseDataItems.  # noqa: E501

        Used for action registration.  # noqa: E501

        :return: The analytics_response_payload of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: str
        """
        return self._analytics_response_payload

    @analytics_response_payload.setter
    def analytics_response_payload(self, analytics_response_payload):
        """Sets the analytics_response_payload of this AllOfEmojiResponseDataItems.

        Used for action registration.  # noqa: E501

        :param analytics_response_payload: The analytics_response_payload of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: str
        """

        self._analytics_response_payload = analytics_response_payload

    @property
    def analytics(self):
        """Gets the analytics of this AllOfEmojiResponseDataItems.  # noqa: E501


        :return: The analytics of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: object
        """
        return self._analytics

    @analytics.setter
    def analytics(self, analytics):
        """Sets the analytics of this AllOfEmojiResponseDataItems.


        :param analytics: The analytics of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: object
        """

        self._analytics = analytics

    @property
    def variation_count(self):
        """Gets the variation_count of this AllOfEmojiResponseDataItems.  # noqa: E501

        The number of variations associated with the emoji.  # noqa: E501

        :return: The variation_count of this AllOfEmojiResponseDataItems.  # noqa: E501
        :rtype: int
        """
        return self._variation_count

    @variation_count.setter
    def variation_count(self, variation_count):
        """Sets the variation_count of this AllOfEmojiResponseDataItems.

        The number of variations associated with the emoji.  # noqa: E501

        :param variation_count: The variation_count of this AllOfEmojiResponseDataItems.  # noqa: E501
        :type: int
        """

        self._variation_count = variation_count

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
        if issubclass(AllOfEmojiResponseDataItems, dict):
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
        if not isinstance(other, AllOfEmojiResponseDataItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
