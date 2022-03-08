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


class CampaignReports1(object):
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
        'reports': 'list[CampaignReport]',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'reports': 'reports',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, reports=None, total_items=None, links=None):  # noqa: E501
        """CampaignReports1 - a model defined in Swagger"""  # noqa: E501

        self._reports = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if reports is not None:
            self.reports = reports
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def reports(self):
        """Gets the reports of this CampaignReports1.  # noqa: E501

        An array of objects, each representing a report resource.  # noqa: E501

        :return: The reports of this CampaignReports1.  # noqa: E501
        :rtype: list[CampaignReport]
        """
        return self._reports

    @reports.setter
    def reports(self, reports):
        """Sets the reports of this CampaignReports1.

        An array of objects, each representing a report resource.  # noqa: E501

        :param reports: The reports of this CampaignReports1.  # noqa: E501
        :type: list[CampaignReport]
        """

        self._reports = reports

    @property
    def total_items(self):
        """Gets the total_items of this CampaignReports1.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this CampaignReports1.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this CampaignReports1.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this CampaignReports1.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this CampaignReports1.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this CampaignReports1.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CampaignReports1.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this CampaignReports1.  # noqa: E501
        :type: list[ResourceLink]
        """

        self._links = links

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
        if issubclass(CampaignReports1, dict):
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
        if not isinstance(other, CampaignReports1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
