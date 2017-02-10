# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "library_managment"
app_title = "LMS"
app_publisher = "myself"
app_description = "Library Managment"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "utpal@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/library_managment/css/library_managment.css"
# app_include_js = "/assets/library_managment/js/library_managment.js"

# include js, css files in header of web template
# web_include_css = "/assets/library_managment/css/library_managment.css"
# web_include_js = "/assets/library_managment/js/library_managment.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "library_managment.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "library_managment.install.before_install"
# after_install = "library_managment.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "library_managment.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"library_managment.tasks.all"
# 	],
# 	"daily": [
# 		"library_managment.tasks.daily"
# 	],
# 	"hourly": [
# 		"library_managment.tasks.hourly"
# 	],
# 	"weekly": [
# 		"library_managment.tasks.weekly"
# 	]
# 	"monthly": [
# 		"library_managment.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "library_managment.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "library_managment.event.get_events"
# }

