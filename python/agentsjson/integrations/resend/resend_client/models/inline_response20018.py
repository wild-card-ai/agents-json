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

class InlineResponse20018(object):
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
        'id': 'str',
        'name': 'str',
        'audience_id': 'str',
        '_from': 'str',
        'subject': 'str',
        'reply_to': 'list[str]',
        'preview_text': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'scheduled_at': 'datetime',
        'sent_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'audience_id': 'audience_id',
        '_from': 'from',
        'subject': 'subject',
        'reply_to': 'reply_to',
        'preview_text': 'preview_text',
        'status': 'status',
        'created_at': 'created_at',
        'scheduled_at': 'scheduled_at',
        'sent_at': 'sent_at'
    }

    def __init__(self, id=None, name=None, audience_id=None, _from=None, subject=None, reply_to=None, preview_text=None, status=None, created_at=None, scheduled_at=None, sent_at=None):  # noqa: E501
        """InlineResponse20018 - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._audience_id = None
        self.__from = None
        self._subject = None
        self._reply_to = None
        self._preview_text = None
        self._status = None
        self._created_at = None
        self._scheduled_at = None
        self._sent_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if audience_id is not None:
            self.audience_id = audience_id
        if _from is not None:
            self._from = _from
        if subject is not None:
            self.subject = subject
        if reply_to is not None:
            self.reply_to = reply_to
        if preview_text is not None:
            self.preview_text = preview_text
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if sent_at is not None:
            self.sent_at = sent_at

    @property
    def id(self):
        """Gets the id of this InlineResponse20018.  # noqa: E501

        Unique identifier for the broadcast.  # noqa: E501

        :return: The id of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InlineResponse20018.

        Unique identifier for the broadcast.  # noqa: E501

        :param id: The id of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this InlineResponse20018.  # noqa: E501

        Name of the broadcast.  # noqa: E501

        :return: The name of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this InlineResponse20018.

        Name of the broadcast.  # noqa: E501

        :param name: The name of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def audience_id(self):
        """Gets the audience_id of this InlineResponse20018.  # noqa: E501

        Unique identifier of the audience this broadcast will be sent to.  # noqa: E501

        :return: The audience_id of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._audience_id

    @audience_id.setter
    def audience_id(self, audience_id):
        """Sets the audience_id of this InlineResponse20018.

        Unique identifier of the audience this broadcast will be sent to.  # noqa: E501

        :param audience_id: The audience_id of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._audience_id = audience_id

    @property
    def _from(self):
        """Gets the _from of this InlineResponse20018.  # noqa: E501

        The email address of the sender.  # noqa: E501

        :return: The _from of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this InlineResponse20018.

        The email address of the sender.  # noqa: E501

        :param _from: The _from of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self.__from = _from

    @property
    def subject(self):
        """Gets the subject of this InlineResponse20018.  # noqa: E501

        The subject line of the email.  # noqa: E501

        :return: The subject of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this InlineResponse20018.

        The subject line of the email.  # noqa: E501

        :param subject: The subject of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def reply_to(self):
        """Gets the reply_to of this InlineResponse20018.  # noqa: E501

        The email addresses to which replies should be sent.  # noqa: E501

        :return: The reply_to of this InlineResponse20018.  # noqa: E501
        :rtype: list[str]
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this InlineResponse20018.

        The email addresses to which replies should be sent.  # noqa: E501

        :param reply_to: The reply_to of this InlineResponse20018.  # noqa: E501
        :type: list[str]
        """

        self._reply_to = reply_to

    @property
    def preview_text(self):
        """Gets the preview_text of this InlineResponse20018.  # noqa: E501

        The preview text of the email.  # noqa: E501

        :return: The preview_text of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._preview_text

    @preview_text.setter
    def preview_text(self, preview_text):
        """Sets the preview_text of this InlineResponse20018.

        The preview text of the email.  # noqa: E501

        :param preview_text: The preview_text of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._preview_text = preview_text

    @property
    def status(self):
        """Gets the status of this InlineResponse20018.  # noqa: E501

        The status of the broadcast.  # noqa: E501

        :return: The status of this InlineResponse20018.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this InlineResponse20018.

        The status of the broadcast.  # noqa: E501

        :param status: The status of this InlineResponse20018.  # noqa: E501
        :type: str
        """

        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this InlineResponse20018.  # noqa: E501

        Timestamp indicating when the broadcast was created.  # noqa: E501

        :return: The created_at of this InlineResponse20018.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this InlineResponse20018.

        Timestamp indicating when the broadcast was created.  # noqa: E501

        :param created_at: The created_at of this InlineResponse20018.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this InlineResponse20018.  # noqa: E501

        Timestamp indicating when the broadcast is scheduled to be sent.  # noqa: E501

        :return: The scheduled_at of this InlineResponse20018.  # noqa: E501
        :rtype: datetime
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this InlineResponse20018.

        Timestamp indicating when the broadcast is scheduled to be sent.  # noqa: E501

        :param scheduled_at: The scheduled_at of this InlineResponse20018.  # noqa: E501
        :type: datetime
        """

        self._scheduled_at = scheduled_at

    @property
    def sent_at(self):
        """Gets the sent_at of this InlineResponse20018.  # noqa: E501

        Timestamp indicating when the broadcast was sent.  # noqa: E501

        :return: The sent_at of this InlineResponse20018.  # noqa: E501
        :rtype: datetime
        """
        return self._sent_at

    @sent_at.setter
    def sent_at(self, sent_at):
        """Sets the sent_at of this InlineResponse20018.

        Timestamp indicating when the broadcast was sent.  # noqa: E501

        :param sent_at: The sent_at of this InlineResponse20018.  # noqa: E501
        :type: datetime
        """

        self._sent_at = sent_at

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
        if issubclass(InlineResponse20018, dict):
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
        if not isinstance(other, InlineResponse20018):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
