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


class EcommercePromoRule(object):
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
        'title': 'str',
        'description': 'str',
        'starts_at': 'datetime',
        'ends_at': 'str',
        'amount': 'float',
        'type': 'str',
        'target': 'str',
        'enabled': 'bool',
        'created_at_foreign': 'datetime',
        'updated_at_foreign': 'datetime',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'title': 'title',
        'description': 'description',
        'starts_at': 'starts_at',
        'ends_at': 'ends_at',
        'amount': 'amount',
        'type': 'type',
        'target': 'target',
        'enabled': 'enabled',
        'created_at_foreign': 'created_at_foreign',
        'updated_at_foreign': 'updated_at_foreign',
        'links': '_links'
    }

    def __init__(self, id=None, title=None, description=None, starts_at=None, ends_at=None, amount=None, type=None, target=None, enabled=None, created_at_foreign=None, updated_at_foreign=None, links=None):  # noqa: E501
        """EcommercePromoRule - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._title = None
        self._description = None
        self._starts_at = None
        self._ends_at = None
        self._amount = None
        self._type = None
        self._target = None
        self._enabled = None
        self._created_at_foreign = None
        self._updated_at_foreign = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if title is not None:
            self.title = title
        if description is not None:
            self.description = description
        if starts_at is not None:
            self.starts_at = starts_at
        if ends_at is not None:
            self.ends_at = ends_at
        if amount is not None:
            self.amount = amount
        if type is not None:
            self.type = type
        if target is not None:
            self.target = target
        if enabled is not None:
            self.enabled = enabled
        if created_at_foreign is not None:
            self.created_at_foreign = created_at_foreign
        if updated_at_foreign is not None:
            self.updated_at_foreign = updated_at_foreign
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this EcommercePromoRule.  # noqa: E501

        A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.  # noqa: E501

        :return: The id of this EcommercePromoRule.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcommercePromoRule.

        A unique identifier for the promo rule. If Ecommerce platform does not support promo rule, use promo code id as promo rule id. Restricted to UTF-8 characters with max length 50.  # noqa: E501

        :param id: The id of this EcommercePromoRule.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def title(self):
        """Gets the title of this EcommercePromoRule.  # noqa: E501

        The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.  # noqa: E501

        :return: The title of this EcommercePromoRule.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this EcommercePromoRule.

        The title that will show up in promotion campaign. Restricted to UTF-8 characters with max length of 100 bytes.  # noqa: E501

        :param title: The title of this EcommercePromoRule.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def description(self):
        """Gets the description of this EcommercePromoRule.  # noqa: E501

        The description of a promotion restricted to UTF-8 characters with max length 255.  # noqa: E501

        :return: The description of this EcommercePromoRule.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this EcommercePromoRule.

        The description of a promotion restricted to UTF-8 characters with max length 255.  # noqa: E501

        :param description: The description of this EcommercePromoRule.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def starts_at(self):
        """Gets the starts_at of this EcommercePromoRule.  # noqa: E501

        The date and time when the promotion is in effect in ISO 8601 format.  # noqa: E501

        :return: The starts_at of this EcommercePromoRule.  # noqa: E501
        :rtype: datetime
        """
        return self._starts_at

    @starts_at.setter
    def starts_at(self, starts_at):
        """Sets the starts_at of this EcommercePromoRule.

        The date and time when the promotion is in effect in ISO 8601 format.  # noqa: E501

        :param starts_at: The starts_at of this EcommercePromoRule.  # noqa: E501
        :type: datetime
        """

        self._starts_at = starts_at

    @property
    def ends_at(self):
        """Gets the ends_at of this EcommercePromoRule.  # noqa: E501

        The date and time when the promotion ends. Must be after starts_at and in ISO 8601 format.  # noqa: E501

        :return: The ends_at of this EcommercePromoRule.  # noqa: E501
        :rtype: str
        """
        return self._ends_at

    @ends_at.setter
    def ends_at(self, ends_at):
        """Sets the ends_at of this EcommercePromoRule.

        The date and time when the promotion ends. Must be after starts_at and in ISO 8601 format.  # noqa: E501

        :param ends_at: The ends_at of this EcommercePromoRule.  # noqa: E501
        :type: str
        """

        self._ends_at = ends_at

    @property
    def amount(self):
        """Gets the amount of this EcommercePromoRule.  # noqa: E501

        The amount of the promo code discount. If 'type' is 'fixed', the amount is treated as a monetary value. If 'type' is 'percentage', amount must be a decimal value between 0.0 and 1.0, inclusive.  # noqa: E501

        :return: The amount of this EcommercePromoRule.  # noqa: E501
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this EcommercePromoRule.

        The amount of the promo code discount. If 'type' is 'fixed', the amount is treated as a monetary value. If 'type' is 'percentage', amount must be a decimal value between 0.0 and 1.0, inclusive.  # noqa: E501

        :param amount: The amount of this EcommercePromoRule.  # noqa: E501
        :type: float
        """

        self._amount = amount

    @property
    def type(self):
        """Gets the type of this EcommercePromoRule.  # noqa: E501

        Type of discount. For free shipping set type to fixed.  # noqa: E501

        :return: The type of this EcommercePromoRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EcommercePromoRule.

        Type of discount. For free shipping set type to fixed.  # noqa: E501

        :param type: The type of this EcommercePromoRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["fixed", "percentage"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def target(self):
        """Gets the target of this EcommercePromoRule.  # noqa: E501

        The target that the discount applies to.  # noqa: E501

        :return: The target of this EcommercePromoRule.  # noqa: E501
        :rtype: str
        """
        return self._target

    @target.setter
    def target(self, target):
        """Sets the target of this EcommercePromoRule.

        The target that the discount applies to.  # noqa: E501

        :param target: The target of this EcommercePromoRule.  # noqa: E501
        :type: str
        """
        allowed_values = ["per_item", "total", "shipping"]  # noqa: E501
        if target not in allowed_values:
            raise ValueError(
                "Invalid value for `target` ({0}), must be one of {1}"  # noqa: E501
                .format(target, allowed_values)
            )

        self._target = target

    @property
    def enabled(self):
        """Gets the enabled of this EcommercePromoRule.  # noqa: E501

        Whether the promo rule is currently enabled.  # noqa: E501

        :return: The enabled of this EcommercePromoRule.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this EcommercePromoRule.

        Whether the promo rule is currently enabled.  # noqa: E501

        :param enabled: The enabled of this EcommercePromoRule.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def created_at_foreign(self):
        """Gets the created_at_foreign of this EcommercePromoRule.  # noqa: E501

        The date and time the promotion was created in ISO 8601 format.  # noqa: E501

        :return: The created_at_foreign of this EcommercePromoRule.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at_foreign

    @created_at_foreign.setter
    def created_at_foreign(self, created_at_foreign):
        """Sets the created_at_foreign of this EcommercePromoRule.

        The date and time the promotion was created in ISO 8601 format.  # noqa: E501

        :param created_at_foreign: The created_at_foreign of this EcommercePromoRule.  # noqa: E501
        :type: datetime
        """

        self._created_at_foreign = created_at_foreign

    @property
    def updated_at_foreign(self):
        """Gets the updated_at_foreign of this EcommercePromoRule.  # noqa: E501

        The date and time the promotion was updated in ISO 8601 format.  # noqa: E501

        :return: The updated_at_foreign of this EcommercePromoRule.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at_foreign

    @updated_at_foreign.setter
    def updated_at_foreign(self, updated_at_foreign):
        """Sets the updated_at_foreign of this EcommercePromoRule.

        The date and time the promotion was updated in ISO 8601 format.  # noqa: E501

        :param updated_at_foreign: The updated_at_foreign of this EcommercePromoRule.  # noqa: E501
        :type: datetime
        """

        self._updated_at_foreign = updated_at_foreign

    @property
    def links(self):
        """Gets the links of this EcommercePromoRule.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this EcommercePromoRule.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EcommercePromoRule.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this EcommercePromoRule.  # noqa: E501
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
        if issubclass(EcommercePromoRule, dict):
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
        if not isinstance(other, EcommercePromoRule):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
