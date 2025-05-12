let navOpen = false;

function toggleNav() {
  const sidenav = document.getElementById("mySidenav");
  const navTexts = document.querySelectorAll('.nav-text');

  if (navOpen) {
    sidenav.style.width = "60px";  // Shrnutí na zobrazení jen ikon
    document.getElementById("main").style.marginLeft = "60px";
    navTexts.forEach(text => text.style.display = 'none');  // Skryj text vedle ikon
  } else {
    sidenav.style.width = "250px";  // Rozbalení s textem
    document.getElementById("main").style.marginLeft = "250px";
    navTexts.forEach(text => text.style.display = 'inline');  // Zobraz text vedle ikon
  }

  navOpen = !navOpen;
}