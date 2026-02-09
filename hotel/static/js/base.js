function openLogoutModal() {
    document.getElementById("logoutModal").style.display = "flex";
}

function closeLogoutModal() {
    document.getElementById("logoutModal").style.display = "none";
}

// close if clicked outside
window.onclick = function(e) {
    const modal = document.getElementById("logoutModal");
    if (e.target === modal) {
        modal.style.display = "none";
    }
}
