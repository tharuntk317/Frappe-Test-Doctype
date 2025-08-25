import frappe

def get_context(context):
    context.title = "Welcome to My Website"
    context.my_name = "Tharun Kumar"
    context.my_age = 21
    context.image = "/assets/test_doctype/image/error.png"  # ✅ correct path for public files
    return context
