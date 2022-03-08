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


class AutomationTrigger1(object):
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
        'workflow_type': 'str'
    }

    attribute_map = {
        'workflow_type': 'workflow_type'
    }

    def __init__(self, workflow_type=None):  # noqa: E501
        """AutomationTrigger1 - a model defined in Swagger"""  # noqa: E501

        self._workflow_type = None
        self.discriminator = None

        self.workflow_type = workflow_type

    @property
    def workflow_type(self):
        """Gets the workflow_type of this AutomationTrigger1.  # noqa: E501

        The type of Automation workflow. Currently only supports 'abandonedCart'.  # noqa: E501

        :return: The workflow_type of this AutomationTrigger1.  # noqa: E501
        :rtype: str
        """
        return self._workflow_type

    @workflow_type.setter
    def workflow_type(self, workflow_type):
        """Sets the workflow_type of this AutomationTrigger1.

        The type of Automation workflow. Currently only supports 'abandonedCart'.  # noqa: E501

        :param workflow_type: The workflow_type of this AutomationTrigger1.  # noqa: E501
        :type: str
        """
        if workflow_type is None:
            raise ValueError("Invalid value for `workflow_type`, must not be `None`")  # noqa: E501

        self._workflow_type = workflow_type

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
        if issubclass(AutomationTrigger1, dict):
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
        if not isinstance(other, AutomationTrigger1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other