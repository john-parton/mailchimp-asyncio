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


class Forwards(object):
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
        'forwards_count': 'int',
        'forwards_opens': 'int'
    }

    attribute_map = {
        'forwards_count': 'forwards_count',
        'forwards_opens': 'forwards_opens'
    }

    def __init__(self, forwards_count=None, forwards_opens=None):  # noqa: E501
        """Forwards - a model defined in Swagger"""  # noqa: E501

        self._forwards_count = None
        self._forwards_opens = None
        self.discriminator = None

        if forwards_count is not None:
            self.forwards_count = forwards_count
        if forwards_opens is not None:
            self.forwards_opens = forwards_opens

    @property
    def forwards_count(self):
        """Gets the forwards_count of this Forwards.  # noqa: E501

        How many times the campaign has been forwarded.  # noqa: E501

        :return: The forwards_count of this Forwards.  # noqa: E501
        :rtype: int
        """
        return self._forwards_count

    @forwards_count.setter
    def forwards_count(self, forwards_count):
        """Sets the forwards_count of this Forwards.

        How many times the campaign has been forwarded.  # noqa: E501

        :param forwards_count: The forwards_count of this Forwards.  # noqa: E501
        :type: int
        """

        self._forwards_count = forwards_count

    @property
    def forwards_opens(self):
        """Gets the forwards_opens of this Forwards.  # noqa: E501

        How many times the forwarded campaign has been opened.  # noqa: E501

        :return: The forwards_opens of this Forwards.  # noqa: E501
        :rtype: int
        """
        return self._forwards_opens

    @forwards_opens.setter
    def forwards_opens(self, forwards_opens):
        """Sets the forwards_opens of this Forwards.

        How many times the forwarded campaign has been opened.  # noqa: E501

        :param forwards_opens: The forwards_opens of this Forwards.  # noqa: E501
        :type: int
        """

        self._forwards_opens = forwards_opens

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
        if issubclass(Forwards, dict):
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
        if not isinstance(other, Forwards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
