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


class UploadArchive(object):
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
        'archive_content': 'str',
        'archive_type': 'str'
    }

    attribute_map = {
        'archive_content': 'archive_content',
        'archive_type': 'archive_type'
    }

    def __init__(self, archive_content=None, archive_type=None):  # noqa: E501
        """UploadArchive - a model defined in Swagger"""  # noqa: E501

        self._archive_content = None
        self._archive_type = None
        self.discriminator = None

        self.archive_content = archive_content
        if archive_type is not None:
            self.archive_type = archive_type

    @property
    def archive_content(self):
        """Gets the archive_content of this UploadArchive.  # noqa: E501

        The base64-encoded representation of the archive file.  # noqa: E501

        :return: The archive_content of this UploadArchive.  # noqa: E501
        :rtype: str
        """
        return self._archive_content

    @archive_content.setter
    def archive_content(self, archive_content):
        """Sets the archive_content of this UploadArchive.

        The base64-encoded representation of the archive file.  # noqa: E501

        :param archive_content: The archive_content of this UploadArchive.  # noqa: E501
        :type: str
        """
        if archive_content is None:
            raise ValueError("Invalid value for `archive_content`, must not be `None`")  # noqa: E501

        self._archive_content = archive_content

    @property
    def archive_type(self):
        """Gets the archive_type of this UploadArchive.  # noqa: E501

        The type of encoded file. Defaults to zip.  # noqa: E501

        :return: The archive_type of this UploadArchive.  # noqa: E501
        :rtype: str
        """
        return self._archive_type

    @archive_type.setter
    def archive_type(self, archive_type):
        """Sets the archive_type of this UploadArchive.

        The type of encoded file. Defaults to zip.  # noqa: E501

        :param archive_type: The archive_type of this UploadArchive.  # noqa: E501
        :type: str
        """
        allowed_values = ["zip", "tar.gz", "tar.bz2", "tar", "tgz", "tbz"]  # noqa: E501
        if archive_type not in allowed_values:
            raise ValueError(
                "Invalid value for `archive_type` ({0}), must be one of {1}"  # noqa: E501
                .format(archive_type, allowed_values)
            )

        self._archive_type = archive_type

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
        if issubclass(UploadArchive, dict):
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
        if not isinstance(other, UploadArchive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
