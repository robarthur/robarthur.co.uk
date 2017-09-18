#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Rob Arthur'
COPYRIGHT_NAME = 'Rob Arthur'
SITEURL = 'robarthur.co.uk'
SITENAME = 'Rob Arthur'
SITETITLE = 'Rob Arthur'
SITESUBTITLE = 'Personal Blog for notes, thoughts and experiments'
SITEDESCRIPTION = 'Personal Blog of Rob Arthur, interested in software development, devops, AWS/Cloud.'
SITELOGO = 'http://s.gravatar.com/avatar/ed179e15a36dcb39b4e0b91633533499?s=240'
FAVICON = '/images/favicon.ico'

PATH = 'content'
STATIC_PATHS = ['images', 'extra']

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ( )

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/rob-arthur-88016840/'),
          ('github', 'https://github.com/robarthur'),
          ('twitter', 'https://twitter.com/rob_arthur1'))

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'themes/flex'
COPYRIGHT_YEAR = 2017

PLUGIN_PATHS = ['./pelican-plugins']
PLUGINS = ['representative_image']