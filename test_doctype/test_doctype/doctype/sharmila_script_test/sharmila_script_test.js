// Copyright (c) 2025, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on("Sharmila Script Test", {
    refresh(frm) {
        frm.add_custom_button('sharmila', () => {
            frappe.call({
                method: "test_doctype.test_doctype.doctype.sharmila_script_test.sharmila_script_test.sharmila",
                args: {
                    z: frm.doc.name1,
                    x: frm.doc.age
                },
                callback: function (r) {
                    if (r.message) {
                        frappe.msgprint('Server responded: ' + r.message);
                        document.body.style.backgroundColor = 'blue';
                    }
                }
            });
        });
    },
});

