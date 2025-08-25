# Copyright (c) 2025, frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class ScriptBothServerTest(Document):
	pass

# File: test_doctype/test_doctype/doctype/script_both_server_test/script_both_server_test.py

# import frappe

# @frappe.whitelist()
# def xdc(name, age):
#     doc = frappe.new_doc('Script Both Server Test')
#     doc.phone_number = 93434
#     doc.save()
#     if frappe.db.exists('Script Both Server Test', {'name': 'Tharun'}):
#     t = frappe.msgprint('Customer already exists')
#     return f"Hello {name}, you are {age} years old. {t}"

import frappe

@frappe.whitelist()
def xdc(name, age):
    # Create new doc
    doc = frappe.new_doc('Script Both Server Test')
    doc.name1 = name  # Use a field that exists in your doctype
    doc.age = age
    doc.phone_number = 93434  # Ensure this field exists
    doc.save()

    # Check if a doc with same name1 exists (not the `name` field)
    exists = frappe.db.exists('Script Both Server Test', {'name1': name})
    if exists:
        message = 'Record already exists'
        # frappe.log_error(title=f"{message}" message=f"{doc}")
    else:
        message = 'Record created successfully'

    return f"Hello {name}, you are {age} years old. {message}"


