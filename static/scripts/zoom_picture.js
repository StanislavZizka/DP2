document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("popupContainer").style.display = "none"; // Ujistí se, že pop-up je při načtení skrytý
});

function openPopup(imgElement) {
    const popup = document.getElementById("popupContainer");
    const popupImg = document.getElementById("popupImage");

    popupImg.src = imgElement.src;
    popup.style.display = "flex"; // Otevře pop-up
}

function closePopup(event) {
    const popup = document.getElementById("popupContainer");
    
    // Zavře se při kliknutí mimo obrázek nebo na křížek
    if (event?.target.classList.contains("popup") || event?.target.classList.contains("popup-close")) {
        popup.style.display = "none";
    }
}

// Zachytí klávesu ESC a zavře pop-up
document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") { 
        document.getElementById("popupContainer").style.display = "none";
    }
});
