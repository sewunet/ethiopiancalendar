import frappe
from frappe.utils import cint

def boot_session(bootinfo):
    if frappe.session["user"] != "Guest":
        bootinfo.ethiopian_date_datepicker_format = frappe.db.get_single_value("Ethiopian Date Settings", "ethiopian_date_datepicker_format")
        bootinfo.ethiopian_date_format = frappe.db.get_single_value("Ethiopian Date Settings", "ethiopian_date_format")

def bootinfo(bootinfo):
    if frappe.session["user"] != "Guest":
        bootinfo.ethiopian_date_datepicker_format = frappe.db.get_single_value("Ethiopian Date Settings", "ethiopian_date_datepicker_format")
        bootinfo.ethiopian_date_format = frappe.db.get_single_value("Ethiopian Date Settings", "ethiopian_date_format")
