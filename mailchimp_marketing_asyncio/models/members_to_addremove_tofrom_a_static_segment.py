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


class MembersToAddremoveTofromAStaticSegment(object):
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
        'members_to_add': 'list[str]',
        'members_to_remove': 'list[str]'
    }

    attribute_map = {
        'members_to_add': 'members_to_add',
        'members_to_remove': 'members_to_remove'
    }

    def __init__(self, members_to_add=None, members_to_remove=None):  # noqa: E501
        """MembersToAddremoveTofromAStaticSegment - a model defined in Swagger"""  # noqa: E501

        self._members_to_add = None
        self._members_to_remove = None
        self.discriminator = None

        if members_to_add is not None:
            self.members_to_add = members_to_add
        if members_to_remove is not None:
            self.members_to_remove = members_to_remove

    @property
    def members_to_add(self):
        """Gets the members_to_add of this MembersToAddremoveTofromAStaticSegment.  # noqa: E501

        An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.  # noqa: E501

        :return: The members_to_add of this MembersToAddremoveTofromAStaticSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._members_to_add

    @members_to_add.setter
    def members_to_add(self, members_to_add):
        """Sets the members_to_add of this MembersToAddremoveTofromAStaticSegment.

        An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.  # noqa: E501

        :param members_to_add: The members_to_add of this MembersToAddremoveTofromAStaticSegment.  # noqa: E501
        :type: list[str]
        """

        self._members_to_add = members_to_add

    @property
    def members_to_remove(self):
        """Gets the members_to_remove of this MembersToAddremoveTofromAStaticSegment.  # noqa: E501

        An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.  # noqa: E501

        :return: The members_to_remove of this MembersToAddremoveTofromAStaticSegment.  # noqa: E501
        :rtype: list[str]
        """
        return self._members_to_remove

    @members_to_remove.setter
    def members_to_remove(self, members_to_remove):
        """Sets the members_to_remove of this MembersToAddremoveTofromAStaticSegment.

        An array of emails to be used for a static segment. Any emails provided that are not present on the list will be ignored. A maximum of 500 members can be sent.  # noqa: E501

        :param members_to_remove: The members_to_remove of this MembersToAddremoveTofromAStaticSegment.  # noqa: E501
        :type: list[str]
        """

        self._members_to_remove = members_to_remove

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
        if issubclass(MembersToAddremoveTofromAStaticSegment, dict):
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
        if not isinstance(other, MembersToAddremoveTofromAStaticSegment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other