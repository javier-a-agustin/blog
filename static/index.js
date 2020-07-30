function setTheme(themeName) {
    localStorage.setItem('theme', themeName);
    document.documentElement.className = themeName;
}

// function to toggle between light and dark theme
function toggleTheme() {
    if (localStorage.getItem('theme') === 'tema-dark') {
        setTheme('tema-light');
    } else {
        setTheme('tema-dark');
    }
}

// Immediately invoked function to set the theme on initial load
(function () {
    if (localStorage.getItem('theme') === 'tema-dark') {
        setTheme('tema-dark');
    } else {
        setTheme('tema-light');
    }
})();