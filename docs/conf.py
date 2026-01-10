# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

from dataclasses import asdict
from sphinxawesome_theme import ThemeOptions

project = 'OMW Achievements'
copyright = '2025, sko0malover'
author = 'sko0malover'
release = 'v2.1.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']

html_theme_options = asdict(ThemeOptions(
   awesome_headerlinks=False
))

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'https://gitlab.com/OpenMW/openmw-docs/raw/master/docs/source/_static/images/openmw.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'https://gitlab.com/OpenMW/openmw-docs/raw/master/docs/source/_static/images/favicon.png'
