// Highlight empty inputs on submit
document.addEventListener("DOMContentLoaded", () => {
    const form = document.querySelector("form");
    if (!form) return;

    form.addEventListener("submit", (e) => {
        let valid = true;
        const inputs = form.querySelectorAll("input[type='number']");
        inputs.forEach(input => {
            if (input.value === "" || isNaN(input.value)) {
                input.style.border = "2px solid #ff6b6b";
                valid = false;
            } else {
                input.style.border = "2px solid #4cd137";
            }
        });

        if (!valid) {
            e.preventDefault();
            alert("⚠️ Please fill in all fields with valid numbers before submitting!");
        }
    });
});
