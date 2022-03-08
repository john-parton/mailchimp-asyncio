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


class DailyClicksAndVisitsDataClicks(object):
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
        '_date': 'str',
        'val': 'int'
    }

    attribute_map = {
        '_date': 'date',
        'val': 'val'
    }

    def __init__(self, _date=None, val=None):  # noqa: E501
        """DailyClicksAndVisitsDataClicks - a model defined in Swagger"""  # noqa: E501

        self.__date = None
        self._val = None
        self.discriminator = None

        if _date is not None:
            self._date = _date
        if val is not None:
            self.val = val

    @property
    def _date(self):
        """Gets the _date of this DailyClicksAndVisitsDataClicks.  # noqa: E501


        :return: The _date of this DailyClicksAndVisitsDataClicks.  # noqa: E501
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this DailyClicksAndVisitsDataClicks.


        :param _date: The _date of this DailyClicksAndVisitsDataClicks.  # noqa: E501
        :type: str
        """

        self.__date = _date

    @property
    def val(self):
        """Gets the val of this DailyClicksAndVisitsDataClicks.  # noqa: E501


        :return: The val of this DailyClicksAndVisitsDataClicks.  # noqa: E501
        :rtype: int
        """
        return self._val

    @val.setter
    def val(self, val):
        """Sets the val of this DailyClicksAndVisitsDataClicks.


        :param val: The val of this DailyClicksAndVisitsDataClicks.  # noqa: E501
        :type: int
        """

        self._val = val

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
        if issubclass(DailyClicksAndVisitsDataClicks, dict):
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
        if not isinstance(other, DailyClicksAndVisitsDataClicks):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other