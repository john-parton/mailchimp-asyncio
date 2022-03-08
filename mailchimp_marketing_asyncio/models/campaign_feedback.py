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


class CampaignFeedback(object):
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
        'feedback_id': 'int',
        'parent_id': 'int',
        'block_id': 'int',
        'message': 'str',
        'is_complete': 'bool',
        'created_by': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'source': 'str',
        'campaign_id': 'str',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'feedback_id': 'feedback_id',
        'parent_id': 'parent_id',
        'block_id': 'block_id',
        'message': 'message',
        'is_complete': 'is_complete',
        'created_by': 'created_by',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'source': 'source',
        'campaign_id': 'campaign_id',
        'links': '_links'
    }

    def __init__(self, feedback_id=None, parent_id=None, block_id=None, message=None, is_complete=None, created_by=None, created_at=None, updated_at=None, source=None, campaign_id=None, links=None):  # noqa: E501
        """CampaignFeedback - a model defined in Swagger"""  # noqa: E501

        self._feedback_id = None
        self._parent_id = None
        self._block_id = None
        self._message = None
        self._is_complete = None
        self._created_by = None
        self._created_at = None
        self._updated_at = None
        self._source = None
        self._campaign_id = None
        self._links = None
        self.discriminator = None

        if feedback_id is not None:
            self.feedback_id = feedback_id
        if parent_id is not None:
            self.parent_id = parent_id
        if block_id is not None:
            self.block_id = block_id
        self.message = message
        if is_complete is not None:
            self.is_complete = is_complete
        if created_by is not None:
            self.created_by = created_by
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if source is not None:
            self.source = source
        if campaign_id is not None:
            self.campaign_id = campaign_id
        if links is not None:
            self.links = links

    @property
    def feedback_id(self):
        """Gets the feedback_id of this CampaignFeedback.  # noqa: E501

        The individual id for the feedback item.  # noqa: E501

        :return: The feedback_id of this CampaignFeedback.  # noqa: E501
        :rtype: int
        """
        return self._feedback_id

    @feedback_id.setter
    def feedback_id(self, feedback_id):
        """Sets the feedback_id of this CampaignFeedback.

        The individual id for the feedback item.  # noqa: E501

        :param feedback_id: The feedback_id of this CampaignFeedback.  # noqa: E501
        :type: int
        """

        self._feedback_id = feedback_id

    @property
    def parent_id(self):
        """Gets the parent_id of this CampaignFeedback.  # noqa: E501

        If a reply, the id of the parent feedback item.  # noqa: E501

        :return: The parent_id of this CampaignFeedback.  # noqa: E501
        :rtype: int
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this CampaignFeedback.

        If a reply, the id of the parent feedback item.  # noqa: E501

        :param parent_id: The parent_id of this CampaignFeedback.  # noqa: E501
        :type: int
        """

        self._parent_id = parent_id

    @property
    def block_id(self):
        """Gets the block_id of this CampaignFeedback.  # noqa: E501

        The block id for the editable block that the feedback addresses.  # noqa: E501

        :return: The block_id of this CampaignFeedback.  # noqa: E501
        :rtype: int
        """
        return self._block_id

    @block_id.setter
    def block_id(self, block_id):
        """Sets the block_id of this CampaignFeedback.

        The block id for the editable block that the feedback addresses.  # noqa: E501

        :param block_id: The block_id of this CampaignFeedback.  # noqa: E501
        :type: int
        """

        self._block_id = block_id

    @property
    def message(self):
        """Gets the message of this CampaignFeedback.  # noqa: E501

        The content of the feedback.  # noqa: E501

        :return: The message of this CampaignFeedback.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CampaignFeedback.

        The content of the feedback.  # noqa: E501

        :param message: The message of this CampaignFeedback.  # noqa: E501
        :type: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")  # noqa: E501

        self._message = message

    @property
    def is_complete(self):
        """Gets the is_complete of this CampaignFeedback.  # noqa: E501

        The status of feedback.  # noqa: E501

        :return: The is_complete of this CampaignFeedback.  # noqa: E501
        :rtype: bool
        """
        return self._is_complete

    @is_complete.setter
    def is_complete(self, is_complete):
        """Sets the is_complete of this CampaignFeedback.

        The status of feedback.  # noqa: E501

        :param is_complete: The is_complete of this CampaignFeedback.  # noqa: E501
        :type: bool
        """

        self._is_complete = is_complete

    @property
    def created_by(self):
        """Gets the created_by of this CampaignFeedback.  # noqa: E501

        The login name of the user who created the feedback.  # noqa: E501

        :return: The created_by of this CampaignFeedback.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CampaignFeedback.

        The login name of the user who created the feedback.  # noqa: E501

        :param created_by: The created_by of this CampaignFeedback.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def created_at(self):
        """Gets the created_at of this CampaignFeedback.  # noqa: E501

        The date and time the feedback item was created in ISO 8601 format.  # noqa: E501

        :return: The created_at of this CampaignFeedback.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CampaignFeedback.

        The date and time the feedback item was created in ISO 8601 format.  # noqa: E501

        :param created_at: The created_at of this CampaignFeedback.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this CampaignFeedback.  # noqa: E501

        The date and time the feedback was last updated in ISO 8601 format.  # noqa: E501

        :return: The updated_at of this CampaignFeedback.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this CampaignFeedback.

        The date and time the feedback was last updated in ISO 8601 format.  # noqa: E501

        :param updated_at: The updated_at of this CampaignFeedback.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

    @property
    def source(self):
        """Gets the source of this CampaignFeedback.  # noqa: E501

        The source of the feedback.  # noqa: E501

        :return: The source of this CampaignFeedback.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this CampaignFeedback.

        The source of the feedback.  # noqa: E501

        :param source: The source of this CampaignFeedback.  # noqa: E501
        :type: str
        """
        allowed_values = ["api", "email", "sms", "web", "ios", "android"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

    @property
    def campaign_id(self):
        """Gets the campaign_id of this CampaignFeedback.  # noqa: E501

        The unique id for the campaign.  # noqa: E501

        :return: The campaign_id of this CampaignFeedback.  # noqa: E501
        :rtype: str
        """
        return self._campaign_id

    @campaign_id.setter
    def campaign_id(self, campaign_id):
        """Sets the campaign_id of this CampaignFeedback.

        The unique id for the campaign.  # noqa: E501

        :param campaign_id: The campaign_id of this CampaignFeedback.  # noqa: E501
        :type: str
        """

        self._campaign_id = campaign_id

    @property
    def links(self):
        """Gets the links of this CampaignFeedback.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this CampaignFeedback.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this CampaignFeedback.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this CampaignFeedback.  # noqa: E501
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
        if issubclass(CampaignFeedback, dict):
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
        if not isinstance(other, CampaignFeedback):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
