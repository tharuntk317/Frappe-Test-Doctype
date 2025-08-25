app_name = "test_doctype"
app_title = "Test Doctype"
app_publisher = "frappe"
app_description = "Test_Doctype"
app_email = "f@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "test_doctype",
# 		"logo": "/assets/test_doctype/logo.png",
# 		"title": "Test Doctype",
# 		"route": "/test_doctype",
# 		"has_permission": "test_doctype.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/test_doctype/css/test_doctype.css"
# app_include_js = "/assets/test_doctype/js/test_doctype.js"

# include js, css files in header of web template
# web_include_css = "/assets/test_doctype/css/test_doctype.css"
# web_include_js = "/assets/test_doctype/js/test_doctype.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "test_doctype/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "test_doctype/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "test_doctype.utils.jinja_methods",
# 	"filters": "test_doctype.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "test_doctype.install.before_install"
# after_install = "test_doctype.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "test_doctype.uninstall.before_uninstall"
# after_uninstall = "test_doctype.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "test_doctype.utils.before_app_install"
# after_app_install = "test_doctype.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "test_doctype.utils.before_app_uninstall"
# after_app_uninstall = "test_doctype.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "test_doctype.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"test_doctype.tasks.all"
# 	],
# 	"daily": [
# 		"test_doctype.tasks.daily"
# 	],
# 	"hourly": [
# 		"test_doctype.tasks.hourly"
# 	],
# 	"weekly": [
# 		"test_doctype.tasks.weekly"
# 	],
# 	"monthly": [
# 		"test_doctype.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "test_doctype.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "test_doctype.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "test_doctype.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["test_doctype.utils.before_request"]
# after_request = ["test_doctype.utils.after_request"]

# Job Events
# ----------
# before_job = ["test_doctype.utils.before_job"]
# after_job = ["test_doctype.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"test_doctype.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }
# -----------------------------Website Context ----------------------------------

website_context = {
    "favicon": "/assets/test_doctype/image/t_img.png"
}
# # hooks.py
# def get_current_year():
#     import datetime
#     return datetime.datetime.now().year

# website_context = {
#     "get_current_year": get_current_year
# }

# -----------------------------Website Controller Context ----------------------------------


# extend_website_page_controller_context = {
#     "frappe.www.404": "test_doctype.www.404.get_context"
# }

# -----------------------------website_redirects ----------------------------------


# website_redirects = [
#     {"source": "/", "target": "/form"},
# ]

# website_redirects = [
#     {"source": "/docs(/.*)?", "target": "https://www.youtube.com/\\1"},
# ]

# website_redirects = [
#      {"source": r'/playlist\?list=(.*)', 
#       "target": 'https://www.youtube.com/@frappeschool', 
#       "match_with_query_string" : True},
# ]

# -----------------------------website_route_rules ----------------------------------

# website_route_rules = [
#     {"from_route": "/emp/<name>", "to_route": "test_doctype.project.project"}
# ]
# website_route_rules = [
#     {"from_route": "/emp/<emp_name>", "to_route": "project"}
# ]


# -----------------------------website_path_resolver ----------------------------------


# website_path_resolver = "test_doctype.utils.custom_resolver"

# -----------------------------website_catch_all----------------------------------

# website_catch_all = "test_doctype.www.not_found"

# -----------------------------homepage----------------------------------


# homepage = "homepage"


# --------------------------------------------=portal_menu_items=----------------------------------

# portal_menu_items = [
#     {"title": "Dashboard", "route": "/dashboard", "role": "Administrator"},
#     {"title": "Orders", "route": "/orders", "role": "Administrator"},
# ]

# brand_html = '<div><img src="/assets/test_doctype/images/a_icon.jpg" style="height:30px; width:auto;"/> TennisMart</div>'

brand_html = """
<div style="display: flex; align-items: center; gap: 12px;">
    <!-- Logo + Title -->
    <div style="display: flex; align-items: center; gap: 6px;">
        <img src="/assets/test_doctype/images/a_icon.jpg" style="height:30px; width:auto;"/>
        <span style="font-weight: bold; font-size: 18px;">TennisMart</span>
    </div>

    <!-- Search Bar -->
    <div style="margin-left: 20px;">
        <input type="text" placeholder="Search..." 
               style="padding:5px 10px; border:1px solid #ccc; border-radius:6px;"/>
    </div>

    <!-- Extra Nav Links -->
    <div style="margin-left: auto; display:flex; gap:15px;">
        <a href="/about" style="text-decoration:none; color:#333;">About</a>
        <a href="/contact" style="text-decoration:none; color:#333;">Contact</a>
        <a href="/help" style="text-decoration:none; color:#333;">Help</a>
    </div>
</div>
"""



# base_template = "test_doctype/templates/my_custom_base.html"





