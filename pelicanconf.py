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
    ("GitHub", "https://github.com/yourusername"),
    ("LinkedIn", "https://www.linkedin.com/in/yourprofile"),
    ("Email", "mailto:your@email.com"),
    ("ORCID", "https://orcid.org/0000-0000-0000-0000"),
)

DEFAULT_PAGINATION: int = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME: str = "/Users/skyeavila/pelican-themes/Flex"
THEME_COLOR: str = "default"
PYGMENTS_STYLE: str = "monokai"

PLUGINS: list[str] = [
    "granular_signals",
    "precompress",
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

SITEDESCRIPTION: str = ""
SITELOGO: str = ""
FAVICON: str = ""
BROWSER_COLOR: str = ""

COPYRIGHT_YEAR: int = 2025

SHOW_ARTICLE_AUTHOR: bool = True
SHOW_COPYRIGHT: bool = True
SHOW_RELATIVE_DATES: bool = False

MAIN_MENU: bool = True
MENUITEMS: tuple[tuple[str, str]] = (
    ("Home", "/"),
    ("CV", "/pages/cv.html"),
    ("Blog", "/category/blog.html"),
    ("Projects", "/pages/projects.html"),
    ("Contact", "/pages/contact.html"),
)

STATIC_PATHS: list[str] = ["images", "extra/robots.txt", "extra/favicon.ico"]
EXTRA_PATH_METADATA: dict[str, dict[str, str]] = {
    "extra/robots.txt": {"path": "robots.txt"},
    "extra/favicon.ico": {"path": "favicon.ico"},
}

SEO_REPORT: bool = True
SEO_ENHANCER: bool = True
SEO_ENHANCER_OPEN_GRAPH: bool = True

SITEMAP: dict[str, Union[str, dict[str, float]]] = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "pages": 0.5,
        "indexes": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "pages": "monthly",
        "indexes": "daily",
    },
}

TYPOGRIFY: bool = True  # Smart quotes, dashes, etc.
DEFAULT_METADATA: dict[str, str] = {
    "status": "draft",
}
RELATIVE_URLS: bool = True  # Uncomment during local development
DELETE_OUTPUT_DIRECTORY: bool = True
