#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Friedl De Groote'
SITENAME = 'Research - Friedl De Groote'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = 'EN'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Specify a customized theme, via absolute path
#THEME = "C:/Users/u0088756/Documents/Software/WebPage/PelicanThemesGit/~/pelican-themes/blueidea"

 # AVATAR = 'images//PastFoto_Friedl.jpg'

# Social widget
#DEFAULT_PAGINATION = 2

# Pages
#DISPLAY_PAGES_ON_MENU = True 
#STATIC_PATHS  = ['siteImages']

# Nice and simple theme
#THEME = 'C:/Users/u0088756/Documents/Software/WebPage/PelicanThemesGit/~/pelican-themes/built-texts'

#Second theme
#THEME = 'C:/Users/u0088756/Documents/Software/WebPage/PelicanThemesGit/~/pelican-themes/tuxlite_tbs'
THEME = 'C:/Users/u0088756/Documents/Software/WebPage/PelicanThemesGit/~/pelican-themes/pelican-bootstrap3'

JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

PLUGIN_PATHS = ['C:/Users/u0088756/Documents/Software/WebPage/pelican-plugins'] 
PLUGINS = ['i18n_subsites']

LINKS_WIDGET_NAME = 'Research'


# Maths
# PLUGINS ={'render-math'}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
