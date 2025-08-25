// Copyright (c) 2025, frappe and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Total Find Out Doctype", {
// quentity(frm){
//     update(frm)
// },
// amount(frm){
//     update(frm)
// }
// });

// function update(frm){
//     v = frm.doc.quentity || 0
//     b = frm.doc.amount || 0
//     frm.set_value(frm.doc.result = v * b)
// }

// frappe.ui.form.on("Total Find Out Doctype", {
//     validate:function(frm){
//    if(frm.doc.name1){
//     quantity(frm) {
//         update_total(frm);
//     },
//     amount(frm) {
//         update_total(frm);
//     }
//     }
//     }
 
// });

// function update_total(frm) {
//     let qty = frm.doc.quantity || 0;
//     let amt = frm.doc.amount || 0;
//     frm.set_value('result', qty * amt);
// }

// frappe.ui.form.on("Total Find Out Doctype", {
//     // Trigger on quantity change
//     quantity(frm) {
//         update_total(frm);
//     },

//     // Trigger on amount change
//     amount(frm) {
//         update_total(frm);
//     },

//     // Optional: Trigger on validate to recalculate before save
//     validate(frm) {
//         if (frm.doc.name1) {
//             update_total(frm);
//         }
//     }
// });

// // Function to calculate result = quantity * amount
// function update_total(frm) {
//     let qty = frm.doc.quantity || 0;
//     let amt = frm.doc.amount || 0;
//    frappe.new_doc( frm.set_value('result', qty * amt))
// }


// frappe.ui.form.on("Total Find Out Doctype", {
//     // Trigger on quantity change
//     quantity(frm) {
//         update_total(frm);
//     },

//     // Trigger on amount change
//     amount(frm) {
//         update_total(frm);
//     },

//     // Trigger on validate
//     validate(frm) {
//         if (frm.doc.name1) {
//             update_total(frm);
//         }
//     }
// });

// // Function to calculate result = quantity * amount
// function update_total(frm) {
//     let qty = frm.doc.quantity || 0;
//     let amt = frm.doc.amount || 0;
//     s = qty * amt
//     frm.set_value(result, s);
// }

// frappe.ui.form.on("Total Find Out Doctype", {
//     quantity(frm) {
//     frappe.msgprint(frm.quantity);


//         // update_total(frm);

//     },
//     amount(frm) {
//         // update_total(frm);
//     frappe.msgprint(frm.amount);

//     },
//     validate(frm) {
//         if (frm.doc.name1) {
//             // update_total(frm);
//         }
//     }
// });
// function update_total(d,c) {
//     // let qty = frm.doc.quantity || 0;
//     // let amt = frm.doc.amount || 0;
//     // let s = qty * amt;
//     let s = int(d) * int(c)
//     frappe.msgprint(`Result is: ${s}`);
//     // frm.set_value('result', s);

//     // Optional: show value as message safely
//     // frappe.msgprint(`Result is: ${s}`);
// }

// frappe.ui.form.on("Total Find Out Doctype", {
//     quantity(frm) {
//      let  d = frm.doc.quantity
//         // frappe.msgprint(`Quantity entered: ${frm.doc.quantity}`);
//         update_total(d);
//     },
//     amount(frm) {
//         // frappe.msgprint(`Amount entered: ${frm.doc.amount}`);
//         let c = frm.doc.amount
//         update_total(c);
//     }
// });

// frappe.ui.form.on('Total Find Out Doctype',{
//     refresh:function(frm){
//         t = frm.doc.quentity * frm.doc.amount
//         frappe.msgprint(frm.set_value(frm.doc.result , t))
//     }
// })

// frappe.ui.form.on('Total Find Out Doctype', {
//     refresh: function(frm) {
//         let qty = frm.doc.quentity || 0;
//         let amt = frm.doc.amount || 0;
//         let total = qty * amt;

//         frm.set_value('result', total);  // ✅ Correct fieldname usage
//         frappe.msgprint(`Total = ${total}`);  // ✅ Correct message
//     }
// });


// frappe.ui.form.on('Total Find Out Doctype', {
//     quantity(frm) {
//         show_total(frm);
//     },
//     amount(frm) {
//         show_total(frm);
//     }
// });

// function show_total(frm) {
//     let qty = frm.doc.quantity || 0;
//     let amt = frm.doc.amount || 0;
//     let total = qty * amt;

//     frm.set_value('result', total);

//     // Optional: Show in popup after both values are non-zero
//     if (qty && amt) {
//         frappe.msgprint(`Total = ${total}`);
//     }
// }

// frappe.ui.form.on('Total Find Out Doctype', {
//     refresh(frm) {
//         frm.add_custom_button("Check Result", () => {
//             frappe.msgprint(`Result = ${frm.doc.result}`);
//         });
//     },
//     quantity(frm) {
//         show_total(frm);
//     },
//     amount(frm) {
//         show_total(frm);
//     }
// });

// function show_total(frm) {
//     let qty = frm.doc.quantity || 0;
//     let amt = frm.doc.amount || 0;
//     let total = qty * amt;
//     frappe.msgprint(total)
// }

frappe.ui.form.on('Total Find Out Doctype', {
    refresh(frm) {
        frm.add_custom_button("Check Result", () => {
            frappe.msgprint(`Result = ${frm.doc.result}`);
        });
    },
    quentity(frm) {
        show_total(frm);
    },
    amount(frm) {
        show_total(frm);
    }
});

function show_total(frm) {
    let qty = frm.doc.quentity || 0;
    let amt = frm.doc.amount || 0;
    let total = qty * amt;

    // ✅ Save total to the result field
    frm.set_value('result', total);
    
}



