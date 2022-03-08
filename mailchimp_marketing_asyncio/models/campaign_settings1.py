# coding: utf-8

"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.74
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CampaignSettings1(object):
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
        'subject_line': 'str',
        'preview_text': 'str',
        'title': 'str',
        'from_name': 'str',
        'reply_to': 'str'
    }

    attribute_map = {
        'subject_line': 'subject_line',
        'preview_text': 'preview_text',
        'title': 'title',
        'from_name': 'from_name',
        'reply_to': 'reply_to'
    }

    def __init__(self, subject_line=None, preview_text=None, title=None, from_name=None, reply_to=None):  # noqa: E501
        """CampaignSettings1 - a model defined in Swagger"""  # noqa: E501

        self._subject_line = None
        self._preview_text = None
        self._title = None
        self._from_name = None
        self._reply_to = None
        self.discriminator = None

        if subject_line is not None:
            self.subject_line = subject_line
        if preview_text is not None:
            self.preview_text = preview_text
        if title is not None:
            self.title = title
        if from_name is not None:
            self.from_name = from_name
        if reply_to is not None:
            self.reply_to = reply_to

    @property
    def subject_line(self):
        """Gets the subject_line of this CampaignSettings1.  # noqa: E501

        The subject line for the campaign.  # noqa: E501

        :return: The subject_line of this CampaignSettings1.  # noqa: E501
        :rtype: str
        """
        return self._subject_line

    @subject_line.setter
    def subject_line(self, subject_line):
        """Sets the subject_line of this CampaignSettings1.

        The subject line for the campaign.  # noqa: E501

        :param subject_line: The subject_line of this CampaignSettings1.  # noqa: E501
        :type: str
        """

        self._subject_line = subject_line

    @property
    def preview_text(self):
        """Gets the preview_text of this CampaignSettings1.  # noqa: E501

        The preview text for the campaign.  # noqa: E501

        :return: The preview_text of this CampaignSettings1.  # noqa: E501
        :rtype: str
        """
        return self._preview_text

    @preview_text.setter
    def preview_text(self, preview_text):
        """Sets the preview_text of this CampaignSettings1.

        The preview text for the campaign.  # noqa: E501

        :param preview_text: The preview_text of this CampaignSettings1.  # noqa: E501
        :type: str
        """

        self._preview_text = preview_text

    @property
    def title(self):
        """Gets the title of this CampaignSettings1.  # noqa: E501

        The title of the Automation.  # noqa: E501

        :return: The title of this CampaignSettings1.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this CampaignSettings1.

        The title of the Automation.  # noqa: E501

        :param title: The title of this CampaignSettings1.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def from_name(self):
        """Gets the from_name of this CampaignSettings1.  # noqa: E501

        The 'from' name for the Automation (not an email address).  # noqa: E501

        :return: The from_name of this CampaignSettings1.  # noqa: E501
        :rtype: str
        """
        return self._from_name

    @from_name.setter
    def from_name(self, from_name):
        """Sets the from_name of this CampaignSettings1.

        The 'from' name for the Automation (not an email address).  # noqa: E501

        :param from_name: The from_name of this CampaignSettings1.  # noqa: E501
        :type: str
        """

        self._from_name = from_name

    @property
    def reply_to(self):
        """Gets the reply_to of this CampaignSettings1.  # noqa: E501

        The reply-to email address for the Automation.  # noqa: E501

        :return: The reply_to of this CampaignSettings1.  # noqa: E501
        :rtype: str
        """
        return self._reply_to

    @reply_to.setter
    def reply_to(self, reply_to):
        """Sets the reply_to of this CampaignSettings1.

        The reply-to email address for the Automation.  # noqa: E501

        :param reply_to: The reply_to of this CampaignSettings1.  # noqa: E501
        :type: str
        """

        self._reply_to = reply_to

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
        if issubclass(CampaignSettings1, dict):
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
        if not isinstance(other, CampaignSettings1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other