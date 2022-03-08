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


class EmailDomain(object):
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
        'domain': 'str',
        'emails_sent': 'int',
        'bounces': 'int',
        'opens': 'int',
        'clicks': 'int',
        'unsubs': 'int',
        'delivered': 'int',
        'emails_pct': 'float',
        'bounces_pct': 'float',
        'opens_pct': 'float',
        'clicks_pct': 'float',
        'unsubs_pct': 'float'
    }

    attribute_map = {
        'domain': 'domain',
        'emails_sent': 'emails_sent',
        'bounces': 'bounces',
        'opens': 'opens',
        'clicks': 'clicks',
        'unsubs': 'unsubs',
        'delivered': 'delivered',
        'emails_pct': 'emails_pct',
        'bounces_pct': 'bounces_pct',
        'opens_pct': 'opens_pct',
        'clicks_pct': 'clicks_pct',
        'unsubs_pct': 'unsubs_pct'
    }

    def __init__(self, domain=None, emails_sent=None, bounces=None, opens=None, clicks=None, unsubs=None, delivered=None, emails_pct=None, bounces_pct=None, opens_pct=None, clicks_pct=None, unsubs_pct=None):  # noqa: E501
        """EmailDomain - a model defined in Swagger"""  # noqa: E501

        self._domain = None
        self._emails_sent = None
        self._bounces = None
        self._opens = None
        self._clicks = None
        self._unsubs = None
        self._delivered = None
        self._emails_pct = None
        self._bounces_pct = None
        self._opens_pct = None
        self._clicks_pct = None
        self._unsubs_pct = None
        self.discriminator = None

        if domain is not None:
            self.domain = domain
        if emails_sent is not None:
            self.emails_sent = emails_sent
        if bounces is not None:
            self.bounces = bounces
        if opens is not None:
            self.opens = opens
        if clicks is not None:
            self.clicks = clicks
        if unsubs is not None:
            self.unsubs = unsubs
        if delivered is not None:
            self.delivered = delivered
        if emails_pct is not None:
            self.emails_pct = emails_pct
        if bounces_pct is not None:
            self.bounces_pct = bounces_pct
        if opens_pct is not None:
            self.opens_pct = opens_pct
        if clicks_pct is not None:
            self.clicks_pct = clicks_pct
        if unsubs_pct is not None:
            self.unsubs_pct = unsubs_pct

    @property
    def domain(self):
        """Gets the domain of this EmailDomain.  # noqa: E501

        The name of the domain (gmail.com, hotmail.com, yahoo.com).  # noqa: E501

        :return: The domain of this EmailDomain.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this EmailDomain.

        The name of the domain (gmail.com, hotmail.com, yahoo.com).  # noqa: E501

        :param domain: The domain of this EmailDomain.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def emails_sent(self):
        """Gets the emails_sent of this EmailDomain.  # noqa: E501

        The number of emails sent to that specific domain.  # noqa: E501

        :return: The emails_sent of this EmailDomain.  # noqa: E501
        :rtype: int
        """
        return self._emails_sent

    @emails_sent.setter
    def emails_sent(self, emails_sent):
        """Sets the emails_sent of this EmailDomain.

        The number of emails sent to that specific domain.  # noqa: E501

        :param emails_sent: The emails_sent of this EmailDomain.  # noqa: E501
        :type: int
        """

        self._emails_sent = emails_sent

    @property
    def bounces(self):
        """Gets the bounces of this EmailDomain.  # noqa: E501

        The number of bounces at a domain.  # noqa: E501

        :return: The bounces of this EmailDomain.  # noqa: E501
        :rtype: int
        """
        return self._bounces

    @bounces.setter
    def bounces(self, bounces):
        """Sets the bounces of this EmailDomain.

        The number of bounces at a domain.  # noqa: E501

        :param bounces: The bounces of this EmailDomain.  # noqa: E501
        :type: int
        """

        self._bounces = bounces

    @property
    def opens(self):
        """Gets the opens of this EmailDomain.  # noqa: E501

        The number of opens for a domain.  # noqa: E501

        :return: The opens of this EmailDomain.  # noqa: E501
        :rtype: int
        """
        return self._opens

    @opens.setter
    def opens(self, opens):
        """Sets the opens of this EmailDomain.

        The number of opens for a domain.  # noqa: E501

        :param opens: The opens of this EmailDomain.  # noqa: E501
        :type: int
        """

        self._opens = opens

    @property
    def clicks(self):
        """Gets the clicks of this EmailDomain.  # noqa: E501

        The number of clicks for a domain.  # noqa: E501

        :return: The clicks of this EmailDomain.  # noqa: E501
        :rtype: int
        """
        return self._clicks

    @clicks.setter
    def clicks(self, clicks):
        """Sets the clicks of this EmailDomain.

        The number of clicks for a domain.  # noqa: E501

        :param clicks: The clicks of this EmailDomain.  # noqa: E501
        :type: int
        """

        self._clicks = clicks

    @property
    def unsubs(self):
        """Gets the unsubs of this EmailDomain.  # noqa: E501

        The total number of unsubscribes for a domain.  # noqa: E501

        :return: The unsubs of this EmailDomain.  # noqa: E501
        :rtype: int
        """
        return self._unsubs

    @unsubs.setter
    def unsubs(self, unsubs):
        """Sets the unsubs of this EmailDomain.

        The total number of unsubscribes for a domain.  # noqa: E501

        :param unsubs: The unsubs of this EmailDomain.  # noqa: E501
        :type: int
        """

        self._unsubs = unsubs

    @property
    def delivered(self):
        """Gets the delivered of this EmailDomain.  # noqa: E501

        The number of successful deliveries for a domain.  # noqa: E501

        :return: The delivered of this EmailDomain.  # noqa: E501
        :rtype: int
        """
        return self._delivered

    @delivered.setter
    def delivered(self, delivered):
        """Sets the delivered of this EmailDomain.

        The number of successful deliveries for a domain.  # noqa: E501

        :param delivered: The delivered of this EmailDomain.  # noqa: E501
        :type: int
        """

        self._delivered = delivered

    @property
    def emails_pct(self):
        """Gets the emails_pct of this EmailDomain.  # noqa: E501

        The percentage of total emails that went to this domain.  # noqa: E501

        :return: The emails_pct of this EmailDomain.  # noqa: E501
        :rtype: float
        """
        return self._emails_pct

    @emails_pct.setter
    def emails_pct(self, emails_pct):
        """Sets the emails_pct of this EmailDomain.

        The percentage of total emails that went to this domain.  # noqa: E501

        :param emails_pct: The emails_pct of this EmailDomain.  # noqa: E501
        :type: float
        """

        self._emails_pct = emails_pct

    @property
    def bounces_pct(self):
        """Gets the bounces_pct of this EmailDomain.  # noqa: E501

        The percentage of total bounces from this domain.  # noqa: E501

        :return: The bounces_pct of this EmailDomain.  # noqa: E501
        :rtype: float
        """
        return self._bounces_pct

    @bounces_pct.setter
    def bounces_pct(self, bounces_pct):
        """Sets the bounces_pct of this EmailDomain.

        The percentage of total bounces from this domain.  # noqa: E501

        :param bounces_pct: The bounces_pct of this EmailDomain.  # noqa: E501
        :type: float
        """

        self._bounces_pct = bounces_pct

    @property
    def opens_pct(self):
        """Gets the opens_pct of this EmailDomain.  # noqa: E501

        The percentage of total opens from this domain.  # noqa: E501

        :return: The opens_pct of this EmailDomain.  # noqa: E501
        :rtype: float
        """
        return self._opens_pct

    @opens_pct.setter
    def opens_pct(self, opens_pct):
        """Sets the opens_pct of this EmailDomain.

        The percentage of total opens from this domain.  # noqa: E501

        :param opens_pct: The opens_pct of this EmailDomain.  # noqa: E501
        :type: float
        """

        self._opens_pct = opens_pct

    @property
    def clicks_pct(self):
        """Gets the clicks_pct of this EmailDomain.  # noqa: E501

        The percentage of total clicks from this domain.  # noqa: E501

        :return: The clicks_pct of this EmailDomain.  # noqa: E501
        :rtype: float
        """
        return self._clicks_pct

    @clicks_pct.setter
    def clicks_pct(self, clicks_pct):
        """Sets the clicks_pct of this EmailDomain.

        The percentage of total clicks from this domain.  # noqa: E501

        :param clicks_pct: The clicks_pct of this EmailDomain.  # noqa: E501
        :type: float
        """

        self._clicks_pct = clicks_pct

    @property
    def unsubs_pct(self):
        """Gets the unsubs_pct of this EmailDomain.  # noqa: E501

        The percentage of total unsubscribes from this domain.  # noqa: E501

        :return: The unsubs_pct of this EmailDomain.  # noqa: E501
        :rtype: float
        """
        return self._unsubs_pct

    @unsubs_pct.setter
    def unsubs_pct(self, unsubs_pct):
        """Sets the unsubs_pct of this EmailDomain.

        The percentage of total unsubscribes from this domain.  # noqa: E501

        :param unsubs_pct: The unsubs_pct of this EmailDomain.  # noqa: E501
        :type: float
        """

        self._unsubs_pct = unsubs_pct

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
        if issubclass(EmailDomain, dict):
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
        if not isinstance(other, EmailDomain):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
