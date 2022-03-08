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


class CollectionAuthorization(object):
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
        'may_create': 'bool',
        'max_instances': 'int',
        'current_total_instances': 'int'
    }

    attribute_map = {
        'may_create': 'may_create',
        'max_instances': 'max_instances',
        'current_total_instances': 'current_total_instances'
    }

    def __init__(self, may_create=None, max_instances=None, current_total_instances=None):  # noqa: E501
        """CollectionAuthorization - a model defined in Swagger"""  # noqa: E501

        self._may_create = None
        self._max_instances = None
        self._current_total_instances = None
        self.discriminator = None

        self.may_create = may_create
        self.max_instances = max_instances
        if current_total_instances is not None:
            self.current_total_instances = current_total_instances

    @property
    def may_create(self):
        """Gets the may_create of this CollectionAuthorization.  # noqa: E501

        May the user create additional instances of this resource?  # noqa: E501

        :return: The may_create of this CollectionAuthorization.  # noqa: E501
        :rtype: bool
        """
        return self._may_create

    @may_create.setter
    def may_create(self, may_create):
        """Sets the may_create of this CollectionAuthorization.

        May the user create additional instances of this resource?  # noqa: E501

        :param may_create: The may_create of this CollectionAuthorization.  # noqa: E501
        :type: bool
        """
        if may_create is None:
            raise ValueError("Invalid value for `may_create`, must not be `None`")  # noqa: E501

        self._may_create = may_create

    @property
    def max_instances(self):
        """Gets the max_instances of this CollectionAuthorization.  # noqa: E501

        How many total instances of this resource are allowed? This is independent of any filter conditions applied to the query. As a special case, -1 indicates unlimited.  # noqa: E501

        :return: The max_instances of this CollectionAuthorization.  # noqa: E501
        :rtype: int
        """
        return self._max_instances

    @max_instances.setter
    def max_instances(self, max_instances):
        """Sets the max_instances of this CollectionAuthorization.

        How many total instances of this resource are allowed? This is independent of any filter conditions applied to the query. As a special case, -1 indicates unlimited.  # noqa: E501

        :param max_instances: The max_instances of this CollectionAuthorization.  # noqa: E501
        :type: int
        """
        if max_instances is None:
            raise ValueError("Invalid value for `max_instances`, must not be `None`")  # noqa: E501

        self._max_instances = max_instances

    @property
    def current_total_instances(self):
        """Gets the current_total_instances of this CollectionAuthorization.  # noqa: E501

        How many total instances of this resource are already in use? This is independent of any filter conditions applied to the query. Value may be larger than max_instances. As a special case, -1 is returned when access is unlimited.  # noqa: E501

        :return: The current_total_instances of this CollectionAuthorization.  # noqa: E501
        :rtype: int
        """
        return self._current_total_instances

    @current_total_instances.setter
    def current_total_instances(self, current_total_instances):
        """Sets the current_total_instances of this CollectionAuthorization.

        How many total instances of this resource are already in use? This is independent of any filter conditions applied to the query. Value may be larger than max_instances. As a special case, -1 is returned when access is unlimited.  # noqa: E501

        :param current_total_instances: The current_total_instances of this CollectionAuthorization.  # noqa: E501
        :type: int
        """

        self._current_total_instances = current_total_instances

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
        if issubclass(CollectionAuthorization, dict):
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
        if not isinstance(other, CollectionAuthorization):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other