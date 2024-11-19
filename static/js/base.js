// Theme toggling functionality
const themeToggle = document.getElementById('theme-toggle');
const themeIcon = themeToggle.querySelector('i');

// Check for saved theme preference
const savedTheme = localStorage.getItem('theme') || 'light';
document.documentElement.setAttribute('data-theme', savedTheme);
updateThemeIcon(savedTheme);
updateNavbarTogglerIcon(savedTheme);

// Toggle theme
themeToggle.addEventListener('click', () => {
    const currentTheme = document.documentElement.getAttribute('data-theme');
    const newTheme = currentTheme === 'light' ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
    updateNavbarTogglerIcon(newTheme);
});

function updateThemeIcon(theme) {
    if (theme === 'dark') {
        themeIcon.classList.remove('fa-moon');
        themeIcon.classList.add('fa-sun');
    } else {
        themeIcon.classList.remove('fa-sun');
        themeIcon.classList.add('fa-moon');
    }
}

function updateNavbarTogglerIcon(theme) {
    const root = document.documentElement;
    if (theme === 'dark') {
        root.style.setProperty('--nav-icon-filter', 'invert(1)');
    } else {
        root.style.setProperty('--nav-icon-filter', 'none');
    }
}

// Update year in footer
const currentYear = new Date().getFullYear();
document.querySelector('.year').textContent = currentYear;
