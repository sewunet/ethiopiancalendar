app_name = "ethiopiancalendar"
app_title = "Ethiopian Calendar"
app_publisher = "Sewunet Abebaw"
app_description = "The Ethiopian calendar is quite different from the Gregorian calendar, with 13 months (12 months of 30 days and a 13th month of 5 or 6 days in a leap year). Integrating this requires careful consideration of how dates are displayed, stored, and processed within Frappe."
app_email = "sewunet92@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ethiopiancalendar",
# 		"logo": "/assets/ethiopiancalendar/logo.png",
# 		"title": "Ethiopian Calendar",
# 		"route": "/ethiopiancalendar",
# 		"has_permission": "ethiopiancalendar.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ethiopiancalendar/css/ethiopiancalendar.css"
# app_include_js =  "/assets/ethiopiancalendar/js/eth-date-picker.js"
app_include_css = ["/assets/ethiopiancalendar/css/ethiopian_calendar.css",
                   "/assets/ethiopiancalendar/css/eth_switcher.css"]
# app_include_js = "/assets/ethiopiancalendar/js/datepicker.min.js"

app_include_js = [
    "/assets/ethiopiancalendar/js/jquery.plugin.js",
    "/assets/ethiopiancalendar/js/jquery.calendars.js",
    "/assets/ethiopiancalendar/js/jquery.calendars.plus.js",
    "/assets/ethiopiancalendar/js/ethiopian_calendar.js",
    "/assets/ethiopiancalendar/js/ethiopian_date_control.js"
    ]
 
# boot_session = "ethiopiancalendar.ethiopian_calendar.ethiopian_calendar_configure.boot_session"
# extend_bootinfo = [
# 	"ethiopiancalendar.ethiopian_calendar.ethiopian_calendar_configure.bootinfo",
# ]
# include js, css files in header of web template
# web_include_css = "/assets/ethiopiancalendar/css/ethiopiancalendar.css"
# web_include_js = "/assets/ethiopiancalendar/js/ethiopiancalendar.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ethiopiancalendar/public/scss/website"

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
# app_include_icons = "ethiopiancalendar/public/icons.svg"

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
# 	"methods": "ethiopiancalendar.utils.jinja_methods",
# 	"filters": "ethiopiancalendar.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ethiopiancalendar.install.before_install"
# after_install = "ethiopiancalendar.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ethiopiancalendar.uninstall.before_uninstall"
# after_uninstall = "ethiopiancalendar.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ethiopiancalendar.utils.before_app_install"
# after_app_install = "ethiopiancalendar.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ethiopiancalendar.utils.before_app_uninstall"
# after_app_uninstall = "ethiopiancalendar.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ethiopiancalendar.notifications.get_notification_config"

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
# 		"ethiopiancalendar.tasks.all"
# 	],
# 	"daily": [
# 		"ethiopiancalendar.tasks.daily"
# 	],
# 	"hourly": [
# 		"ethiopiancalendar.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ethiopiancalendar.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ethiopiancalendar.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ethiopiancalendar.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ethiopiancalendar.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ethiopiancalendar.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ethiopiancalendar.utils.before_request"]
# after_request = ["ethiopiancalendar.utils.after_request"]

# Job Events
# ----------
# before_job = ["ethiopiancalendar.utils.before_job"]
# after_job = ["ethiopiancalendar.utils.after_job"]

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
# 	"ethiopiancalendar.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

