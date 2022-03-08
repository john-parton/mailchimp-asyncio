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


class ListLocation(object):
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
        'country': 'str',
        'cc': 'str',
        'percent': 'float',
        'total': 'int'
    }

    attribute_map = {
        'country': 'country',
        'cc': 'cc',
        'percent': 'percent',
        'total': 'total'
    }

    def __init__(self, country=None, cc=None, percent=None, total=None):  # noqa: E501
        """ListLocation - a model defined in Swagger"""  # noqa: E501

        self._country = None
        self._cc = None
        self._percent = None
        self._total = None
        self.discriminator = None

        if country is not None:
            self.country = country
        if cc is not None:
            self.cc = cc
        if percent is not None:
            self.percent = percent
        if total is not None:
            self.total = total

    @property
    def country(self):
        """Gets the country of this ListLocation.  # noqa: E501

        The name of the country.  # noqa: E501

        :return: The country of this ListLocation.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ListLocation.

        The name of the country.  # noqa: E501

        :param country: The country of this ListLocation.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def cc(self):
        """Gets the cc of this ListLocation.  # noqa: E501

        The ISO 3166 2 digit country code.  # noqa: E501

        :return: The cc of this ListLocation.  # noqa: E501
        :rtype: str
        """
        return self._cc

    @cc.setter
    def cc(self, cc):
        """Sets the cc of this ListLocation.

        The ISO 3166 2 digit country code.  # noqa: E501

        :param cc: The cc of this ListLocation.  # noqa: E501
        :type: str
        """

        self._cc = cc

    @property
    def percent(self):
        """Gets the percent of this ListLocation.  # noqa: E501

        The percent of subscribers in the country.  # noqa: E501

        :return: The percent of this ListLocation.  # noqa: E501
        :rtype: float
        """
        return self._percent

    @percent.setter
    def percent(self, percent):
        """Sets the percent of this ListLocation.

        The percent of subscribers in the country.  # noqa: E501

        :param percent: The percent of this ListLocation.  # noqa: E501
        :type: float
        """

        self._percent = percent

    @property
    def total(self):
        """Gets the total of this ListLocation.  # noqa: E501

        The total number of subscribers in the country.  # noqa: E501

        :return: The total of this ListLocation.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListLocation.

        The total number of subscribers in the country.  # noqa: E501

        :param total: The total of this ListLocation.  # noqa: E501
        :type: int
        """

        self._total = total

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
        if issubclass(ListLocation, dict):
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
        if not isinstance(other, ListLocation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
