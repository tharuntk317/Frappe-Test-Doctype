// Copyright (c) 2025, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Email Sender For Verification", {
    refresh(frm) {
        frm.add_custom_button('Send_Email', () => {
            frappe.call({
    method: "test_doctype.test_doctype.doctype.email_sender_for_verification.email_sender_for_verification.email_sender",
    args: {
        doctype: frm.doc.doctype,
        name: frm.doc.name
    },
    callback: (r) => {
        if (r.message) {
            frappe.msgprint("This From Server Side: " + r.message);
        }
    }
});

        });
    },
});

