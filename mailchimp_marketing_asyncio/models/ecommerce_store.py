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


class EcommerceStore(object):
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
        'list_id': 'str',
        'name': 'str',
        'platform': 'str',
        'domain': 'str',
        'is_syncing': 'bool',
        'email_address': 'str',
        'currency_code': 'str',
        'money_format': 'str',
        'primary_locale': 'str',
        'timezone': 'str',
        'phone': 'str',
        'address': 'Address1',
        'connected_site': 'ConnectedSite2',
        'automations': 'Automations',
        'list_is_active': 'bool',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'list_id': 'list_id',
        'name': 'name',
        'platform': 'platform',
        'domain': 'domain',
        'is_syncing': 'is_syncing',
        'email_address': 'email_address',
        'currency_code': 'currency_code',
        'money_format': 'money_format',
        'primary_locale': 'primary_locale',
        'timezone': 'timezone',
        'phone': 'phone',
        'address': 'address',
        'connected_site': 'connected_site',
        'automations': 'automations',
        'list_is_active': 'list_is_active',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'links': '_links'
    }

    def __init__(self, id=None, list_id=None, name=None, platform=None, domain=None, is_syncing=None, email_address=None, currency_code=None, money_format=None, primary_locale=None, timezone=None, phone=None, address=None, connected_site=None, automations=None, list_is_active=None, created_at=None, updated_at=None, links=None):  # noqa: E501
        """EcommerceStore - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._list_id = None
        self._name = None
        self._platform = None
        self._domain = None
        self._is_syncing = None
        self._email_address = None
        self._currency_code = None
        self._money_format = None
        self._primary_locale = None
        self._timezone = None
        self._phone = None
        self._address = None
        self._connected_site = None
        self._automations = None
        self._list_is_active = None
        self._created_at = None
        self._updated_at = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if list_id is not None:
            self.list_id = list_id
        if name is not None:
            self.name = name
        if platform is not None:
            self.platform = platform
        if domain is not None:
            self.domain = domain
        if is_syncing is not None:
            self.is_syncing = is_syncing
        if email_address is not None:
            self.email_address = email_address
        if currency_code is not None:
            self.currency_code = currency_code
        if money_format is not None:
            self.money_format = money_format
        if primary_locale is not None:
            self.primary_locale = primary_locale
        if timezone is not None:
            self.timezone = timezone
        if phone is not None:
            self.phone = phone
        if address is not None:
            self.address = address
        if connected_site is not None:
            self.connected_site = connected_site
        if automations is not None:
            self.automations = automations
        if list_is_active is not None:
            self.list_is_active = list_is_active
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this EcommerceStore.  # noqa: E501

        The unique identifier for the store.  # noqa: E501

        :return: The id of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EcommerceStore.

        The unique identifier for the store.  # noqa: E501

        :param id: The id of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def list_id(self):
        """Gets the list_id of this EcommerceStore.  # noqa: E501

        The unique identifier for the list that's associated with the store. The `list_id` for a specific store can't change.  # noqa: E501

        :return: The list_id of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this EcommerceStore.

        The unique identifier for the list that's associated with the store. The `list_id` for a specific store can't change.  # noqa: E501

        :param list_id: The list_id of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def name(self):
        """Gets the name of this EcommerceStore.  # noqa: E501

        The name of the store.  # noqa: E501

        :return: The name of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this EcommerceStore.

        The name of the store.  # noqa: E501

        :param name: The name of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def platform(self):
        """Gets the platform of this EcommerceStore.  # noqa: E501

        The e-commerce platform of the store.  # noqa: E501

        :return: The platform of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this EcommerceStore.

        The e-commerce platform of the store.  # noqa: E501

        :param platform: The platform of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._platform = platform

    @property
    def domain(self):
        """Gets the domain of this EcommerceStore.  # noqa: E501

        The store domain.  The store domain must be unique within a user account.  # noqa: E501

        :return: The domain of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this EcommerceStore.

        The store domain.  The store domain must be unique within a user account.  # noqa: E501

        :param domain: The domain of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._domain = domain

    @property
    def is_syncing(self):
        """Gets the is_syncing of this EcommerceStore.  # noqa: E501

        Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).  # noqa: E501

        :return: The is_syncing of this EcommerceStore.  # noqa: E501
        :rtype: bool
        """
        return self._is_syncing

    @is_syncing.setter
    def is_syncing(self, is_syncing):
        """Sets the is_syncing of this EcommerceStore.

        Whether to disable automations because the store is currently [syncing](https://mailchimp.com/developer/marketing/docs/e-commerce/#pausing-store-automations).  # noqa: E501

        :param is_syncing: The is_syncing of this EcommerceStore.  # noqa: E501
        :type: bool
        """

        self._is_syncing = is_syncing

    @property
    def email_address(self):
        """Gets the email_address of this EcommerceStore.  # noqa: E501

        The email address for the store.  # noqa: E501

        :return: The email_address of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this EcommerceStore.

        The email address for the store.  # noqa: E501

        :param email_address: The email_address of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def currency_code(self):
        """Gets the currency_code of this EcommerceStore.  # noqa: E501

        The three-letter ISO 4217 code for the currency that the store accepts.  # noqa: E501

        :return: The currency_code of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this EcommerceStore.

        The three-letter ISO 4217 code for the currency that the store accepts.  # noqa: E501

        :param currency_code: The currency_code of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

    @property
    def money_format(self):
        """Gets the money_format of this EcommerceStore.  # noqa: E501

        The currency format for the store. For example: `$`, `£`, etc.  # noqa: E501

        :return: The money_format of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._money_format

    @money_format.setter
    def money_format(self, money_format):
        """Sets the money_format of this EcommerceStore.

        The currency format for the store. For example: `$`, `£`, etc.  # noqa: E501

        :param money_format: The money_format of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._money_format = money_format

    @property
    def primary_locale(self):
        """Gets the primary_locale of this EcommerceStore.  # noqa: E501

        The primary locale for the store. For example: `en`, `de`, etc.  # noqa: E501

        :return: The primary_locale of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._primary_locale

    @primary_locale.setter
    def primary_locale(self, primary_locale):
        """Sets the primary_locale of this EcommerceStore.

        The primary locale for the store. For example: `en`, `de`, etc.  # noqa: E501

        :param primary_locale: The primary_locale of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._primary_locale = primary_locale

    @property
    def timezone(self):
        """Gets the timezone of this EcommerceStore.  # noqa: E501

        The timezone for the store.  # noqa: E501

        :return: The timezone of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this EcommerceStore.

        The timezone for the store.  # noqa: E501

        :param timezone: The timezone of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def phone(self):
        """Gets the phone of this EcommerceStore.  # noqa: E501

        The store phone number.  # noqa: E501

        :return: The phone of this EcommerceStore.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this EcommerceStore.

        The store phone number.  # noqa: E501

        :param phone: The phone of this EcommerceStore.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def address(self):
        """Gets the address of this EcommerceStore.  # noqa: E501


        :return: The address of this EcommerceStore.  # noqa: E501
        :rtype: Address1
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this EcommerceStore.


        :param address: The address of this EcommerceStore.  # noqa: E501
        :type: Address1
        """

        self._address = address

    @property
    def connected_site(self):
        """Gets the connected_site of this EcommerceStore.  # noqa: E501


        :return: The connected_site of this EcommerceStore.  # noqa: E501
        :rtype: ConnectedSite2
        """
        return self._connected_site

    @connected_site.setter
    def connected_site(self, connected_site):
        """Sets the connected_site of this EcommerceStore.


        :param connected_site: The connected_site of this EcommerceStore.  # noqa: E501
        :type: ConnectedSite2
        """

        self._connected_site = connected_site

    @property
    def automations(self):
        """Gets the automations of this EcommerceStore.  # noqa: E501


        :return: The automations of this EcommerceStore.  # noqa: E501
        :rtype: Automations
        """
        return self._automations

    @automations.setter
    def automations(self, automations):
        """Sets the automations of this EcommerceStore.


        :param automations: The automations of this EcommerceStore.  # noqa: E501
        :type: Automations
        """

        self._automations = automations

    @property
    def list_is_active(self):
        """Gets the list_is_active of this EcommerceStore.  # noqa: E501

        The status of the list connected to the store, namely if it's deleted or disabled.  # noqa: E501

        :return: The list_is_active of this EcommerceStore.  # noqa: E501
        :rtype: bool
        """
        return self._list_is_active

    @list_is_active.setter
    def list_is_active(self, list_is_active):
        """Sets the list_is_active of this EcommerceStore.

        The status of the list connected to the store, namely if it's deleted or disabled.  # noqa: E501

        :param list_is_active: The list_is_active of this EcommerceStore.  # noqa: E501
        :type: bool
        """

        self._list_is_active = list_is_active

    @property
    def created_at(self):
        """Gets the created_at of this EcommerceStore.  # noqa: E501

        The date and time the store was created in ISO 8601 format.  # noqa: E501

        :return: The created_at of this EcommerceStore.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this EcommerceStore.

        The date and time the store was created in ISO 8601 format.  # noqa: E501

        :param created_at: The created_at of this EcommerceStore.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this EcommerceStore.  # noqa: E501

        The date and time the store was last updated in ISO 8601 format.  # noqa: E501

        :return: The updated_at of this EcommerceStore.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this EcommerceStore.

        The date and time the store was last updated in ISO 8601 format.  # noqa: E501

        :param updated_at: The updated_at of this EcommerceStore.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def links(self):
        """Gets the links of this EcommerceStore.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this EcommerceStore.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this EcommerceStore.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this EcommerceStore.  # noqa: E501
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
        if issubclass(EcommerceStore, dict):
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
        if not isinstance(other, EcommerceStore):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
