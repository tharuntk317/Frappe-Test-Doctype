# Copyright (c) 2025, frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class SharmilaScriptTest(Document):
	pass

@frappe.whitelist()
def sharmila(z,x):
    r= int(x) + 100
    return z,r

# @frappe.whitelist(allow_gust=0)
# def tharun():
#    return frappe.msgprint('tjhsddc')