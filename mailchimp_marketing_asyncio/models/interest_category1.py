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


class InterestCategory1(object):
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
        'title': 'str',
        'display_order': 'int',
        'type': 'str'
    }

    attribute_map = {
        'title': 'title',
        'display_order': 'display_order',
        'type': 'type'
    }

    def __init__(self, title=None, display_order=None, type=None):  # noqa: E501
        """InterestCategory1 - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._display_order = None
        self._type = None
        self.discriminator = None

        self.title = title
        if display_order is not None:
            self.display_order = display_order
        self.type = type

    @property
    def title(self):
        """Gets the title of this InterestCategory1.  # noqa: E501

        The text description of this category. This field appears on signup forms and is often phrased as a question.  # noqa: E501

        :return: The title of this InterestCategory1.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this InterestCategory1.

        The text description of this category. This field appears on signup forms and is often phrased as a question.  # noqa: E501

        :param title: The title of this InterestCategory1.  # noqa: E501
        :type: str
        """
        if title is None:
            raise ValueError("Invalid value for `title`, must not be `None`")  # noqa: E501

        self._title = title

    @property
    def display_order(self):
        """Gets the display_order of this InterestCategory1.  # noqa: E501

        The order that the categories are displayed in the list. Lower numbers display first.  # noqa: E501

        :return: The display_order of this InterestCategory1.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this InterestCategory1.

        The order that the categories are displayed in the list. Lower numbers display first.  # noqa: E501

        :param display_order: The display_order of this InterestCategory1.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def type(self):
        """Gets the type of this InterestCategory1.  # noqa: E501

        Determines how this category’s interests appear on signup forms.  # noqa: E501

        :return: The type of this InterestCategory1.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InterestCategory1.

        Determines how this category’s interests appear on signup forms.  # noqa: E501

        :param type: The type of this InterestCategory1.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["checkboxes", "dropdown", "radio", "hidden"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(InterestCategory1, dict):
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
        if not isinstance(other, InterestCategory1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
