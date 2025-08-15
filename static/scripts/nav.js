let navOpen = false;

function toggleNav() {
  const sidenav = document.getElementById("mySidenav");
  const main = document.getElementById("main");

  if (navOpen) {
    sidenav.classList.remove('expanded');
    main.classList.remove('expanded');
  } else {
    sidenav.classList.add('expanded');
    main.classList.add('expanded');
  }

  navOpen = !navOpen;
}

// Enhanced navigation with keyboard support
document.addEventListener('DOMContentLoaded', function() {
  // Add keyboard navigation
  document.addEventListener('keydown', function(e) {
    if (e.key === 'Escape' && navOpen) {
      toggleNav();
    }
  });

  // Smooth hover effects
  const navLinks = document.querySelectorAll('.sidenav a');
  navLinks.forEach(link => {
    link.addEventListener('mouseenter', function() {
      this.style.transform = 'translateX(4px)';
    });
    
    link.addEventListener('mouseleave', function() {
      this.style.transform = 'translateX(0)';
    });
  });
});