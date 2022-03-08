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


class Unsubscribes(object):
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
        'unsubscribes': 'list[Unsubscribes]',
        'campaign_id': 'str',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'unsubscribes': 'unsubscribes',
        'campaign_id': 'campaign_id',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, unsubscribes=None, campaign_id=None, total_items=None, links=None):  # noqa: E501
        """Unsubscribes - a model defined in Swagger"""  # noqa: E501

        self._unsubscribes = None
        self._campaign_id = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if unsubscribes is not None:
            self.unsubscribes = unsubscribes
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def unsubscribes(self):
        """Gets the unsubscribes of this Unsubscribes.  # noqa: E501

        An array of objects, each representing a member who unsubscribed from a campaign.  # noqa: E501

        :return: The unsubscribes of this Unsubscribes.  # noqa: E501
        :rtype: list[Unsubscribes]
        """
        return self._unsubscribes

    @unsubscribes.setter
    def unsubscribes(self, unsubscribes):
        """Sets the unsubscribes of this Unsubscribes.

        An array of objects, each representing a member who unsubscribed from a campaign.  # noqa: E501

        :param unsubscribes: The unsubscribes of this Unsubscribes.  # noqa: E501
        :type: list[Unsubscribes]
        """

        self._unsubscribes = unsubscribes

    @property
    def campaign_id(self):
        """Gets the campaign_id of this Unsubscribes.  # noqa: E501

        The campaign id.  # noqa: E501

        :return: The campaign_id of this Unsubscribes.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this Unsubscribes.

        The campaign id.  # noqa: E501

        :param campaign_id: The campaign_id of this Unsubscribes.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def total_items(self):
        """Gets the total_items of this Unsubscribes.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this Unsubscribes.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this Unsubscribes.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this Unsubscribes.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this Unsubscribes.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this Unsubscribes.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Unsubscribes.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this Unsubscribes.  # noqa: E501
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
        if issubclass(Unsubscribes, dict):
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
        if not isinstance(other, Unsubscribes):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
