from typing import Union

AUTHOR: str = "Skye Lane Goetz"
SITENAME: str = "Skye Lane Goetz - Data Scientist & Bio-Cheminformatician"
SITEURL: str = ""

PATH: str = "content"

TIMEZONE: str = "US/Pacific"

DEFAULT_LANG: str = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM: None = None
CATEGORY_FEED_ATOM: None = None
TRANSLATION_FEED_ATOM: None = None
AUTHOR_FEED_ATOM: None = None
AUTHOR_FEED_RSS: None = None

# Blogroll
LINKS: tuple[tuple[str, str]] = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL: tuple[tuple[str, str]] = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION: int = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

PLUGINS: list[str] = [
    "granular_signals" "precompress",
    "search",
    "seo",
    "share_post",
    "sitemap",
    "webassets",
    "yaml_metadata",
]

MARKDOWN: dict[str, Union[str, dict[str, dict[str, str]]]] = {
    "extension_configs": {"markdown.extensions.meta": {}},
    "output_format": "html5",
}
