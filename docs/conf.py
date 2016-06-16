# -*- coding: utf-8 -*-
# conf.py ... http://docs.sphinx-users.jp/config.html

import sys, os
from recommonmark.parser import CommonMarkParser

extensions = []

source_suffix = ['.rst', '.md']
source_parsers = {
    '.md': CommonMarkParser,
}

master_doc = 'index'
exclude_patterns = []
templates_path = ['_templates']

project = u'pdfminer-docs'
copyright = u'2016, Levia3'

version = '0'
release = '0.0.1'

pygments_style = 'sphinx'

html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'pdfminer-doc'

latex_documents = [
  ('index', 'pdfminer.tex', u'pdfminer',
   u'Levia3', 'manual'),
]

man_pages = [
    ('index', 'pdfminer', u'pdfminer',
     [u'Levia3'], 1)
]

epub_title = u'pdfminer'
