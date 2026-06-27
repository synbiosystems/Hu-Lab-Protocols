project = "Hu Lab Protocols"
author = "Hu Lab"
copyright = "2026, Hu Lab"

extensions = [
    "sphinx_rtd_theme",
    "myst_parser",
]

html_theme = "sphinx_rtd_theme"

html_static_path = ["_static"]

html_css_files = [
    "css/custom.css",
]

html_logo = "_static/lab_logo.png"

html_theme_options = {
    "collapse_navigation": False,
    "navigation_depth": 4,
    "style_nav_header_background": "#2c6854",
    "prev_next_buttons_location": "bottom",
}
