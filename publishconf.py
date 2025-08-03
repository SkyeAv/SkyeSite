# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL: str = "https://SkyeAv.github.io/SKYESITE"
RELATIVE_URLS: bool = False

FEED_ALL_ATOM: str = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM: str = r"feeds/{slug}.atom.xml"

DELETE_OUTPUT_DIRECTORY: bool = True

# Following items are often useful when publishing

# DISQUS_SITENAME = ""
# GOOGLE_ANALYTICS = ""
