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


class ListContact(object):
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
        'company': 'str',
        'address1': 'str',
        'address2': 'str',
        'city': 'str',
        'state': 'str',
        'zip': 'str',
        'country': 'str',
        'phone': 'str'
    }

    attribute_map = {
        'company': 'company',
        'address1': 'address1',
        'address2': 'address2',
        'city': 'city',
        'state': 'state',
        'zip': 'zip',
        'country': 'country',
        'phone': 'phone'
    }

    def __init__(self, company=None, address1=None, address2=None, city=None, state=None, zip=None, country=None, phone=None):  # noqa: E501
        """ListContact - a model defined in Swagger"""  # noqa: E501

        self._company = None
        self._address1 = None
        self._address2 = None
        self._city = None
        self._state = None
        self._zip = None
        self._country = None
        self._phone = None
        self.discriminator = None

        if company is not None:
            self.company = company
        if address1 is not None:
            self.address1 = address1
        if address2 is not None:
            self.address2 = address2
        if city is not None:
            self.city = city
        if state is not None:
            self.state = state
        if zip is not None:
            self.zip = zip
        if country is not None:
            self.country = country
        if phone is not None:
            self.phone = phone

    @property
    def company(self):
        """Gets the company of this ListContact.  # noqa: E501

        The company name for the list.  # noqa: E501

        :return: The company of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._company

    @company.setter
    def company(self, company):
        """Sets the company of this ListContact.

        The company name for the list.  # noqa: E501

        :param company: The company of this ListContact.  # noqa: E501
        :type: str
        """

        self._company = company

    @property
    def address1(self):
        """Gets the address1 of this ListContact.  # noqa: E501

        The street address for the list contact.  # noqa: E501

        :return: The address1 of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._address1

    @address1.setter
    def address1(self, address1):
        """Sets the address1 of this ListContact.

        The street address for the list contact.  # noqa: E501

        :param address1: The address1 of this ListContact.  # noqa: E501
        :type: str
        """

        self._address1 = address1

    @property
    def address2(self):
        """Gets the address2 of this ListContact.  # noqa: E501

        The street address for the list contact.  # noqa: E501

        :return: The address2 of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._address2

    @address2.setter
    def address2(self, address2):
        """Sets the address2 of this ListContact.

        The street address for the list contact.  # noqa: E501

        :param address2: The address2 of this ListContact.  # noqa: E501
        :type: str
        """

        self._address2 = address2

    @property
    def city(self):
        """Gets the city of this ListContact.  # noqa: E501

        The city for the list contact.  # noqa: E501

        :return: The city of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this ListContact.

        The city for the list contact.  # noqa: E501

        :param city: The city of this ListContact.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this ListContact.  # noqa: E501

        The state for the list contact.  # noqa: E501

        :return: The state of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ListContact.

        The state for the list contact.  # noqa: E501

        :param state: The state of this ListContact.  # noqa: E501
        :type: str
        """

        self._state = state

    @property
    def zip(self):
        """Gets the zip of this ListContact.  # noqa: E501

        The postal or zip code for the list contact.  # noqa: E501

        :return: The zip of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._zip

    @zip.setter
    def zip(self, zip):
        """Sets the zip of this ListContact.

        The postal or zip code for the list contact.  # noqa: E501

        :param zip: The zip of this ListContact.  # noqa: E501
        :type: str
        """

        self._zip = zip

    @property
    def country(self):
        """Gets the country of this ListContact.  # noqa: E501

        A two-character ISO3166 country code. Defaults to US if invalid.  # noqa: E501

        :return: The country of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this ListContact.

        A two-character ISO3166 country code. Defaults to US if invalid.  # noqa: E501

        :param country: The country of this ListContact.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def phone(self):
        """Gets the phone of this ListContact.  # noqa: E501

        The phone number for the list contact.  # noqa: E501

        :return: The phone of this ListContact.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this ListContact.

        The phone number for the list contact.  # noqa: E501

        :param phone: The phone of this ListContact.  # noqa: E501
        :type: str
        """

        self._phone = phone

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
        if issubclass(ListContact, dict):
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
        if not isinstance(other, ListContact):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other