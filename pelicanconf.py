#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Naoto Yamaguchi'
SITENAME = "nafoto'z_blog"
SITEURL = ''
SITELOGO = 'https://paper-attachments.dropbox.com/s_8FAC27AC251845FE76C63F0EAF156DF8B3F4D3C17D70B16D9D9AEE81A162B247_1559875512584_profile_dubai.jpg'
FAVICON = SITEURL + '/images/favicon_dna.ico'

PATH = 'content'

TIMEZONE = 'Asia/Tokyo'

DEFAULT_LANG = 'ja'

THEME='../pelican-themes/Flex'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Home', SITEURL),
        ('Twitter', 'http://twitter.com/nafoto_z'),
         ('立替たろう', 'http://tatekaetaro.work/'))
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ['../pelican-plugins']
PLUGINS = ['render_math']

#PLUGIN_PATH = ['../pelican-plugins']
#PLUGINS = ['render_math']
