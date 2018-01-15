#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Edmundo Sanchez'
SITENAME = 'fauxcoup'
SITEURL = ''

PATH = 'content'
USE_FOLDER_AS_CATEGORY = False

TIMEZONE = 'America/Mexico_City'

#My settings
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = True
SITESUBTITLE = "Aprende conmigo"
GITHUB_URL = "https://github.com/gdledsan/fauxcoup"
DEFAULT_DATE = 'fs'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites']
#JINJA_EXTENSIONS = ['jinja2.ext.i18n']

# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'FauxCoup',
        'THEME':'themes/nmi'
        },
    'es': {
        'SITENAME': 'FauxCoup',
        'THEME':'themes/nmi.ES'
        },
    'fr': {
        'SITENAME': 'FauxCoup',
        'THEME':'themes/nmi.FR'
        }
    }

#themes
THEME_STATIC_DIR = 'themes'
THEME = 'themes/nmi'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
