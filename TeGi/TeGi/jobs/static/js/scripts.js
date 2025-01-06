// Optional for future enhancements
document.addEventListener('DOMContentLoaded', function() {
    // Add form validation for login and registration
    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', function(event) {
            const email = this.querySelector('input[type="email"]');
            const password = this.querySelector('input[type="password"]');

            // Simple validation
            if (email && !validateEmail(email.value)) {
                alert('Please enter a valid email address.');
                event.preventDefault(); // Prevent form submission
            }

            if (password && password.value.length < 6) {
                alert('Password must be at least 6 characters long.');
                event.preventDefault(); // Prevent form submission
            }
        });
    });

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/; // Simple regex for email validation
        return re.test(String(email).toLowerCase());
    }
});


document.addEventListener('DOMContentLoaded', () => {
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    burger.addEventListener('click', () => {
        navLinks.classList.toggle('active');
        burger.classList.toggle('toggle');
    });
});
