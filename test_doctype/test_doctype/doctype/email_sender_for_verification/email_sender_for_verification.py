
import frappe
from frappe.model.document import Document


class EmailSenderForVerification(Document):
	pass

@frappe.whitelist()
def email_sender(doctype=None, name=None):
    doc = frappe.get_doc(doctype, name)
    if getattr(doc, "email", None):
        frappe.sendmail(
            recipients=[doc.email],
            subject="Verification Email",
            message=f"Hello, this is a test verification for {doc.name}.",
            now=True
        )
        return "Success"
    else:
        return "No email field found in this document"



# @frappe.whitelist()
# def email_sender(doctype=None,name=None):
#     doc = frappe.get_doc(doctype,name)
#     return doc.name