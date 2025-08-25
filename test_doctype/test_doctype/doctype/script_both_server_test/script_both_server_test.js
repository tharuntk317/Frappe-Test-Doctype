// Copyright (c) 2025, frappe and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Script Both Server Test", {
// 	refresh(frm) {
//         frm.add_custom_button('Click Me',()=>{
//             // frappe.msgprint('Hellow World')
//             frappe.call('test_doctype.test_doctype.doctype.script_both_server_test.script_both_server_test.script'){
//                 method:xdc,
//                 arg:{
//                  name:frm.doc.name,
//                  age:frm.doc.age,
//                 }

//             }

//         })
// 	},
// });

// frappe.ui.form.on("Script Both Server Test", {
//     refresh(frm) {
//         frm.add_custom_button('Click Me', () => {
//             frappe.call({
//                 method: 'test_doctype.test_doctype.doctype.script_both_server_test.script_both_server_test.xdc',
//                 args: {
//                     name: frm.doc.name,
//                     age: frm.doc.age
//                 },
//                 callback: function(r) {
//                     if (r.message) {
//                         frappe.msgprint('Server responded: ' + r.message);
//                     }
//                 },
//                 bg.color : red
//             });
//         });
//     }
// });

frappe.ui.form.on("Script Both Server Test", {
    refresh(frm) {
        frm.add_custom_button('Click Me', () => {
            frappe.call({
                method: 'test_doctype.test_doctype.doctype.script_both_server_test.script_both_server_test.xdc',
                args: {
                    name: frm.doc.name,
                    age: frm.doc.age || 0
                },
                callback: function(r) {
                    if (r.message) {
                        frappe.msgprint('Server responded: ' + r.message);

                        // Change the background color of the body
                        document.body.style.backgroundColor = 'red';
                    }
                }
            });
        });
    }
});

