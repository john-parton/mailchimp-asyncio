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


class EcommerceProduct2(object):
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
        'title': 'str',
        'handle': 'str',
        'url': 'str',
        'description': 'str',
        'type': 'str',
        'vendor': 'str',
        'image_url': 'str',
        'variants': 'list[EcommerceProductVariant2]',
        'images': 'list[EcommerceProductImage2]',
        'published_at_foreign': 'datetime'
    }

    attribute_map = {
        'title': 'title',
        'handle': 'handle',
        'url': 'url',
        'description': 'description',
        'type': 'type',
        'vendor': 'vendor',
        'image_url': 'image_url',
        'variants': 'variants',
        'images': 'images',
        'published_at_foreign': 'published_at_foreign'
    }

    def __init__(self, title=None, handle=None, url=None, description=None, type=None, vendor=None, image_url=None, variants=None, images=None, published_at_foreign=None):  # noqa: E501
        """EcommerceProduct2 - a model defined in Swagger"""  # noqa: E501

        self._title = None
        self._handle = None
        self._url = None
        self._description = None
        self._type = None
        self._vendor = None
        self._image_url = None
        self._variants = None
        self._images = None
        self._published_at_foreign = None
        self.discriminator = None

        if title is not None:
            self.title = title
        if handle is not None:
            self.handle = handle
        if url is not None:
            self.url = url
        if description is not None:
            self.description = description
        if type is not None:
            self.type = type
        if vendor is not None:
            self.vendor = vendor
        if image_url is not None:
            self.image_url = image_url
        if variants is not None:
            self.variants = variants
        if images is not None:
            self.images = images
        if published_at_foreign is not None:
            self.published_at_foreign = published_at_foreign

    @property
    def title(self):
        """Gets the title of this EcommerceProduct2.  # noqa: E501

        The title of a product.  # noqa: E501

        :return: The title of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EcommerceProduct2.

        The title of a product.  # noqa: E501

        :param title: The title of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def handle(self):
        """Gets the handle of this EcommerceProduct2.  # noqa: E501

        The handle of a product.  # noqa: E501

        :return: The handle of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._handle

    @handle.setter
    def handle(self, handle):
        """Sets the handle of this EcommerceProduct2.

        The handle of a product.  # noqa: E501

        :param handle: The handle of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._handle = handle

    @property
    def url(self):
        """Gets the url of this EcommerceProduct2.  # noqa: E501

        The URL for a product.  # noqa: E501

        :return: The url of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this EcommerceProduct2.

        The URL for a product.  # noqa: E501

        :param url: The url of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def description(self):
        """Gets the description of this EcommerceProduct2.  # noqa: E501

        The description of a product.  # noqa: E501

        :return: The description of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EcommerceProduct2.

        The description of a product.  # noqa: E501

        :param description: The description of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def type(self):
        """Gets the type of this EcommerceProduct2.  # noqa: E501

        The type of product.  # noqa: E501

        :return: The type of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EcommerceProduct2.

        The type of product.  # noqa: E501

        :param type: The type of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def vendor(self):
        """Gets the vendor of this EcommerceProduct2.  # noqa: E501

        The vendor for a product.  # noqa: E501

        :return: The vendor of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._vendor

    @vendor.setter
    def vendor(self, vendor):
        """Sets the vendor of this EcommerceProduct2.

        The vendor for a product.  # noqa: E501

        :param vendor: The vendor of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._vendor = vendor

    @property
    def image_url(self):
        """Gets the image_url of this EcommerceProduct2.  # noqa: E501

        The image URL for a product.  # noqa: E501

        :return: The image_url of this EcommerceProduct2.  # noqa: E501
        :rtype: str
        """
        return self._image_url

    @image_url.setter
    def image_url(self, image_url):
        """Sets the image_url of this EcommerceProduct2.

        The image URL for a product.  # noqa: E501

        :param image_url: The image_url of this EcommerceProduct2.  # noqa: E501
        :type: str
        """

        self._image_url = image_url

    @property
    def variants(self):
        """Gets the variants of this EcommerceProduct2.  # noqa: E501

        An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.  # noqa: E501

        :return: The variants of this EcommerceProduct2.  # noqa: E501
        :rtype: list[EcommerceProductVariant2]
        """
        return self._variants

    @variants.setter
    def variants(self, variants):
        """Sets the variants of this EcommerceProduct2.

        An array of the product's variants. At least one variant is required for each product. A variant can use the same `id` and `title` as the parent product.  # noqa: E501

        :param variants: The variants of this EcommerceProduct2.  # noqa: E501
        :type: list[EcommerceProductVariant2]
        """

        self._variants = variants

    @property
    def images(self):
        """Gets the images of this EcommerceProduct2.  # noqa: E501

        An array of the product's images.  # noqa: E501

        :return: The images of this EcommerceProduct2.  # noqa: E501
        :rtype: list[EcommerceProductImage2]
        """
        return self._images

    @images.setter
    def images(self, images):
        """Sets the images of this EcommerceProduct2.

        An array of the product's images.  # noqa: E501

        :param images: The images of this EcommerceProduct2.  # noqa: E501
        :type: list[EcommerceProductImage2]
        """

        self._images = images

    @property
    def published_at_foreign(self):
        """Gets the published_at_foreign of this EcommerceProduct2.  # noqa: E501

        The date and time the product was published in ISO 8601 format.  # noqa: E501

        :return: The published_at_foreign of this EcommerceProduct2.  # noqa: E501
        :rtype: datetime
        """
        return self._published_at_foreign

    @published_at_foreign.setter
    def published_at_foreign(self, published_at_foreign):
        """Sets the published_at_foreign of this EcommerceProduct2.

        The date and time the product was published in ISO 8601 format.  # noqa: E501

        :param published_at_foreign: The published_at_foreign of this EcommerceProduct2.  # noqa: E501
        :type: datetime
        """

        self._published_at_foreign = published_at_foreign

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
        if issubclass(EcommerceProduct2, dict):
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
        if not isinstance(other, EcommerceProduct2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
