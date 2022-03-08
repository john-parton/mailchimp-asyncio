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


class List5(object):
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
        'list_id': 'str',
        'segment_opts': 'SegmentOptions1'
    }

    attribute_map = {
        'list_id': 'list_id',
        'segment_opts': 'segment_opts'
    }

    def __init__(self, list_id=None, segment_opts=None):  # noqa: E501
        """List5 - a model defined in Swagger"""  # noqa: E501

        self._list_id = None
        self._segment_opts = None
        self.discriminator = None

        self.list_id = list_id
        if segment_opts is not None:
            self.segment_opts = segment_opts

    @property
    def list_id(self):
        """Gets the list_id of this List5.  # noqa: E501

        The unique list id.  # noqa: E501

        :return: The list_id of this List5.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this List5.

        The unique list id.  # noqa: E501

        :param list_id: The list_id of this List5.  # noqa: E501
        :type: str
        """
        if list_id is None:
            raise ValueError("Invalid value for `list_id`, must not be `None`")  # noqa: E501

        self._list_id = list_id

    @property
    def segment_opts(self):
        """Gets the segment_opts of this List5.  # noqa: E501


        :return: The segment_opts of this List5.  # noqa: E501
        :rtype: SegmentOptions1
        """
        return self._segment_opts

    @segment_opts.setter
    def segment_opts(self, segment_opts):
        """Sets the segment_opts of this List5.


        :param segment_opts: The segment_opts of this List5.  # noqa: E501
        :type: SegmentOptions1
        """

        self._segment_opts = segment_opts

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
        if issubclass(List5, dict):
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
        if not isinstance(other, List5):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
