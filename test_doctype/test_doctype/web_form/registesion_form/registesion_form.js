frappe.ready(function () {
    document.body.style.backgroundColor = "#e0f0ff";
    document.body.style.transition = "background-color 1s ease";
    const header = document.createElement("div");
    header.innerHTML = "<h2 style='text-align:center; color: #004080;'>Welcome to Registration</h2>";
    header.style.padding = "10px";
    header.style.backgroundColor = "#cce5ff";
    header.style.borderBottom = "2px solid #004080";
    header.style.animation = "fadeIn 1s";
    const footer = document.createElement("div");
    footer.innerHTML = "<p style='text-align:center; color: #004080;'>© 2025 MyApp. All Rights Reserved.</p>";
    footer.style.padding = "10px";
    footer.style.backgroundColor = "#cce5ff";
    footer.style.borderTop = "2px solid #004080";
    footer.style.position = "fixed";
    footer.style.bottom = 0;
    footer.style.width = "100%";
    footer.style.animation = "fadeIn 1s";
    document.body.prepend(header);
    document.body.appendChild(footer);
    const style = document.createElement("style");
    style.innerHTML = `
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(-10px); }
            to { opacity: 1; transform: translateY(0); }
        }
    `;
    document.head.appendChild(style);
});
