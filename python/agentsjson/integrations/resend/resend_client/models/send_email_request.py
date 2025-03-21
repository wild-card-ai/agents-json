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

class SendEmailRequest(object):
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
        '_from': 'str',
        'to': 'list[str]',
        'subject': 'str',
        'bcc': 'str',
        'cc': 'str',
        'reply_to': 'str',
        'html': 'str',
        'text': 'str',
        'headers': 'object',
        'scheduled_at': 'str',
        'attachments': 'list[EmailsAttachments]',
        'tags': 'list[EmailsTags]'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'subject': 'subject',
        'bcc': 'bcc',
        'cc': 'cc',
        'reply_to': 'reply_to',
        'html': 'html',
        'text': 'text',
        'headers': 'headers',
        'scheduled_at': 'scheduled_at',
        'attachments': 'attachments',
        'tags': 'tags'
    }

    def __init__(self, _from=None, to=None, subject=None, bcc=None, cc=None, reply_to=None, html=None, text=None, headers=None, scheduled_at=None, attachments=None, tags=None):  # noqa: E501
        """SendEmailRequest - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._to = None
        self._subject = None
        self._bcc = None
        self._cc = None
        self._reply_to = None
        self._html = None
        self._text = None
        self._headers = None
        self._scheduled_at = None
        self._attachments = None
        self._tags = None
        self.discriminator = None
        self._from = _from
        self.to = to
        self.subject = subject
        if bcc is not None:
            self.bcc = bcc
        if cc is not None:
            self.cc = cc
        if reply_to is not None:
            self.reply_to = reply_to
        if html is not None:
            self.html = html
        if text is not None:
            self.text = text
        if headers is not None:
            self.headers = headers
        if scheduled_at is not None:
            self.scheduled_at = scheduled_at
        if attachments is not None:
            self.attachments = attachments
        if tags is not None:
            self.tags = tags

    @property
    def _from(self):
        """Gets the _from of this SendEmailRequest.  # noqa: E501

        Sender email address. To include a friendly name, use the format \"Your Name <sender@domain.com>\".  # noqa: E501

        :return: The _from of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this SendEmailRequest.

        Sender email address. To include a friendly name, use the format \"Your Name <sender@domain.com>\".  # noqa: E501

        :param _from: The _from of this SendEmailRequest.  # noqa: E501
        :type: str
        """
        if _from is None:
            raise ValueError("Invalid value for `_from`, must not be `None`")  # noqa: E501

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this SendEmailRequest.  # noqa: E501


        :return: The to of this SendEmailRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this SendEmailRequest.


        :param to: The to of this SendEmailRequest.  # noqa: E501
        :type: list[str]
        """
        if to is None:
            raise ValueError("Invalid value for `to`, must not be `None`")  # noqa: E501

        self._to = to

    @property
    def subject(self):
        """Gets the subject of this SendEmailRequest.  # noqa: E501

        Email subject.  # noqa: E501

        :return: The subject of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SendEmailRequest.

        Email subject.  # noqa: E501

        :param subject: The subject of this SendEmailRequest.  # noqa: E501
        :type: str
        """
        if subject is None:
            raise ValueError("Invalid value for `subject`, must not be `None`")  # noqa: E501

        self._subject = subject

    @property
    def bcc(self):
        """Gets the bcc of this SendEmailRequest.  # noqa: E501

        Bcc recipient email address. For multiple addresses, send as an array of strings.  # noqa: E501

        :return: The bcc of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._bcc

    @bcc.setter
    def bcc(self, bcc):
        """Sets the bcc of this SendEmailRequest.

        Bcc recipient email address. For multiple addresses, send as an array of strings.  # noqa: E501

        :param bcc: The bcc of this SendEmailRequest.  # noqa: E501
        :type: str
        """

        self._bcc = bcc

    @property
    def cc(self):
        """Gets the cc of this SendEmailRequest.  # noqa: E501

        Cc recipient email address. For multiple addresses, send as an array of strings.  # noqa: E501

        :return: The cc of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this SendEmailRequest.

        Cc recipient email address. For multiple addresses, send as an array of strings.  # noqa: E501

        :param cc: The cc of this SendEmailRequest.  # noqa: E501
        :type: str
        """

        self._cc = cc

    @property
    def reply_to(self):
        """Gets the reply_to of this SendEmailRequest.  # noqa: E501

        Reply-to email address. For multiple addresses, send as an array of strings.  # noqa: E501

        :return: The reply_to of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this SendEmailRequest.

        Reply-to email address. For multiple addresses, send as an array of strings.  # noqa: E501

        :param reply_to: The reply_to of this SendEmailRequest.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

    @property
    def html(self):
        """Gets the html of this SendEmailRequest.  # noqa: E501

        The HTML version of the message.  # noqa: E501

        :return: The html of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this SendEmailRequest.

        The HTML version of the message.  # noqa: E501

        :param html: The html of this SendEmailRequest.  # noqa: E501
        :type: str
        """

        self._html = html

    @property
    def text(self):
        """Gets the text of this SendEmailRequest.  # noqa: E501

        The plain text version of the message.  # noqa: E501

        :return: The text of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SendEmailRequest.

        The plain text version of the message.  # noqa: E501

        :param text: The text of this SendEmailRequest.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def headers(self):
        """Gets the headers of this SendEmailRequest.  # noqa: E501

        Custom headers to add to the email.  # noqa: E501

        :return: The headers of this SendEmailRequest.  # noqa: E501
        :rtype: object
        """
        return self._headers

    @headers.setter
    def headers(self, headers):
        """Sets the headers of this SendEmailRequest.

        Custom headers to add to the email.  # noqa: E501

        :param headers: The headers of this SendEmailRequest.  # noqa: E501
        :type: object
        """

        self._headers = headers

    @property
    def scheduled_at(self):
        """Gets the scheduled_at of this SendEmailRequest.  # noqa: E501

        Schedule email to be sent later. The date should be in ISO 8601 format.  # noqa: E501

        :return: The scheduled_at of this SendEmailRequest.  # noqa: E501
        :rtype: str
        """
        return self._scheduled_at

    @scheduled_at.setter
    def scheduled_at(self, scheduled_at):
        """Sets the scheduled_at of this SendEmailRequest.

        Schedule email to be sent later. The date should be in ISO 8601 format.  # noqa: E501

        :param scheduled_at: The scheduled_at of this SendEmailRequest.  # noqa: E501
        :type: str
        """

        self._scheduled_at = scheduled_at

    @property
    def attachments(self):
        """Gets the attachments of this SendEmailRequest.  # noqa: E501


        :return: The attachments of this SendEmailRequest.  # noqa: E501
        :rtype: list[EmailsAttachments]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """Sets the attachments of this SendEmailRequest.


        :param attachments: The attachments of this SendEmailRequest.  # noqa: E501
        :type: list[EmailsAttachments]
        """

        self._attachments = attachments

    @property
    def tags(self):
        """Gets the tags of this SendEmailRequest.  # noqa: E501


        :return: The tags of this SendEmailRequest.  # noqa: E501
        :rtype: list[EmailsTags]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this SendEmailRequest.


        :param tags: The tags of this SendEmailRequest.  # noqa: E501
        :type: list[EmailsTags]
        """

        self._tags = tags

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
        if issubclass(SendEmailRequest, dict):
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
        if not isinstance(other, SendEmailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
