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


class SegmentOptions1(object):
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
        'saved_segment_id': 'int',
        'prebuilt_segment_id': 'str',
        'match': 'str',
        'conditions': 'list[object]'
    }

    attribute_map = {
        'saved_segment_id': 'saved_segment_id',
        'prebuilt_segment_id': 'prebuilt_segment_id',
        'match': 'match',
        'conditions': 'conditions'
    }

    def __init__(self, saved_segment_id=None, prebuilt_segment_id=None, match=None, conditions=None):  # noqa: E501
        """SegmentOptions1 - a model defined in Swagger"""  # noqa: E501

        self._saved_segment_id = None
        self._prebuilt_segment_id = None
        self._match = None
        self._conditions = None
        self.discriminator = None

        if saved_segment_id is not None:
            self.saved_segment_id = saved_segment_id
        if prebuilt_segment_id is not None:
            self.prebuilt_segment_id = prebuilt_segment_id
        if match is not None:
            self.match = match
        if conditions is not None:
            self.conditions = conditions

    @property
    def saved_segment_id(self):
        """Gets the saved_segment_id of this SegmentOptions1.  # noqa: E501

        The id for an existing saved segment.  # noqa: E501

        :return: The saved_segment_id of this SegmentOptions1.  # noqa: E501
        :rtype: int
        """
        return self._saved_segment_id

    @saved_segment_id.setter
    def saved_segment_id(self, saved_segment_id):
        """Sets the saved_segment_id of this SegmentOptions1.

        The id for an existing saved segment.  # noqa: E501

        :param saved_segment_id: The saved_segment_id of this SegmentOptions1.  # noqa: E501
        :type: int
        """

        self._saved_segment_id = saved_segment_id

    @property
    def prebuilt_segment_id(self):
        """Gets the prebuilt_segment_id of this SegmentOptions1.  # noqa: E501

        The prebuilt segment id, if a prebuilt segment has been designated for this campaign.  # noqa: E501

        :return: The prebuilt_segment_id of this SegmentOptions1.  # noqa: E501
        :rtype: str
        """
        return self._prebuilt_segment_id

    @prebuilt_segment_id.setter
    def prebuilt_segment_id(self, prebuilt_segment_id):
        """Sets the prebuilt_segment_id of this SegmentOptions1.

        The prebuilt segment id, if a prebuilt segment has been designated for this campaign.  # noqa: E501

        :param prebuilt_segment_id: The prebuilt_segment_id of this SegmentOptions1.  # noqa: E501
        :type: str
        """

        self._prebuilt_segment_id = prebuilt_segment_id

    @property
    def match(self):
        """Gets the match of this SegmentOptions1.  # noqa: E501

        Segment match type.  # noqa: E501

        :return: The match of this SegmentOptions1.  # noqa: E501
        :rtype: str
        """
        return self._match

    @match.setter
    def match(self, match):
        """Sets the match of this SegmentOptions1.

        Segment match type.  # noqa: E501

        :param match: The match of this SegmentOptions1.  # noqa: E501
        :type: str
        """
        allowed_values = ["any", "all"]  # noqa: E501
        if match not in allowed_values:
            raise ValueError(
                "Invalid value for `match` ({0}), must be one of {1}"  # noqa: E501
                .format(match, allowed_values)
            )

        self._match = match

    @property
    def conditions(self):
        """Gets the conditions of this SegmentOptions1.  # noqa: E501

        Segment match conditions. There are multiple possible types, see the [condition types documentation](https://mailchimp.com/developer/marketing/docs/alternative-schemas/#segment-condition-schemas).  # noqa: E501

        :return: The conditions of this SegmentOptions1.  # noqa: E501
        :rtype: list[object]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this SegmentOptions1.

        Segment match conditions. There are multiple possible types, see the [condition types documentation](https://mailchimp.com/developer/marketing/docs/alternative-schemas/#segment-condition-schemas).  # noqa: E501

        :param conditions: The conditions of this SegmentOptions1.  # noqa: E501
        :type: list[object]
        """

        self._conditions = conditions

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
        if issubclass(SegmentOptions1, dict):
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
        if not isinstance(other, SegmentOptions1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other