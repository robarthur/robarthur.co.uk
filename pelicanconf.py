#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rob Arthur'
COPYRIGHT_NAME = 'Rob Arthur'
SITEURL = 'https://www.robarthur.co.uk'
SITENAME = 'Rob Arthur | Blog'
SITETITLE = 'Rob Arthur | Blog'
SITESUBTITLE = 'Personal Blog for notes, thoughts and experiments'
SITEDESCRIPTION = 'Personal Blog of Rob Arthur, interested in software development, devops, AWS/Cloud.'
SITELOGO = '//s.gravatar.com/avatar/ed179e15a36dcb39b4e0b91633533499?s=240'
FAVICON = '/images/favicon.ico'

PATH = 'content'
IGNORE_FILES = ['content/draft/*']
STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
MAIN_MENU = True

LINKS = ( )

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/rob-arthur-88016840/'),
          ('github', 'https://github.com/robarthur'),
          ('twitter', 'https://twitter.com/rob_arthur1'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = 10

#Integrations
GOOGLE_ANALYTICS = 'UA-106756061-1'
PYGMENTS_STYLE = 'friendly'

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-themes/Flex'
COPYRIGHT_YEAR = 2020
DEFAULT_PAGINATION = 5

MARKUP = ('md', 'ipynb')
IGNORE_FILES = ['.ipynb_checkpoints']
IPYNB_USE_META_SUMMARY=True
PLUGIN_PATHS = ['./pelican-plugins/']
PLUGINS = ['post_stats','sitemap','pelican-ipynb.markup']

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.6,
        'indexes': 0.6,
        'pages': 0.5,
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly',
    }
}
