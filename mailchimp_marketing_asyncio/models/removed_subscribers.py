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


class RemovedSubscribers(object):
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
        'workflow_id': 'str',
        'subscribers': 'list[SubscriberRemovedFromAutomationWorkflow]',
        'total_items': 'int',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'workflow_id': 'workflow_id',
        'subscribers': 'subscribers',
        'total_items': 'total_items',
        'links': '_links'
    }

    def __init__(self, workflow_id=None, subscribers=None, total_items=None, links=None):  # noqa: E501
        """RemovedSubscribers - a model defined in Swagger"""  # noqa: E501

        self._workflow_id = None
        self._subscribers = None
        self._total_items = None
        self._links = None
        self.discriminator = None

        if workflow_id is not None:
            self.workflow_id = workflow_id
        if subscribers is not None:
            self.subscribers = subscribers
        if total_items is not None:
            self.total_items = total_items
        if links is not None:
            self.links = links

    @property
    def workflow_id(self):
        """Gets the workflow_id of this RemovedSubscribers.  # noqa: E501

        A string that uniquely identifies an Automation workflow.  # noqa: E501

        :return: The workflow_id of this RemovedSubscribers.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this RemovedSubscribers.

        A string that uniquely identifies an Automation workflow.  # noqa: E501

        :param workflow_id: The workflow_id of this RemovedSubscribers.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def subscribers(self):
        """Gets the subscribers of this RemovedSubscribers.  # noqa: E501

        An array of objects, each representing a subscriber who was removed from an Automation workflow.  # noqa: E501

        :return: The subscribers of this RemovedSubscribers.  # noqa: E501
        :rtype: list[SubscriberRemovedFromAutomationWorkflow]
        """
        return self._subscribers

    @subscribers.setter
    def subscribers(self, subscribers):
        """Sets the subscribers of this RemovedSubscribers.

        An array of objects, each representing a subscriber who was removed from an Automation workflow.  # noqa: E501

        :param subscribers: The subscribers of this RemovedSubscribers.  # noqa: E501
        :type: list[SubscriberRemovedFromAutomationWorkflow]
        """

        self._subscribers = subscribers

    @property
    def total_items(self):
        """Gets the total_items of this RemovedSubscribers.  # noqa: E501

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :return: The total_items of this RemovedSubscribers.  # noqa: E501
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """Sets the total_items of this RemovedSubscribers.

        The total number of items matching the query regardless of pagination.  # noqa: E501

        :param total_items: The total_items of this RemovedSubscribers.  # noqa: E501
        :type: int
        """

        self._total_items = total_items

    @property
    def links(self):
        """Gets the links of this RemovedSubscribers.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this RemovedSubscribers.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this RemovedSubscribers.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this RemovedSubscribers.  # noqa: E501
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
        if issubclass(RemovedSubscribers, dict):
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
        if not isinstance(other, RemovedSubscribers):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other