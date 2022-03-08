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


class EcommerceProductImage(object):
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
        'id': 'str',
        'url': 'str',
        'variant_ids': 'list[str]',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'url': 'url',
        'variant_ids': 'variant_ids',
        'links': '_links'
    }

    def __init__(self, id=None, url=None, variant_ids=None, links=None):  # noqa: E501
        """EcommerceProductImage - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._url = None
        self._variant_ids = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if url is not None:
            self.url = url
        if variant_ids is not None:
            self.variant_ids = variant_ids
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this EcommerceProductImage.  # noqa: E501

        A unique identifier for the product image.  # noqa: E501

        :return: The id of this EcommerceProductImage.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcommerceProductImage.

        A unique identifier for the product image.  # noqa: E501

        :param id: The id of this EcommerceProductImage.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def url(self):
        """Gets the url of this EcommerceProductImage.  # noqa: E501

        The URL for a product image.  # noqa: E501

        :return: The url of this EcommerceProductImage.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EcommerceProductImage.

        The URL for a product image.  # noqa: E501

        :param url: The url of this EcommerceProductImage.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def variant_ids(self):
        """Gets the variant_ids of this EcommerceProductImage.  # noqa: E501

        The list of product variants using the image.  # noqa: E501

        :return: The variant_ids of this EcommerceProductImage.  # noqa: E501
        :rtype: list[str]
        """
        return self._variant_ids

    @variant_ids.setter
    def variant_ids(self, variant_ids):
        """Sets the variant_ids of this EcommerceProductImage.

        The list of product variants using the image.  # noqa: E501

        :param variant_ids: The variant_ids of this EcommerceProductImage.  # noqa: E501
        :type: list[str]
        """

        self._variant_ids = variant_ids

    @property
    def links(self):
        """Gets the links of this EcommerceProductImage.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this EcommerceProductImage.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EcommerceProductImage.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this EcommerceProductImage.  # noqa: E501
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
        if issubclass(EcommerceProductImage, dict):
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
        if not isinstance(other, EcommerceProductImage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
