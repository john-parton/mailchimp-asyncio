# coding: utf-8

# flake8: noqa
"""
    Mailchimp Marketing API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0.74
    Contact: apihelp@mailchimp.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

# import models into model package
from mailchimp_marketing_asyncio.models.ab_split import ABSplit
from mailchimp_marketing_asyncio.models.ab_split_stats import ABSplitStats
from mailchimp_marketing_asyncio.models.ab_test_options import ABTestOptions
from mailchimp_marketing_asyncio.models.ab_test_options1 import ABTestOptions1
from mailchimp_marketing_asyncio.models.ab_test_options2 import ABTestOptions2
from mailchimp_marketing_asyncio.models.ab_test_options_combinations import ABTestOptionsCombinations
from mailchimp_marketing_asyncio.models.ab_testing_options import ABTestingOptions
from mailchimp_marketing_asyncio.models.api_health_status import APIHealthStatus
from mailchimp_marketing_asyncio.models.api_root import APIRoot
from mailchimp_marketing_asyncio.models.abandoned_browse_automation import AbandonedBrowseAutomation
from mailchimp_marketing_asyncio.models.abandoned_cart_automation import AbandonedCartAutomation
from mailchimp_marketing_asyncio.models.abuse_complaint import AbuseComplaint
from mailchimp_marketing_asyncio.models.abuse_complaint1 import AbuseComplaint1
from mailchimp_marketing_asyncio.models.abuse_complaints import AbuseComplaints
from mailchimp_marketing_asyncio.models.abuse_complaints1 import AbuseComplaints1
from mailchimp_marketing_asyncio.models.account_contact import AccountContact
from mailchimp_marketing_asyncio.models.add_list_members import AddListMembers
from mailchimp_marketing_asyncio.models.add_list_members1 import AddListMembers1
from mailchimp_marketing_asyncio.models.add_list_members2 import AddListMembers2
from mailchimp_marketing_asyncio.models.add_list_members3 import AddListMembers3
from mailchimp_marketing_asyncio.models.add_webhook import AddWebhook
from mailchimp_marketing_asyncio.models.add_webhook1 import AddWebhook1
from mailchimp_marketing_asyncio.models.address import Address
from mailchimp_marketing_asyncio.models.address1 import Address1
from mailchimp_marketing_asyncio.models.an_option_for_signup_form_styles import AnOptionForSignupFormStyles
from mailchimp_marketing_asyncio.models.automation_campaign_settings import AutomationCampaignSettings
from mailchimp_marketing_asyncio.models.automation_campaign_settings1 import AutomationCampaignSettings1
from mailchimp_marketing_asyncio.models.automation_delay import AutomationDelay
from mailchimp_marketing_asyncio.models.automation_delay1 import AutomationDelay1
from mailchimp_marketing_asyncio.models.automation_emails import AutomationEmails
from mailchimp_marketing_asyncio.models.automation_tracking_options import AutomationTrackingOptions
from mailchimp_marketing_asyncio.models.automation_trigger import AutomationTrigger
from mailchimp_marketing_asyncio.models.automation_trigger1 import AutomationTrigger1
from mailchimp_marketing_asyncio.models.automation_workflow import AutomationWorkflow
from mailchimp_marketing_asyncio.models.automation_workflow1 import AutomationWorkflow1
from mailchimp_marketing_asyncio.models.automation_workflow_email import AutomationWorkflowEmail
from mailchimp_marketing_asyncio.models.automation_workflow_runtime_settings import AutomationWorkflowRuntimeSettings
from mailchimp_marketing_asyncio.models.automations import Automations
from mailchimp_marketing_asyncio.models.batch import Batch
from mailchimp_marketing_asyncio.models.batch_addremove_list_members_tofrom_static_segment import BatchAddremoveListMembersTofromStaticSegment
from mailchimp_marketing_asyncio.models.batch_addremove_list_members_tofrom_static_segment_errors import BatchAddremoveListMembersTofromStaticSegmentErrors
from mailchimp_marketing_asyncio.models.batch_delivery import BatchDelivery
from mailchimp_marketing_asyncio.models.batch_operations import BatchOperations
from mailchimp_marketing_asyncio.models.batch_update_list_members import BatchUpdateListMembers
from mailchimp_marketing_asyncio.models.batch_update_list_members_errors import BatchUpdateListMembersErrors
from mailchimp_marketing_asyncio.models.batch_update_list_members_tags import BatchUpdateListMembersTags
from mailchimp_marketing_asyncio.models.batch_webhook import BatchWebhook
from mailchimp_marketing_asyncio.models.batch_webhook1 import BatchWebhook1
from mailchimp_marketing_asyncio.models.batch_webhook2 import BatchWebhook2
from mailchimp_marketing_asyncio.models.batch_webhooks import BatchWebhooks
from mailchimp_marketing_asyncio.models.billing_address import BillingAddress
from mailchimp_marketing_asyncio.models.billing_address1 import BillingAddress1
from mailchimp_marketing_asyncio.models.body import Body
from mailchimp_marketing_asyncio.models.body1 import Body1
from mailchimp_marketing_asyncio.models.body2 import Body2
from mailchimp_marketing_asyncio.models.body3 import Body3
from mailchimp_marketing_asyncio.models.bounces import Bounces
from mailchimp_marketing_asyncio.models.campaign import Campaign
from mailchimp_marketing_asyncio.models.campaign1 import Campaign1
from mailchimp_marketing_asyncio.models.campaign2 import Campaign2
from mailchimp_marketing_asyncio.models.campaign3 import Campaign3
from mailchimp_marketing_asyncio.models.campaign_a import CampaignA
from mailchimp_marketing_asyncio.models.campaign_advice import CampaignAdvice
from mailchimp_marketing_asyncio.models.campaign_advice_report import CampaignAdviceReport
from mailchimp_marketing_asyncio.models.campaign_b import CampaignB
from mailchimp_marketing_asyncio.models.campaign_content import CampaignContent
from mailchimp_marketing_asyncio.models.campaign_content1 import CampaignContent1
from mailchimp_marketing_asyncio.models.campaign_content_variate_contents import CampaignContentVariateContents
from mailchimp_marketing_asyncio.models.campaign_defaults import CampaignDefaults
from mailchimp_marketing_asyncio.models.campaign_defaults1 import CampaignDefaults1
from mailchimp_marketing_asyncio.models.campaign_delivery_status import CampaignDeliveryStatus
from mailchimp_marketing_asyncio.models.campaign_feedback import CampaignFeedback
from mailchimp_marketing_asyncio.models.campaign_feedback1 import CampaignFeedback1
from mailchimp_marketing_asyncio.models.campaign_feedback2 import CampaignFeedback2
from mailchimp_marketing_asyncio.models.campaign_feedback3 import CampaignFeedback3
from mailchimp_marketing_asyncio.models.campaign_folder import CampaignFolder
from mailchimp_marketing_asyncio.models.campaign_folder1 import CampaignFolder1
from mailchimp_marketing_asyncio.models.campaign_folder2 import CampaignFolder2
from mailchimp_marketing_asyncio.models.campaign_folders import CampaignFolders
from mailchimp_marketing_asyncio.models.campaign_report import CampaignReport
from mailchimp_marketing_asyncio.models.campaign_report_summary import CampaignReportSummary
from mailchimp_marketing_asyncio.models.campaign_report_summary1 import CampaignReportSummary1
from mailchimp_marketing_asyncio.models.campaign_report_summary2 import CampaignReportSummary2
from mailchimp_marketing_asyncio.models.campaign_report_summary3 import CampaignReportSummary3
from mailchimp_marketing_asyncio.models.campaign_reports import CampaignReports
from mailchimp_marketing_asyncio.models.campaign_reports1 import CampaignReports1
from mailchimp_marketing_asyncio.models.campaign_reports1_timeseries import CampaignReports1Timeseries
from mailchimp_marketing_asyncio.models.campaign_reports1_timewarp import CampaignReports1Timewarp
from mailchimp_marketing_asyncio.models.campaign_settings import CampaignSettings
from mailchimp_marketing_asyncio.models.campaign_settings1 import CampaignSettings1
from mailchimp_marketing_asyncio.models.campaign_settings2 import CampaignSettings2
from mailchimp_marketing_asyncio.models.campaign_settings3 import CampaignSettings3
from mailchimp_marketing_asyncio.models.campaign_settings4 import CampaignSettings4
from mailchimp_marketing_asyncio.models.campaign_settings5 import CampaignSettings5
from mailchimp_marketing_asyncio.models.campaign_social_card import CampaignSocialCard
from mailchimp_marketing_asyncio.models.campaign_sub_reports import CampaignSubReports
from mailchimp_marketing_asyncio.models.campaign_tracking_options import CampaignTrackingOptions
from mailchimp_marketing_asyncio.models.campaign_tracking_options1 import CampaignTrackingOptions1
from mailchimp_marketing_asyncio.models.campaigns import Campaigns
from mailchimp_marketing_asyncio.models.campaigns_results import CampaignsResults
from mailchimp_marketing_asyncio.models.campaignscampaign_idcontent_variate_contents import CampaignscampaignIdcontentVariateContents
from mailchimp_marketing_asyncio.models.capsule_crm_tracking import CapsuleCRMTracking
from mailchimp_marketing_asyncio.models.capsule_crm_tracking1 import CapsuleCRMTracking1
from mailchimp_marketing_asyncio.models.capsule_crm_tracking2 import CapsuleCRMTracking2
from mailchimp_marketing_asyncio.models.cart_lines import CartLines
from mailchimp_marketing_asyncio.models.carts import Carts
from mailchimp_marketing_asyncio.models.chimp_chatter import ChimpChatter
from mailchimp_marketing_asyncio.models.click_detail_member import ClickDetailMember
from mailchimp_marketing_asyncio.models.click_detail_members import ClickDetailMembers
from mailchimp_marketing_asyncio.models.click_detail_report import ClickDetailReport
from mailchimp_marketing_asyncio.models.click_summary import ClickSummary
from mailchimp_marketing_asyncio.models.clicks import Clicks
from mailchimp_marketing_asyncio.models.collection_authorization import CollectionAuthorization
from mailchimp_marketing_asyncio.models.collection_of_content_for_list_signup_forms import CollectionOfContentForListSignupForms
from mailchimp_marketing_asyncio.models.collection_of_conversation_messages import CollectionOfConversationMessages
from mailchimp_marketing_asyncio.models.collection_of_element_style_for_list_signup_forms import CollectionOfElementStyleForListSignupForms
from mailchimp_marketing_asyncio.models.collection_of_events import CollectionOfEvents
from mailchimp_marketing_asyncio.models.collection_of_member_activity_events import CollectionOfMemberActivityEvents
from mailchimp_marketing_asyncio.models.collection_of_merge_fields import CollectionOfMergeFields
from mailchimp_marketing_asyncio.models.collection_of_notes import CollectionOfNotes
from mailchimp_marketing_asyncio.models.collection_of_segments import CollectionOfSegments
from mailchimp_marketing_asyncio.models.collection_of_tags import CollectionOfTags
from mailchimp_marketing_asyncio.models.collection_of_tags_tags import CollectionOfTagsTags
from mailchimp_marketing_asyncio.models.conditions import Conditions
from mailchimp_marketing_asyncio.models.conditions1 import Conditions1
from mailchimp_marketing_asyncio.models.conditions2 import Conditions2
from mailchimp_marketing_asyncio.models.connected_site import ConnectedSite
from mailchimp_marketing_asyncio.models.connected_site1 import ConnectedSite1
from mailchimp_marketing_asyncio.models.connected_site2 import ConnectedSite2
from mailchimp_marketing_asyncio.models.connected_sites import ConnectedSites
from mailchimp_marketing_asyncio.models.conversation import Conversation
from mailchimp_marketing_asyncio.models.conversation_message import ConversationMessage
from mailchimp_marketing_asyncio.models.create_an_account_export import CreateAnAccountExport
from mailchimp_marketing_asyncio.models.customers import Customers
from mailchimp_marketing_asyncio.models.daily_clicks_and_visits_data import DailyClicksAndVisitsData
from mailchimp_marketing_asyncio.models.daily_clicks_and_visits_data_clicks import DailyClicksAndVisitsDataClicks
from mailchimp_marketing_asyncio.models.daily_clicks_and_visits_data_unique_visits import DailyClicksAndVisitsDataUniqueVisits
from mailchimp_marketing_asyncio.models.daily_clicks_and_visits_data_visits import DailyClicksAndVisitsDataVisits
from mailchimp_marketing_asyncio.models.daily_list_activity import DailyListActivity
from mailchimp_marketing_asyncio.models.daily_sending_days import DailySendingDays
from mailchimp_marketing_asyncio.models.domain_performance import DomainPerformance
from mailchimp_marketing_asyncio.models.e_commerce_report import ECommerceReport
from mailchimp_marketing_asyncio.models.e_commerce_report1 import ECommerceReport1
from mailchimp_marketing_asyncio.models.ecommerce_cart import EcommerceCart
from mailchimp_marketing_asyncio.models.ecommerce_cart1 import EcommerceCart1
from mailchimp_marketing_asyncio.models.ecommerce_cart2 import EcommerceCart2
from mailchimp_marketing_asyncio.models.ecommerce_cart_line_item import EcommerceCartLineItem
from mailchimp_marketing_asyncio.models.ecommerce_cart_line_item1 import EcommerceCartLineItem1
from mailchimp_marketing_asyncio.models.ecommerce_cart_line_item2 import EcommerceCartLineItem2
from mailchimp_marketing_asyncio.models.ecommerce_cart_line_item3 import EcommerceCartLineItem3
from mailchimp_marketing_asyncio.models.ecommerce_cart_line_item4 import EcommerceCartLineItem4
from mailchimp_marketing_asyncio.models.ecommerce_customer import EcommerceCustomer
from mailchimp_marketing_asyncio.models.ecommerce_customer1 import EcommerceCustomer1
from mailchimp_marketing_asyncio.models.ecommerce_customer2 import EcommerceCustomer2
from mailchimp_marketing_asyncio.models.ecommerce_customer3 import EcommerceCustomer3
from mailchimp_marketing_asyncio.models.ecommerce_customer4 import EcommerceCustomer4
from mailchimp_marketing_asyncio.models.ecommerce_customer5 import EcommerceCustomer5
from mailchimp_marketing_asyncio.models.ecommerce_order import EcommerceOrder
from mailchimp_marketing_asyncio.models.ecommerce_order1 import EcommerceOrder1
from mailchimp_marketing_asyncio.models.ecommerce_order2 import EcommerceOrder2
from mailchimp_marketing_asyncio.models.ecommerce_order_line_item import EcommerceOrderLineItem
from mailchimp_marketing_asyncio.models.ecommerce_order_line_item1 import EcommerceOrderLineItem1
from mailchimp_marketing_asyncio.models.ecommerce_order_line_item2 import EcommerceOrderLineItem2
from mailchimp_marketing_asyncio.models.ecommerce_order_line_item3 import EcommerceOrderLineItem3
from mailchimp_marketing_asyncio.models.ecommerce_order_line_item4 import EcommerceOrderLineItem4
from mailchimp_marketing_asyncio.models.ecommerce_product import EcommerceProduct
from mailchimp_marketing_asyncio.models.ecommerce_product1 import EcommerceProduct1
from mailchimp_marketing_asyncio.models.ecommerce_product2 import EcommerceProduct2
from mailchimp_marketing_asyncio.models.ecommerce_product_image import EcommerceProductImage
from mailchimp_marketing_asyncio.models.ecommerce_product_image1 import EcommerceProductImage1
from mailchimp_marketing_asyncio.models.ecommerce_product_image2 import EcommerceProductImage2
from mailchimp_marketing_asyncio.models.ecommerce_product_image3 import EcommerceProductImage3
from mailchimp_marketing_asyncio.models.ecommerce_product_image4 import EcommerceProductImage4
from mailchimp_marketing_asyncio.models.ecommerce_product_images import EcommerceProductImages
from mailchimp_marketing_asyncio.models.ecommerce_product_variant import EcommerceProductVariant
from mailchimp_marketing_asyncio.models.ecommerce_product_variant1 import EcommerceProductVariant1
from mailchimp_marketing_asyncio.models.ecommerce_product_variant2 import EcommerceProductVariant2
from mailchimp_marketing_asyncio.models.ecommerce_product_variant3 import EcommerceProductVariant3
from mailchimp_marketing_asyncio.models.ecommerce_product_variant4 import EcommerceProductVariant4
from mailchimp_marketing_asyncio.models.ecommerce_product_variant5 import EcommerceProductVariant5
from mailchimp_marketing_asyncio.models.ecommerce_product_variants import EcommerceProductVariants
from mailchimp_marketing_asyncio.models.ecommerce_promo_code import EcommercePromoCode
from mailchimp_marketing_asyncio.models.ecommerce_promo_code1 import EcommercePromoCode1
from mailchimp_marketing_asyncio.models.ecommerce_promo_code2 import EcommercePromoCode2
from mailchimp_marketing_asyncio.models.ecommerce_promo_rule import EcommercePromoRule
from mailchimp_marketing_asyncio.models.ecommerce_promo_rule1 import EcommercePromoRule1
from mailchimp_marketing_asyncio.models.ecommerce_promo_rule2 import EcommercePromoRule2
from mailchimp_marketing_asyncio.models.ecommerce_stats import EcommerceStats
from mailchimp_marketing_asyncio.models.ecommerce_store import EcommerceStore
from mailchimp_marketing_asyncio.models.ecommerce_store1 import EcommerceStore1
from mailchimp_marketing_asyncio.models.ecommerce_store2 import EcommerceStore2
from mailchimp_marketing_asyncio.models.ecommerce_stores import EcommerceStores
from mailchimp_marketing_asyncio.models.ecommercestoresstore_idorders_promos import EcommercestoresstoreIdordersPromos
from mailchimp_marketing_asyncio.models.eepurl_activity import EepurlActivity
from mailchimp_marketing_asyncio.models.email_activity import EmailActivity
from mailchimp_marketing_asyncio.models.email_client import EmailClient
from mailchimp_marketing_asyncio.models.email_clients import EmailClients
from mailchimp_marketing_asyncio.models.email_domain import EmailDomain
from mailchimp_marketing_asyncio.models.event import Event
from mailchimp_marketing_asyncio.models.events import Events
from mailchimp_marketing_asyncio.models.events1 import Events1
from mailchimp_marketing_asyncio.models.exact_matches import ExactMatches
from mailchimp_marketing_asyncio.models.facebook_likes import FacebookLikes
from mailchimp_marketing_asyncio.models.file_manager import FileManager
from mailchimp_marketing_asyncio.models.file_manager_folders import FileManagerFolders
from mailchimp_marketing_asyncio.models.forwards import Forwards
from mailchimp_marketing_asyncio.models.gallery_file import GalleryFile
from mailchimp_marketing_asyncio.models.gallery_file1 import GalleryFile1
from mailchimp_marketing_asyncio.models.gallery_file2 import GalleryFile2
from mailchimp_marketing_asyncio.models.gallery_folder import GalleryFolder
from mailchimp_marketing_asyncio.models.gallery_folder1 import GalleryFolder1
from mailchimp_marketing_asyncio.models.gallery_folder2 import GalleryFolder2
from mailchimp_marketing_asyncio.models.goal import Goal
from mailchimp_marketing_asyncio.models.group_a import GroupA
from mailchimp_marketing_asyncio.models.group_b import GroupB
from mailchimp_marketing_asyncio.models.growth_history import GrowthHistory
from mailchimp_marketing_asyncio.models.hours import Hours
from mailchimp_marketing_asyncio.models.industry_stats import IndustryStats
from mailchimp_marketing_asyncio.models.industry_stats1 import IndustryStats1
from mailchimp_marketing_asyncio.models.inline_response200 import InlineResponse200
from mailchimp_marketing_asyncio.models.inline_response2001 import InlineResponse2001
from mailchimp_marketing_asyncio.models.inline_response20010 import InlineResponse20010
from mailchimp_marketing_asyncio.models.inline_response20011 import InlineResponse20011
from mailchimp_marketing_asyncio.models.inline_response20011_audience_activity import InlineResponse20011AudienceActivity
from mailchimp_marketing_asyncio.models.inline_response20011_audience_activity_clicks import InlineResponse20011AudienceActivityClicks
from mailchimp_marketing_asyncio.models.inline_response20011_audience_activity_impressions import InlineResponse20011AudienceActivityImpressions
from mailchimp_marketing_asyncio.models.inline_response20011_audience_activity_revenue import InlineResponse20011AudienceActivityRevenue
from mailchimp_marketing_asyncio.models.inline_response20011_report_summary import InlineResponse20011ReportSummary
from mailchimp_marketing_asyncio.models.inline_response20011_report_summary_average_order_amount import InlineResponse20011ReportSummaryAverageOrderAmount
from mailchimp_marketing_asyncio.models.inline_response20011_report_summary_ecommerce import InlineResponse20011ReportSummaryEcommerce
from mailchimp_marketing_asyncio.models.inline_response20011_report_summary_extended_at import InlineResponse20011ReportSummaryExtendedAt
from mailchimp_marketing_asyncio.models.inline_response20012 import InlineResponse20012
from mailchimp_marketing_asyncio.models.inline_response2001_exports import InlineResponse2001Exports
from mailchimp_marketing_asyncio.models.inline_response2002 import InlineResponse2002
from mailchimp_marketing_asyncio.models.inline_response2002_apps import InlineResponse2002Apps
from mailchimp_marketing_asyncio.models.inline_response2003 import InlineResponse2003
from mailchimp_marketing_asyncio.models.inline_response2004 import InlineResponse2004
from mailchimp_marketing_asyncio.models.inline_response2005 import InlineResponse2005
from mailchimp_marketing_asyncio.models.inline_response2006 import InlineResponse2006
from mailchimp_marketing_asyncio.models.inline_response2007 import InlineResponse2007
from mailchimp_marketing_asyncio.models.inline_response2007_products import InlineResponse2007Products
from mailchimp_marketing_asyncio.models.inline_response2008 import InlineResponse2008
from mailchimp_marketing_asyncio.models.inline_response2009 import InlineResponse2009
from mailchimp_marketing_asyncio.models.inline_response2009_audience import InlineResponse2009Audience
from mailchimp_marketing_asyncio.models.inline_response2009_audience_email_source import InlineResponse2009AudienceEmailSource
from mailchimp_marketing_asyncio.models.inline_response2009_audience_targeting_specs import InlineResponse2009AudienceTargetingSpecs
from mailchimp_marketing_asyncio.models.inline_response2009_audience_targeting_specs_interests import InlineResponse2009AudienceTargetingSpecsInterests
from mailchimp_marketing_asyncio.models.inline_response2009_audience_targeting_specs_locations import InlineResponse2009AudienceTargetingSpecsLocations
from mailchimp_marketing_asyncio.models.inline_response2009_budget import InlineResponse2009Budget
from mailchimp_marketing_asyncio.models.inline_response2009_channel import InlineResponse2009Channel
from mailchimp_marketing_asyncio.models.inline_response2009_content import InlineResponse2009Content
from mailchimp_marketing_asyncio.models.inline_response2009_content_attachments import InlineResponse2009ContentAttachments
from mailchimp_marketing_asyncio.models.inline_response2009_feedback import InlineResponse2009Feedback
from mailchimp_marketing_asyncio.models.inline_response2009_report_summary import InlineResponse2009ReportSummary
from mailchimp_marketing_asyncio.models.inline_response2009_report_summary_ecommerce import InlineResponse2009ReportSummaryEcommerce
from mailchimp_marketing_asyncio.models.inline_response2009_site import InlineResponse2009Site
from mailchimp_marketing_asyncio.models.interest import Interest
from mailchimp_marketing_asyncio.models.interest1 import Interest1
from mailchimp_marketing_asyncio.models.interest2 import Interest2
from mailchimp_marketing_asyncio.models.interest_category import InterestCategory
from mailchimp_marketing_asyncio.models.interest_category1 import InterestCategory1
from mailchimp_marketing_asyncio.models.interest_category2 import InterestCategory2
from mailchimp_marketing_asyncio.models.interest_groupings import InterestGroupings
from mailchimp_marketing_asyncio.models.interests import Interests
from mailchimp_marketing_asyncio.models.landing_page import LandingPage
from mailchimp_marketing_asyncio.models.landing_page1 import LandingPage1
from mailchimp_marketing_asyncio.models.landing_page2 import LandingPage2
from mailchimp_marketing_asyncio.models.landing_page_content import LandingPageContent
from mailchimp_marketing_asyncio.models.landing_page_report import LandingPageReport
from mailchimp_marketing_asyncio.models.landing_page_report_ecommerce import LandingPageReportEcommerce
from mailchimp_marketing_asyncio.models.landing_page_report_timeseries import LandingPageReportTimeseries
from mailchimp_marketing_asyncio.models.last_message import LastMessage
from mailchimp_marketing_asyncio.models.list import List
from mailchimp_marketing_asyncio.models.list1 import List1
from mailchimp_marketing_asyncio.models.list10 import List10
from mailchimp_marketing_asyncio.models.list2 import List2
from mailchimp_marketing_asyncio.models.list3 import List3
from mailchimp_marketing_asyncio.models.list4 import List4
from mailchimp_marketing_asyncio.models.list5 import List5
from mailchimp_marketing_asyncio.models.list6 import List6
from mailchimp_marketing_asyncio.models.list7 import List7
from mailchimp_marketing_asyncio.models.list8 import List8
from mailchimp_marketing_asyncio.models.list9 import List9
from mailchimp_marketing_asyncio.models.list_activity import ListActivity
from mailchimp_marketing_asyncio.models.list_contact import ListContact
from mailchimp_marketing_asyncio.models.list_contact1 import ListContact1
from mailchimp_marketing_asyncio.models.list_contact2 import ListContact2
from mailchimp_marketing_asyncio.models.list_location import ListLocation
from mailchimp_marketing_asyncio.models.list_locations import ListLocations
from mailchimp_marketing_asyncio.models.list_members import ListMembers
from mailchimp_marketing_asyncio.models.list_members1 import ListMembers1
from mailchimp_marketing_asyncio.models.list_members2 import ListMembers2
from mailchimp_marketing_asyncio.models.list_signup_forms import ListSignupForms
from mailchimp_marketing_asyncio.models.list_stats import ListStats
from mailchimp_marketing_asyncio.models.list_webhooks import ListWebhooks
from mailchimp_marketing_asyncio.models.location import Location
from mailchimp_marketing_asyncio.models.location1 import Location1
from mailchimp_marketing_asyncio.models.location2 import Location2
from mailchimp_marketing_asyncio.models.marketing_permission import MarketingPermission
from mailchimp_marketing_asyncio.models.marketing_permission1 import MarketingPermission1
from mailchimp_marketing_asyncio.models.member_activity import MemberActivity
from mailchimp_marketing_asyncio.models.member_activity1 import MemberActivity1
from mailchimp_marketing_asyncio.models.member_activity2 import MemberActivity2
from mailchimp_marketing_asyncio.models.member_activity_events import MemberActivityEvents
from mailchimp_marketing_asyncio.models.member_activity_events1 import MemberActivityEvents1
from mailchimp_marketing_asyncio.models.member_notes import MemberNotes
from mailchimp_marketing_asyncio.models.member_notes1 import MemberNotes1
from mailchimp_marketing_asyncio.models.member_notes2 import MemberNotes2
from mailchimp_marketing_asyncio.models.member_tag import MemberTag
from mailchimp_marketing_asyncio.models.member_tags import MemberTags
from mailchimp_marketing_asyncio.models.members import Members
from mailchimp_marketing_asyncio.models.members_to_addremove_tofrom_a_static_segment import MembersToAddremoveTofromAStaticSegment
from mailchimp_marketing_asyncio.models.members_to_subscribe_unsubscribe_tofrom_a_list_in_batch import MembersToSubscribeUnsubscribeTofromAListInBatch
from mailchimp_marketing_asyncio.models.merge_field import MergeField
from mailchimp_marketing_asyncio.models.merge_field1 import MergeField1
from mailchimp_marketing_asyncio.models.merge_field2 import MergeField2
from mailchimp_marketing_asyncio.models.merge_field_options import MergeFieldOptions
from mailchimp_marketing_asyncio.models.merge_field_options1 import MergeFieldOptions1
from mailchimp_marketing_asyncio.models.merge_field_options2 import MergeFieldOptions2
from mailchimp_marketing_asyncio.models.notes import Notes
from mailchimp_marketing_asyncio.models.open_activity import OpenActivity
from mailchimp_marketing_asyncio.models.open_detail_report import OpenDetailReport
from mailchimp_marketing_asyncio.models.open_locations import OpenLocations
from mailchimp_marketing_asyncio.models.open_locations_locations import OpenLocationsLocations
from mailchimp_marketing_asyncio.models.opens import Opens
from mailchimp_marketing_asyncio.models.operations import Operations
from mailchimp_marketing_asyncio.models.order_lines import OrderLines
from mailchimp_marketing_asyncio.models.orders import Orders
from mailchimp_marketing_asyncio.models.orders1 import Orders1
from mailchimp_marketing_asyncio.models.orders_promos import OrdersPromos
from mailchimp_marketing_asyncio.models.outreach import Outreach
from mailchimp_marketing_asyncio.models.outreach1 import Outreach1
from mailchimp_marketing_asyncio.models.partial_matches import PartialMatches
from mailchimp_marketing_asyncio.models.problem_detail_document import ProblemDetailDocument
from mailchimp_marketing_asyncio.models.products import Products
from mailchimp_marketing_asyncio.models.promo_codes import PromoCodes
from mailchimp_marketing_asyncio.models.promo_rules import PromoRules
from mailchimp_marketing_asyncio.models.rss_options import RSSOptions
from mailchimp_marketing_asyncio.models.rss_options1 import RSSOptions1
from mailchimp_marketing_asyncio.models.rss_options2 import RSSOptions2
from mailchimp_marketing_asyncio.models.rss_options3 import RSSOptions3
from mailchimp_marketing_asyncio.models.referrer import Referrer
from mailchimp_marketing_asyncio.models.removed_subscribers import RemovedSubscribers
from mailchimp_marketing_asyncio.models.resource_link import ResourceLink
from mailchimp_marketing_asyncio.models.salesforce_crm_tracking import SalesforceCRMTracking
from mailchimp_marketing_asyncio.models.salesforce_crm_tracking1 import SalesforceCRMTracking1
from mailchimp_marketing_asyncio.models.script import Script
from mailchimp_marketing_asyncio.models.script1 import Script1
from mailchimp_marketing_asyncio.models.segment_members import SegmentMembers
from mailchimp_marketing_asyncio.models.segment_options import SegmentOptions
from mailchimp_marketing_asyncio.models.segment_options1 import SegmentOptions1
from mailchimp_marketing_asyncio.models.segment_options2 import SegmentOptions2
from mailchimp_marketing_asyncio.models.send_checklist import SendChecklist
from mailchimp_marketing_asyncio.models.send_checklist_items import SendChecklistItems
from mailchimp_marketing_asyncio.models.sending_schedule import SendingSchedule
from mailchimp_marketing_asyncio.models.sending_schedule1 import SendingSchedule1
from mailchimp_marketing_asyncio.models.sent_to import SentTo
from mailchimp_marketing_asyncio.models.share_report import ShareReport
from mailchimp_marketing_asyncio.models.shipping_address import ShippingAddress
from mailchimp_marketing_asyncio.models.shipping_address1 import ShippingAddress1
from mailchimp_marketing_asyncio.models.signup_form import SignupForm
from mailchimp_marketing_asyncio.models.signup_form1 import SignupForm1
from mailchimp_marketing_asyncio.models.signup_form_header_options import SignupFormHeaderOptions
from mailchimp_marketing_asyncio.models.sources import Sources
from mailchimp_marketing_asyncio.models.statistics import Statistics
from mailchimp_marketing_asyncio.models.subscriber_in_automation_queue import SubscriberInAutomationQueue
from mailchimp_marketing_asyncio.models.subscriber_in_automation_queue1 import SubscriberInAutomationQueue1
from mailchimp_marketing_asyncio.models.subscriber_in_automation_queue2 import SubscriberInAutomationQueue2
from mailchimp_marketing_asyncio.models.subscriber_in_automation_queue3 import SubscriberInAutomationQueue3
from mailchimp_marketing_asyncio.models.subscriber_in_customer_journeys_audience import SubscriberInCustomerJourneysAudience
from mailchimp_marketing_asyncio.models.subscriber_list import SubscriberList
from mailchimp_marketing_asyncio.models.subscriber_list1 import SubscriberList1
from mailchimp_marketing_asyncio.models.subscriber_list2 import SubscriberList2
from mailchimp_marketing_asyncio.models.subscriber_lists import SubscriberLists
from mailchimp_marketing_asyncio.models.subscriber_removed_from_automation_workflow import SubscriberRemovedFromAutomationWorkflow
from mailchimp_marketing_asyncio.models.subscriber_stats import SubscriberStats
from mailchimp_marketing_asyncio.models.subscriber_stats1 import SubscriberStats1
from mailchimp_marketing_asyncio.models.tag import Tag
from mailchimp_marketing_asyncio.models.tag_search_results import TagSearchResults
from mailchimp_marketing_asyncio.models.tag_search_results_tags import TagSearchResultsTags
from mailchimp_marketing_asyncio.models.template_content import TemplateContent
from mailchimp_marketing_asyncio.models.template_content1 import TemplateContent1
from mailchimp_marketing_asyncio.models.template_default_content import TemplateDefaultContent
from mailchimp_marketing_asyncio.models.template_folder import TemplateFolder
from mailchimp_marketing_asyncio.models.template_folder1 import TemplateFolder1
from mailchimp_marketing_asyncio.models.template_folder2 import TemplateFolder2
from mailchimp_marketing_asyncio.models.template_folders import TemplateFolders
from mailchimp_marketing_asyncio.models.template_instance import TemplateInstance
from mailchimp_marketing_asyncio.models.template_instance1 import TemplateInstance1
from mailchimp_marketing_asyncio.models.template_instance2 import TemplateInstance2
from mailchimp_marketing_asyncio.models.templates import Templates
from mailchimp_marketing_asyncio.models.tracked_conversations import TrackedConversations
from mailchimp_marketing_asyncio.models.tracking_settings import TrackingSettings
from mailchimp_marketing_asyncio.models.twitter_stats import TwitterStats
from mailchimp_marketing_asyncio.models.twitter_status import TwitterStatus
from mailchimp_marketing_asyncio.models.unsubscribes import Unsubscribes
from mailchimp_marketing_asyncio.models.update_information_about_a_specific_workflow_email import UpdateInformationAboutASpecificWorkflowEmail
from mailchimp_marketing_asyncio.models.upload_archive import UploadArchive
from mailchimp_marketing_asyncio.models.verified_domains import VerifiedDomains
from mailchimp_marketing_asyncio.models.verified_domains1 import VerifiedDomains1
from mailchimp_marketing_asyncio.models.verified_domains2 import VerifiedDomains2
from mailchimp_marketing_asyncio.models.verify_a_domain_for_sending_ import VerifyADomainForSending_
from mailchimp_marketing_asyncio.models.weekly_clicks_and_visits_data import WeeklyClicksAndVisitsData
from mailchimp_marketing_asyncio.models.weekly_clicks_and_visits_data_clicks import WeeklyClicksAndVisitsDataClicks
from mailchimp_marketing_asyncio.models.weekly_clicks_and_visits_data_visits import WeeklyClicksAndVisitsDataVisits
