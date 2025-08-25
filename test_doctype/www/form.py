import frappe

def get_context(context):
    doc = frappe.get_doc("Employee", 1)
    context.doc = doc
