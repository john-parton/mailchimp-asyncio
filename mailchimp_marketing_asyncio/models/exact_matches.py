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


class ExactMatches(object):
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
        'members': 'list[ListMembers2]',
        'total_items': 'int'
    }

    attribute_map = {
        'members': 'members',
        'total_items': 'total_items'
    }

    def __init__(self, members=None, total_items=None):  # noqa: E501
        """ExactMatches - a model defined in Swagger"""  # noqa: E501

        self._members = None
        self._total_items = None
        self.discriminator = None

        if members is not None:
            self.members = members
        if total_items is not None:
            self.total_items = total_items

    @property
    def members(self):
        """Gets the members of this ExactMatches.  # noqa: E501

        An array of objects, each representing a specific list member.  # noqa: E501

        :return: The members of this ExactMatches.  # noqa: E501
        :rtype: list[ListMembers2]
        """
        return self._members

    @members.setter
    def members(self, members):
        """Sets the members of this ExactMatches.

        An array of objects, each representing a specific list member.  # noqa: E501

        :param members: The members of this ExactMatches.  # noqa: E501
        :type: list[ListMembers2]
        """

        self._members = members

    @property
    def total_items(self):
        """Gets the total_items of this ExactMatches.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this ExactMatches.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this ExactMatches.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this ExactMatches.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

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
        if issubclass(ExactMatches, dict):
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
        if not isinstance(other, ExactMatches):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
