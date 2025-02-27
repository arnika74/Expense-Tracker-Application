document.addEventListener("DOMContentLoaded", function () {
    const slides = document.querySelector(".slides");
    const images = slides.querySelectorAll("img");
    const totalImages = images.length;
    
    // Clone first few images for infinite effect
    images.forEach((img) => {
        let clone = img.cloneNode(true);
        slides.appendChild(clone);
    });

    let index = 0;
    const slideWidth = images[0].clientWidth;
    
    function moveSlide() {
        index++;
        slides.style.transition = "transform 1.0s linear"; // Smooth transition
        slides.style.transform = `translateX(-${index * slideWidth}px)`;

        // When reaching the cloned images, reset instantly
        if (index === totalImages) {
            setTimeout(() => {
                slides.style.transition = "none"; // Remove transition
                slides.style.transform = "translateX(0)";
                index = 0;
            }, 1000); // Wait for transition to end
        }
    }

    // Auto move every 2 seconds
    setInterval(moveSlide, 2000);
});


// for password eye icon 
function togglePassword() {
    let passwordInput = document.getElementById("password");
    let toggleEye = document.getElementById("toggleEye");

    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        toggleEye.classList.remove("fa-eye");
        toggleEye.classList.add("fa-eye-slash");
        // toggleEye.setAttribute("data-tooltip", "Hide Password");
    } else {
        passwordInput.type = "password";
        toggleEye.classList.remove("fa-eye-slash");
        toggleEye.classList.add("fa-eye");
        // toggleEye.setAttribute("data-tooltip", "Show Password");
    }
}




// Check login status
function checkLogin() {
    let user = JSON.parse(localStorage.getItem("loggedInUser"));
    if (user) {
        document.getElementById("authOptions").style.display = "none";
        document.getElementById("userProfile").style.display = "flex";
    }
}

// Handle login
document.getElementById("loginForm")?.addEventListener("submit", function (event) {
    event.preventDefault();
    let username = document.getElementById("username").value;
    let password = document.getElementById("password").value;
    let users = JSON.parse(localStorage.getItem("users")) || [];
    
    let user = users.find(user => (user.username === username || user.email === username) && user.password === password);
    
    if (user) {
        localStorage.setItem("loggedInUser", JSON.stringify(user));
        alert("Login successful!");
        window.location.href = "index.html";
    } else {
        alert("Invalid username or password!");
    }
});

// Handle registration
document.getElementById("registerForm")?.addEventListener("submit", function (event) {
    event.preventDefault();
    let newUser = {
        username: document.getElementById("username").value,
        password: document.getElementById("password").value,
        securityKey: document.getElementById("securityKey").value,
        email: document.getElementById("email").value
    };
    
    let users = JSON.parse(localStorage.getItem("users")) || [];
    users.push(newUser);
    localStorage.setItem("users", JSON.stringify(users));
    
    alert("Registration successful!");
    window.location.href = "index.html";
});

// Expense Addition Restriction
document.getElementById("expenseForm")?.addEventListener("submit", function (event) {
    event.preventDefault();
    let user = JSON.parse(localStorage.getItem("loggedInUser"));
    if (!user) {
        alert("You must log in first!");
        return;
    }
    alert("Expense added successfully!");
});

// Balance Check with Security Key
function requestBalanceKey() {
    let user = JSON.parse(localStorage.getItem("loggedInUser"));
    if (!user) {
        alert("You must log in first!");
        return;
    }
    
    let enteredKey = prompt("Enter your security key:");
    if (enteredKey === user.securityKey) {
        alert("Your balance is $1000");
    } else {
        alert("Incorrect security key!");
    }
}


// document.addEventListener("DOMContentLoaded", function () {
//     checkUserStatus();
// });

// // Function to check if user is logged in
// function checkUserStatus() {
//     let isLoggedIn = localStorage.getItem("isLoggedIn");

//     if (isLoggedIn === "true") {
//         document.getElementById("auth-buttons").style.display = "none";
//         document.getElementById("profile-section").style.display = "block";
//     } else {
//         document.getElementById("auth-buttons").style.display = "block";
//         document.getElementById("profile-section").style.display = "none";
//     }
// }

// // Prevent access if not logged in
// function checkLogin() {
//     let isLoggedIn = localStorage.getItem("isLoggedIn");
//     if (isLoggedIn !== "true") {
//         showPopup("Login First!");
//         return false;
//     }
//     return true;
// }

// // Show popup message
// function showPopup(message) {
//     document.getElementById("popup-message").innerText = message;
//     document.getElementById("popup").style.display = "block";
// }

// // Close popup
// function closePopup() {
//     document.getElementById("popup").style.display = "none";
// }

// // Login successful
// function login() {
//     localStorage.setItem("isLoggedIn", "true");
//     showPopup("Login Successful!");
//     setTimeout(() => window.location.href = "index.html", 1500);
// }

// // Logout function
// function logout() {
//     localStorage.removeItem("isLoggedIn");
//     showPopup("Logged Out!");
//     setTimeout(() => window.location.href = "index.html", 1500);
// }

// // Toggle profile menu
// function toggleProfileMenu() {
//     let menu = document.getElementById("profile-menu");
//     menu.style.display = menu.style.display === "block" ? "none" : "block";
// }

