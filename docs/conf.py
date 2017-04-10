import os
import sys

sys.path.insert(0, os.path.abspath('..'))

from datagovsg_api import __version__


project = 'datagovsg_api'
copyright = '2017, Ray Chen'
author = 'Ray Chen'
version = __version__

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon']
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
napoleon_google_docstring = True

language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False

html_theme = 'sphinx_rtd_theme'
htmlhelp_basename = 'datagovsg_apidoc'
