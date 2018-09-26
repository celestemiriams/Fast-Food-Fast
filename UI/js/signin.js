function validate() {
    var user_type = document.getElementById("user_type");
    if ( user_type.value === "admin") {
        alert("Welcome! You Have Successfully logged-in as admin");
        window.location = 'admin-dashboard.html';
        return false
    }else {
        alert("Welcome! You Have Successfully logged-in as a client");
        window.location = 'user-dashboard.html';
        return false
    }
}