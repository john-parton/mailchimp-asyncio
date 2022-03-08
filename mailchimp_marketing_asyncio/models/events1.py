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


class Events1(object):
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
        'subscribe': 'bool',
        'unsubscribe': 'bool',
        'profile': 'bool',
        'cleaned': 'bool',
        'upemail': 'bool',
        'campaign': 'bool'
    }

    attribute_map = {
        'subscribe': 'subscribe',
        'unsubscribe': 'unsubscribe',
        'profile': 'profile',
        'cleaned': 'cleaned',
        'upemail': 'upemail',
        'campaign': 'campaign'
    }

    def __init__(self, subscribe=None, unsubscribe=None, profile=None, cleaned=None, upemail=None, campaign=None):  # noqa: E501
        """Events1 - a model defined in Swagger"""  # noqa: E501

        self._subscribe = None
        self._unsubscribe = None
        self._profile = None
        self._cleaned = None
        self._upemail = None
        self._campaign = None
        self.discriminator = None

        if subscribe is not None:
            self.subscribe = subscribe
        if unsubscribe is not None:
            self.unsubscribe = unsubscribe
        if profile is not None:
            self.profile = profile
        if cleaned is not None:
            self.cleaned = cleaned
        if upemail is not None:
            self.upemail = upemail
        if campaign is not None:
            self.campaign = campaign

    @property
    def subscribe(self):
        """Gets the subscribe of this Events1.  # noqa: E501

        Whether the webhook is triggered when a list subscriber is added.  # noqa: E501

        :return: The subscribe of this Events1.  # noqa: E501
        :rtype: bool
        """
        return self._subscribe

    @subscribe.setter
    def subscribe(self, subscribe):
        """Sets the subscribe of this Events1.

        Whether the webhook is triggered when a list subscriber is added.  # noqa: E501

        :param subscribe: The subscribe of this Events1.  # noqa: E501
        :type: bool
        """

        self._subscribe = subscribe

    @property
    def unsubscribe(self):
        """Gets the unsubscribe of this Events1.  # noqa: E501

        Whether the webhook is triggered when a list member unsubscribes.  # noqa: E501

        :return: The unsubscribe of this Events1.  # noqa: E501
        :rtype: bool
        """
        return self._unsubscribe

    @unsubscribe.setter
    def unsubscribe(self, unsubscribe):
        """Sets the unsubscribe of this Events1.

        Whether the webhook is triggered when a list member unsubscribes.  # noqa: E501

        :param unsubscribe: The unsubscribe of this Events1.  # noqa: E501
        :type: bool
        """

        self._unsubscribe = unsubscribe

    @property
    def profile(self):
        """Gets the profile of this Events1.  # noqa: E501

        Whether the webhook is triggered when a subscriber's profile is updated.  # noqa: E501

        :return: The profile of this Events1.  # noqa: E501
        :rtype: bool
        """
        return self._profile

    @profile.setter
    def profile(self, profile):
        """Sets the profile of this Events1.

        Whether the webhook is triggered when a subscriber's profile is updated.  # noqa: E501

        :param profile: The profile of this Events1.  # noqa: E501
        :type: bool
        """

        self._profile = profile

    @property
    def cleaned(self):
        """Gets the cleaned of this Events1.  # noqa: E501

        Whether the webhook is triggered when a subscriber's email address is cleaned from the list.  # noqa: E501

        :return: The cleaned of this Events1.  # noqa: E501
        :rtype: bool
        """
        return self._cleaned

    @cleaned.setter
    def cleaned(self, cleaned):
        """Sets the cleaned of this Events1.

        Whether the webhook is triggered when a subscriber's email address is cleaned from the list.  # noqa: E501

        :param cleaned: The cleaned of this Events1.  # noqa: E501
        :type: bool
        """

        self._cleaned = cleaned

    @property
    def upemail(self):
        """Gets the upemail of this Events1.  # noqa: E501

        Whether the webhook is triggered when a subscriber's email address is changed.  # noqa: E501

        :return: The upemail of this Events1.  # noqa: E501
        :rtype: bool
        """
        return self._upemail

    @upemail.setter
    def upemail(self, upemail):
        """Sets the upemail of this Events1.

        Whether the webhook is triggered when a subscriber's email address is changed.  # noqa: E501

        :param upemail: The upemail of this Events1.  # noqa: E501
        :type: bool
        """

        self._upemail = upemail

    @property
    def campaign(self):
        """Gets the campaign of this Events1.  # noqa: E501

        Whether the webhook is triggered when a campaign is sent or cancelled.  # noqa: E501

        :return: The campaign of this Events1.  # noqa: E501
        :rtype: bool
        """
        return self._campaign

    @campaign.setter
    def campaign(self, campaign):
        """Sets the campaign of this Events1.

        Whether the webhook is triggered when a campaign is sent or cancelled.  # noqa: E501

        :param campaign: The campaign of this Events1.  # noqa: E501
        :type: bool
        """

        self._campaign = campaign

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
        if issubclass(Events1, dict):
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
        if not isinstance(other, Events1):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other