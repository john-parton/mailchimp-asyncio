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


class Campaign(object):
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
        'web_id': 'int',
        'parent_campaign_id': 'str',
        'type': 'str',
        'create_time': 'datetime',
        'archive_url': 'str',
        'long_archive_url': 'str',
        'status': 'str',
        'emails_sent': 'int',
        'send_time': 'datetime',
        'content_type': 'str',
        'needs_block_refresh': 'bool',
        'resendable': 'bool',
        'recipients': 'List3',
        'settings': 'CampaignSettings2',
        'variate_settings': 'ABTestOptions',
        'tracking': 'CampaignTrackingOptions1',
        'rss_opts': 'RSSOptions',
        'ab_split_opts': 'ABTestingOptions',
        'social_card': 'CampaignSocialCard',
        'report_summary': 'CampaignReportSummary2',
        'delivery_status': 'CampaignDeliveryStatus',
        'links': 'list[ResourceLink]'
    }

    attribute_map = {
        'id': 'id',
        'web_id': 'web_id',
        'parent_campaign_id': 'parent_campaign_id',
        'type': 'type',
        'create_time': 'create_time',
        'archive_url': 'archive_url',
        'long_archive_url': 'long_archive_url',
        'status': 'status',
        'emails_sent': 'emails_sent',
        'send_time': 'send_time',
        'content_type': 'content_type',
        'needs_block_refresh': 'needs_block_refresh',
        'resendable': 'resendable',
        'recipients': 'recipients',
        'settings': 'settings',
        'variate_settings': 'variate_settings',
        'tracking': 'tracking',
        'rss_opts': 'rss_opts',
        'ab_split_opts': 'ab_split_opts',
        'social_card': 'social_card',
        'report_summary': 'report_summary',
        'delivery_status': 'delivery_status',
        'links': '_links'
    }

    def __init__(self, id=None, web_id=None, parent_campaign_id=None, type=None, create_time=None, archive_url=None, long_archive_url=None, status=None, emails_sent=None, send_time=None, content_type=None, needs_block_refresh=None, resendable=None, recipients=None, settings=None, variate_settings=None, tracking=None, rss_opts=None, ab_split_opts=None, social_card=None, report_summary=None, delivery_status=None, links=None):  # noqa: E501
        """Campaign - a model defined in Swagger"""  # noqa: E501

        self._id = None
        self._web_id = None
        self._parent_campaign_id = None
        self._type = None
        self._create_time = None
        self._archive_url = None
        self._long_archive_url = None
        self._status = None
        self._emails_sent = None
        self._send_time = None
        self._content_type = None
        self._needs_block_refresh = None
        self._resendable = None
        self._recipients = None
        self._settings = None
        self._variate_settings = None
        self._tracking = None
        self._rss_opts = None
        self._ab_split_opts = None
        self._social_card = None
        self._report_summary = None
        self._delivery_status = None
        self._links = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if web_id is not None:
            self.web_id = web_id
        if parent_campaign_id is not None:
            self.parent_campaign_id = parent_campaign_id
        if type is not None:
            self.type = type
        if create_time is not None:
            self.create_time = create_time
        if archive_url is not None:
            self.archive_url = archive_url
        if long_archive_url is not None:
            self.long_archive_url = long_archive_url
        if status is not None:
            self.status = status
        if emails_sent is not None:
            self.emails_sent = emails_sent
        if send_time is not None:
            self.send_time = send_time
        if content_type is not None:
            self.content_type = content_type
        if needs_block_refresh is not None:
            self.needs_block_refresh = needs_block_refresh
        if resendable is not None:
            self.resendable = resendable
        if recipients is not None:
            self.recipients = recipients
        if settings is not None:
            self.settings = settings
        if variate_settings is not None:
            self.variate_settings = variate_settings
        if tracking is not None:
            self.tracking = tracking
        if rss_opts is not None:
            self.rss_opts = rss_opts
        if ab_split_opts is not None:
            self.ab_split_opts = ab_split_opts
        if social_card is not None:
            self.social_card = social_card
        if report_summary is not None:
            self.report_summary = report_summary
        if delivery_status is not None:
            self.delivery_status = delivery_status
        if links is not None:
            self.links = links

    @property
    def id(self):
        """Gets the id of this Campaign.  # noqa: E501

        A string that uniquely identifies this campaign.  # noqa: E501

        :return: The id of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Campaign.

        A string that uniquely identifies this campaign.  # noqa: E501

        :param id: The id of this Campaign.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def web_id(self):
        """Gets the web_id of this Campaign.  # noqa: E501

        The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `https://{dc}.admin.mailchimp.com/campaigns/show/?id={web_id}`.  # noqa: E501

        :return: The web_id of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._web_id

    @web_id.setter
    def web_id(self, web_id):
        """Sets the web_id of this Campaign.

        The ID used in the Mailchimp web application. View this campaign in your Mailchimp account at `https://{dc}.admin.mailchimp.com/campaigns/show/?id={web_id}`.  # noqa: E501

        :param web_id: The web_id of this Campaign.  # noqa: E501
        :type: int
        """

        self._web_id = web_id

    @property
    def parent_campaign_id(self):
        """Gets the parent_campaign_id of this Campaign.  # noqa: E501

        If this campaign is the child of another campaign, this identifies the parent campaign. For Example, for RSS or Automation children.  # noqa: E501

        :return: The parent_campaign_id of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._parent_campaign_id

    @parent_campaign_id.setter
    def parent_campaign_id(self, parent_campaign_id):
        """Sets the parent_campaign_id of this Campaign.

        If this campaign is the child of another campaign, this identifies the parent campaign. For Example, for RSS or Automation children.  # noqa: E501

        :param parent_campaign_id: The parent_campaign_id of this Campaign.  # noqa: E501
        :type: str
        """

        self._parent_campaign_id = parent_campaign_id

    @property
    def type(self):
        """Gets the type of this Campaign.  # noqa: E501

        There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) you can create in Mailchimp. A/B Split campaigns have been deprecated and variate campaigns should be used instead.  # noqa: E501

        :return: The type of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Campaign.

        There are four types of [campaigns](https://mailchimp.com/help/getting-started-with-campaigns/) you can create in Mailchimp. A/B Split campaigns have been deprecated and variate campaigns should be used instead.  # noqa: E501

        :param type: The type of this Campaign.  # noqa: E501
        :type: str
        """
        allowed_values = ["regular", "plaintext", "absplit", "rss", "variate"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def create_time(self):
        """Gets the create_time of this Campaign.  # noqa: E501

        The date and time the campaign was created in ISO 8601 format.  # noqa: E501

        :return: The create_time of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Campaign.

        The date and time the campaign was created in ISO 8601 format.  # noqa: E501

        :param create_time: The create_time of this Campaign.  # noqa: E501
        :type: datetime
        """

        self._create_time = create_time

    @property
    def archive_url(self):
        """Gets the archive_url of this Campaign.  # noqa: E501

        The link to the campaign's archive version in ISO 8601 format.  # noqa: E501

        :return: The archive_url of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._archive_url

    @archive_url.setter
    def archive_url(self, archive_url):
        """Sets the archive_url of this Campaign.

        The link to the campaign's archive version in ISO 8601 format.  # noqa: E501

        :param archive_url: The archive_url of this Campaign.  # noqa: E501
        :type: str
        """

        self._archive_url = archive_url

    @property
    def long_archive_url(self):
        """Gets the long_archive_url of this Campaign.  # noqa: E501

        The original link to the campaign's archive version.  # noqa: E501

        :return: The long_archive_url of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._long_archive_url

    @long_archive_url.setter
    def long_archive_url(self, long_archive_url):
        """Sets the long_archive_url of this Campaign.

        The original link to the campaign's archive version.  # noqa: E501

        :param long_archive_url: The long_archive_url of this Campaign.  # noqa: E501
        :type: str
        """

        self._long_archive_url = long_archive_url

    @property
    def status(self):
        """Gets the status of this Campaign.  # noqa: E501

        The current status of the campaign.  # noqa: E501

        :return: The status of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Campaign.

        The current status of the campaign.  # noqa: E501

        :param status: The status of this Campaign.  # noqa: E501
        :type: str
        """
        allowed_values = ["save", "paused", "schedule", "sending", "sent", "canceled", "canceling", "archived"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def emails_sent(self):
        """Gets the emails_sent of this Campaign.  # noqa: E501

        The total number of emails sent for this campaign.  # noqa: E501

        :return: The emails_sent of this Campaign.  # noqa: E501
        :rtype: int
        """
        return self._emails_sent

    @emails_sent.setter
    def emails_sent(self, emails_sent):
        """Sets the emails_sent of this Campaign.

        The total number of emails sent for this campaign.  # noqa: E501

        :param emails_sent: The emails_sent of this Campaign.  # noqa: E501
        :type: int
        """

        self._emails_sent = emails_sent

    @property
    def send_time(self):
        """Gets the send_time of this Campaign.  # noqa: E501

        The date and time a campaign was sent.  # noqa: E501

        :return: The send_time of this Campaign.  # noqa: E501
        :rtype: datetime
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this Campaign.

        The date and time a campaign was sent.  # noqa: E501

        :param send_time: The send_time of this Campaign.  # noqa: E501
        :type: datetime
        """

        self._send_time = send_time

    @property
    def content_type(self):
        """Gets the content_type of this Campaign.  # noqa: E501

        How the campaign's content is put together.  # noqa: E501

        :return: The content_type of this Campaign.  # noqa: E501
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        """Sets the content_type of this Campaign.

        How the campaign's content is put together.  # noqa: E501

        :param content_type: The content_type of this Campaign.  # noqa: E501
        :type: str
        """
        allowed_values = ["template", "html", "url", "multichannel"]  # noqa: E501
        if content_type not in allowed_values:
            raise ValueError(
                "Invalid value for `content_type` ({0}), must be one of {1}"  # noqa: E501
                .format(content_type, allowed_values)
            )

        self._content_type = content_type

    @property
    def needs_block_refresh(self):
        """Gets the needs_block_refresh of this Campaign.  # noqa: E501

        Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. Deprecated and will always return false.  # noqa: E501

        :return: The needs_block_refresh of this Campaign.  # noqa: E501
        :rtype: bool
        """
        return self._needs_block_refresh

    @needs_block_refresh.setter
    def needs_block_refresh(self, needs_block_refresh):
        """Sets the needs_block_refresh of this Campaign.

        Determines if the campaign needs its blocks refreshed by opening the web-based campaign editor. Deprecated and will always return false.  # noqa: E501

        :param needs_block_refresh: The needs_block_refresh of this Campaign.  # noqa: E501
        :type: bool
        """

        self._needs_block_refresh = needs_block_refresh

    @property
    def resendable(self):
        """Gets the resendable of this Campaign.  # noqa: E501

        Determines if the campaign qualifies to be resent to non-openers.  # noqa: E501

        :return: The resendable of this Campaign.  # noqa: E501
        :rtype: bool
        """
        return self._resendable

    @resendable.setter
    def resendable(self, resendable):
        """Sets the resendable of this Campaign.

        Determines if the campaign qualifies to be resent to non-openers.  # noqa: E501

        :param resendable: The resendable of this Campaign.  # noqa: E501
        :type: bool
        """

        self._resendable = resendable

    @property
    def recipients(self):
        """Gets the recipients of this Campaign.  # noqa: E501


        :return: The recipients of this Campaign.  # noqa: E501
        :rtype: List3
        """
        return self._recipients

    @recipients.setter
    def recipients(self, recipients):
        """Sets the recipients of this Campaign.


        :param recipients: The recipients of this Campaign.  # noqa: E501
        :type: List3
        """

        self._recipients = recipients

    @property
    def settings(self):
        """Gets the settings of this Campaign.  # noqa: E501


        :return: The settings of this Campaign.  # noqa: E501
        :rtype: CampaignSettings2
        """
        return self._settings

    @settings.setter
    def settings(self, settings):
        """Sets the settings of this Campaign.


        :param settings: The settings of this Campaign.  # noqa: E501
        :type: CampaignSettings2
        """

        self._settings = settings

    @property
    def variate_settings(self):
        """Gets the variate_settings of this Campaign.  # noqa: E501


        :return: The variate_settings of this Campaign.  # noqa: E501
        :rtype: ABTestOptions
        """
        return self._variate_settings

    @variate_settings.setter
    def variate_settings(self, variate_settings):
        """Sets the variate_settings of this Campaign.


        :param variate_settings: The variate_settings of this Campaign.  # noqa: E501
        :type: ABTestOptions
        """

        self._variate_settings = variate_settings

    @property
    def tracking(self):
        """Gets the tracking of this Campaign.  # noqa: E501


        :return: The tracking of this Campaign.  # noqa: E501
        :rtype: CampaignTrackingOptions1
        """
        return self._tracking

    @tracking.setter
    def tracking(self, tracking):
        """Sets the tracking of this Campaign.


        :param tracking: The tracking of this Campaign.  # noqa: E501
        :type: CampaignTrackingOptions1
        """

        self._tracking = tracking

    @property
    def rss_opts(self):
        """Gets the rss_opts of this Campaign.  # noqa: E501


        :return: The rss_opts of this Campaign.  # noqa: E501
        :rtype: RSSOptions
        """
        return self._rss_opts

    @rss_opts.setter
    def rss_opts(self, rss_opts):
        """Sets the rss_opts of this Campaign.


        :param rss_opts: The rss_opts of this Campaign.  # noqa: E501
        :type: RSSOptions
        """

        self._rss_opts = rss_opts

    @property
    def ab_split_opts(self):
        """Gets the ab_split_opts of this Campaign.  # noqa: E501


        :return: The ab_split_opts of this Campaign.  # noqa: E501
        :rtype: ABTestingOptions
        """
        return self._ab_split_opts

    @ab_split_opts.setter
    def ab_split_opts(self, ab_split_opts):
        """Sets the ab_split_opts of this Campaign.


        :param ab_split_opts: The ab_split_opts of this Campaign.  # noqa: E501
        :type: ABTestingOptions
        """

        self._ab_split_opts = ab_split_opts

    @property
    def social_card(self):
        """Gets the social_card of this Campaign.  # noqa: E501


        :return: The social_card of this Campaign.  # noqa: E501
        :rtype: CampaignSocialCard
        """
        return self._social_card

    @social_card.setter
    def social_card(self, social_card):
        """Sets the social_card of this Campaign.


        :param social_card: The social_card of this Campaign.  # noqa: E501
        :type: CampaignSocialCard
        """

        self._social_card = social_card

    @property
    def report_summary(self):
        """Gets the report_summary of this Campaign.  # noqa: E501


        :return: The report_summary of this Campaign.  # noqa: E501
        :rtype: CampaignReportSummary2
        """
        return self._report_summary

    @report_summary.setter
    def report_summary(self, report_summary):
        """Sets the report_summary of this Campaign.


        :param report_summary: The report_summary of this Campaign.  # noqa: E501
        :type: CampaignReportSummary2
        """

        self._report_summary = report_summary

    @property
    def delivery_status(self):
        """Gets the delivery_status of this Campaign.  # noqa: E501


        :return: The delivery_status of this Campaign.  # noqa: E501
        :rtype: CampaignDeliveryStatus
        """
        return self._delivery_status

    @delivery_status.setter
    def delivery_status(self, delivery_status):
        """Sets the delivery_status of this Campaign.


        :param delivery_status: The delivery_status of this Campaign.  # noqa: E501
        :type: CampaignDeliveryStatus
        """

        self._delivery_status = delivery_status

    @property
    def links(self):
        """Gets the links of this Campaign.  # noqa: E501

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :return: The links of this Campaign.  # noqa: E501
        :rtype: list[ResourceLink]
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this Campaign.

        A list of link types and descriptions for the API schema documents.  # noqa: E501

        :param links: The links of this Campaign.  # noqa: E501
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
        if issubclass(Campaign, dict):
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
        if not isinstance(other, Campaign):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
