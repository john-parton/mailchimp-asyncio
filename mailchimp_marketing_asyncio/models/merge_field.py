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


class MergeField(object):
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
        'merge_id': 'int',
        'tag': 'str',
        'name': 'str',
        'type': 'str',
        'required': 'bool',
        'default_value': 'str',
        'public': 'bool',
        'display_order': 'int',
        'options': 'MergeFieldOptions',
        'help_text': 'str',
        'list_id': 'str',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'merge_id': 'merge_id',
        'tag': 'tag',
        'name': 'name',
        'type': 'type',
        'required': 'required',
        'default_value': 'default_value',
        'public': 'public',
        'display_order': 'display_order',
        'options': 'options',
        'help_text': 'help_text',
        'list_id': 'list_id',
        'links': '_links'
    }

    def __init__(self, merge_id=None, tag=None, name=None, type=None, required=None, default_value=None, public=None, display_order=None, options=None, help_text=None, list_id=None, links=None):  # noqa: E501
        """MergeField - a model defined in Swagger"""  # noqa: E501

        self._merge_id = None
        self._tag = None
        self._name = None
        self._type = None
        self._required = None
        self._default_value = None
        self._public = None
        self._display_order = None
        self._options = None
        self._help_text = None
        self._list_id = None
        self._links = None
        self.discriminator = None

        if merge_id is not None:
            self.merge_id = merge_id
        if tag is not None:
            self.tag = tag
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if required is not None:
            self.required = required
        if default_value is not None:
            self.default_value = default_value
        if public is not None:
            self.public = public
        if display_order is not None:
            self.display_order = display_order
        if options is not None:
            self.options = options
        if help_text is not None:
            self.help_text = help_text
        if list_id is not None:
            self.list_id = list_id
        if links is not None:
            self.links = links

    @property
    def merge_id(self):
        """Gets the merge_id of this MergeField.  # noqa: E501

        An unchanging id for the merge field.  # noqa: E501

        :return: The merge_id of this MergeField.  # noqa: E501
        :rtype: int
        """
        return self._merge_id

    @merge_id.setter
    def merge_id(self, merge_id):
        """Sets the merge_id of this MergeField.

        An unchanging id for the merge field.  # noqa: E501

        :param merge_id: The merge_id of this MergeField.  # noqa: E501
        :type: int
        """

        self._merge_id = merge_id

    @property
    def tag(self):
        """Gets the tag of this MergeField.  # noqa: E501

        The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).  # noqa: E501

        :return: The tag of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this MergeField.

        The merge tag used for Mailchimp campaigns and [adding contact information](https://mailchimp.com/developer/marketing/docs/merge-fields/#add-merge-data-to-contacts).  # noqa: E501

        :param tag: The tag of this MergeField.  # noqa: E501
        :type: str
        """

        self._tag = tag

    @property
    def name(self):
        """Gets the name of this MergeField.  # noqa: E501

        The name of the merge field (audience field).  # noqa: E501

        :return: The name of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MergeField.

        The name of the merge field (audience field).  # noqa: E501

        :param name: The name of this MergeField.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this MergeField.  # noqa: E501

        The [type](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.  # noqa: E501

        :return: The type of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MergeField.

        The [type](https://mailchimp.com/developer/marketing/docs/merge-fields/#structure) for the merge field.  # noqa: E501

        :param type: The type of this MergeField.  # noqa: E501
        :type: str
        """
        allowed_values = ["text", "number", "address", "phone", "date", "url", "imageurl", "radio", "dropdown", "birthday", "zip"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def required(self):
        """Gets the required of this MergeField.  # noqa: E501

        The boolean value if the merge field is required.  # noqa: E501

        :return: The required of this MergeField.  # noqa: E501
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        """Sets the required of this MergeField.

        The boolean value if the merge field is required.  # noqa: E501

        :param required: The required of this MergeField.  # noqa: E501
        :type: bool
        """

        self._required = required

    @property
    def default_value(self):
        """Gets the default_value of this MergeField.  # noqa: E501

        The default value for the merge field if `null`.  # noqa: E501

        :return: The default_value of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this MergeField.

        The default value for the merge field if `null`.  # noqa: E501

        :param default_value: The default_value of this MergeField.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def public(self):
        """Gets the public of this MergeField.  # noqa: E501

        Whether the merge field is displayed on the signup form.  # noqa: E501

        :return: The public of this MergeField.  # noqa: E501
        :rtype: bool
        """
        return self._public

    @public.setter
    def public(self, public):
        """Sets the public of this MergeField.

        Whether the merge field is displayed on the signup form.  # noqa: E501

        :param public: The public of this MergeField.  # noqa: E501
        :type: bool
        """

        self._public = public

    @property
    def display_order(self):
        """Gets the display_order of this MergeField.  # noqa: E501

        The order that the merge field displays on the list signup form.  # noqa: E501

        :return: The display_order of this MergeField.  # noqa: E501
        :rtype: int
        """
        return self._display_order

    @display_order.setter
    def display_order(self, display_order):
        """Sets the display_order of this MergeField.

        The order that the merge field displays on the list signup form.  # noqa: E501

        :param display_order: The display_order of this MergeField.  # noqa: E501
        :type: int
        """

        self._display_order = display_order

    @property
    def options(self):
        """Gets the options of this MergeField.  # noqa: E501


        :return: The options of this MergeField.  # noqa: E501
        :rtype: MergeFieldOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this MergeField.


        :param options: The options of this MergeField.  # noqa: E501
        :type: MergeFieldOptions
        """

        self._options = options

    @property
    def help_text(self):
        """Gets the help_text of this MergeField.  # noqa: E501

        Extra text to help the subscriber fill out the form.  # noqa: E501

        :return: The help_text of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._help_text

    @help_text.setter
    def help_text(self, help_text):
        """Sets the help_text of this MergeField.

        Extra text to help the subscriber fill out the form.  # noqa: E501

        :param help_text: The help_text of this MergeField.  # noqa: E501
        :type: str
        """

        self._help_text = help_text

    @property
    def list_id(self):
        """Gets the list_id of this MergeField.  # noqa: E501

        The ID that identifies this merge field's audience'.  # noqa: E501

        :return: The list_id of this MergeField.  # noqa: E501
        :rtype: str
        """
        return self._list_id

    @list_id.setter
    def list_id(self, list_id):
        """Sets the list_id of this MergeField.

        The ID that identifies this merge field's audience'.  # noqa: E501

        :param list_id: The list_id of this MergeField.  # noqa: E501
        :type: str
        """

        self._list_id = list_id

    @property
    def links(self):
        """Gets the links of this MergeField.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this MergeField.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this MergeField.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this MergeField.  # noqa: E501
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
        if issubclass(MergeField, dict):
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
        if not isinstance(other, MergeField):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
