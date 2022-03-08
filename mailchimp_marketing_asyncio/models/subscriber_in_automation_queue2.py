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


class SubscriberInAutomationQueue2(object):
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
        'workflow_id': 'str',
        'email_id': 'str',
        'list_id': 'str',
        'list_is_active': 'bool',
        'email_address': 'str',
        'next_send': 'datetime',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'workflow_id': 'workflow_id',
        'email_id': 'email_id',
        'list_id': 'list_id',
        'list_is_active': 'list_is_active',
        'email_address': 'email_address',
        'next_send': 'next_send',
        'links': '_links'
    }

    def __init__(self, id=None, workflow_id=None, email_id=None, list_id=None, list_is_active=None, email_address=None, next_send=None, links=None):  # noqa: E501
        """SubscriberInAutomationQueue2 - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._workflow_id = None
        self._email_id = None
        self._list_id = None
        self._list_is_active = None
        self._email_address = None
        self._next_send = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if workflow_id is not None:
            self.workflow_id = workflow_id
        if email_id is not None:
            self.email_id = email_id
        if list_id is not None:
            self.list_id = list_id
        if list_is_active is not None:
            self.list_is_active = list_is_active
        if email_address is not None:
            self.email_address = email_address
        if next_send is not None:
            self.next_send = next_send
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this SubscriberInAutomationQueue2.  # noqa: E501

        The MD5 hash of the lowercase version of the list member's email address.  # noqa: E501

        :return: The id of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriberInAutomationQueue2.

        The MD5 hash of the lowercase version of the list member's email address.  # noqa: E501

        :param id: The id of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def workflow_id(self):
        """Gets the workflow_id of this SubscriberInAutomationQueue2.  # noqa: E501

        A string that uniquely identifies an Automation workflow.  # noqa: E501

        :return: The workflow_id of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: str
        """
        return self._workflow_id

    @workflow_id.setter
    def workflow_id(self, workflow_id):
        """Sets the workflow_id of this SubscriberInAutomationQueue2.

        A string that uniquely identifies an Automation workflow.  # noqa: E501

        :param workflow_id: The workflow_id of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: str
        """

        self._workflow_id = workflow_id

    @property
    def email_id(self):
        """Gets the email_id of this SubscriberInAutomationQueue2.  # noqa: E501

        A string that uniquely identifies an email in an Automation workflow.  # noqa: E501

        :return: The email_id of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: str
        """
        return self._email_id

    @email_id.setter
    def email_id(self, email_id):
        """Sets the email_id of this SubscriberInAutomationQueue2.

        A string that uniquely identifies an email in an Automation workflow.  # noqa: E501

        :param email_id: The email_id of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: str
        """

        self._email_id = email_id

    @property
    def list_id(self):
        """Gets the list_id of this SubscriberInAutomationQueue2.  # noqa: E501

        A string that uniquely identifies a list.  # noqa: E501

        :return: The list_id of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this SubscriberInAutomationQueue2.

        A string that uniquely identifies a list.  # noqa: E501

        :param list_id: The list_id of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def list_is_active(self):
        """Gets the list_is_active of this SubscriberInAutomationQueue2.  # noqa: E501

        The status of the list used, namely if it's deleted or disabled.  # noqa: E501

        :return: The list_is_active of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: bool
        """
        return self._list_is_active

    @list_is_active.setter
    def list_is_active(self, list_is_active):
        """Sets the list_is_active of this SubscriberInAutomationQueue2.

        The status of the list used, namely if it's deleted or disabled.  # noqa: E501

        :param list_is_active: The list_is_active of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: bool
        """

        self._list_is_active = list_is_active

    @property
    def email_address(self):
        """Gets the email_address of this SubscriberInAutomationQueue2.  # noqa: E501

        The list member's email address.  # noqa: E501

        :return: The email_address of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this SubscriberInAutomationQueue2.

        The list member's email address.  # noqa: E501

        :param email_address: The email_address of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def next_send(self):
        """Gets the next_send of this SubscriberInAutomationQueue2.  # noqa: E501

        The date and time of the next send for the workflow email in ISO 8601 format.  # noqa: E501

        :return: The next_send of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: datetime
        """
        return self._next_send

    @next_send.setter
    def next_send(self, next_send):
        """Sets the next_send of this SubscriberInAutomationQueue2.

        The date and time of the next send for the workflow email in ISO 8601 format.  # noqa: E501

        :param next_send: The next_send of this SubscriberInAutomationQueue2.  # noqa: E501
        :type: datetime
        """

        self._next_send = next_send

    @property
    def links(self):
        """Gets the links of this SubscriberInAutomationQueue2.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this SubscriberInAutomationQueue2.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SubscriberInAutomationQueue2.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this SubscriberInAutomationQueue2.  # noqa: E501
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
        if issubclass(SubscriberInAutomationQueue2, dict):
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
        if not isinstance(other, SubscriberInAutomationQueue2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
