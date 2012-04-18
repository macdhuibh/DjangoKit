#!/usr/bin/python
from djangokit import setup

setup(
  appname = "wiki",
  prettyname = "DjangoWiki",
  version = "0.2",
  author = "Paul Bissex",
  settings = {
    'WIKI_SITEBASE':'/',
  }
)
