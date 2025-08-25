import frappe

def get_context(context):
    # requested path
    path = frappe.local.request.path

    context.message = f"Oops! The page '{path}' was not found."
    return context
