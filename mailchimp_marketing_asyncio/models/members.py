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


class Members(object):
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
        'exact_matches': 'ExactMatches',
        'full_search': 'PartialMatches',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'exact_matches': 'exact_matches',
        'full_search': 'full_search',
        'links': '_links'
    }

    def __init__(self, exact_matches=None, full_search=None, links=None):  # noqa: E501
        """Members - a model defined in Swagger"""  # noqa: E501

        self._exact_matches = None
        self._full_search = None
        self._links = None
        self.discriminator = None

        if exact_matches is not None:
            self.exact_matches = exact_matches
        if full_search is not None:
            self.full_search = full_search
        if links is not None:
            self.links = links

    @property
    def exact_matches(self):
        """Gets the exact_matches of this Members.  # noqa: E501


        :return: The exact_matches of this Members.  # noqa: E501
        :rtype: ExactMatches
        """
        return self._exact_matches

    @exact_matches.setter
    def exact_matches(self, exact_matches):
        """Sets the exact_matches of this Members.


        :param exact_matches: The exact_matches of this Members.  # noqa: E501
        :type: ExactMatches
        """

        self._exact_matches = exact_matches

    @property
    def full_search(self):
        """Gets the full_search of this Members.  # noqa: E501


        :return: The full_search of this Members.  # noqa: E501
        :rtype: PartialMatches
        """
        return self._full_search

    @full_search.setter
    def full_search(self, full_search):
        """Sets the full_search of this Members.


        :param full_search: The full_search of this Members.  # noqa: E501
        :type: PartialMatches
        """

        self._full_search = full_search

    @property
    def links(self):
        """Gets the links of this Members.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this Members.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Members.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this Members.  # noqa: E501
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
        if issubclass(Members, dict):
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
        if not isinstance(other, Members):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other