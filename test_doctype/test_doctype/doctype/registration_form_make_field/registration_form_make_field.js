// Copyright (c) 2025, frappe and contributors
// For license information, please see license.txt
frappe.ui.form.on("Registration Form Make Field", {
    first_name(frm) {
        update_full_name(frm);
    },
    last_name(frm) {
        update_full_name(frm);
    }
});

function update_full_name(frm) {
    if (frm.doc.first_name || frm.doc.last_name) {
        frm.set_value("full_name", (frm.doc.first_name || '') + " " + (frm.doc.last_name || ''));
    }
}

