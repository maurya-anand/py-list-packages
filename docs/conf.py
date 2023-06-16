# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'list_packages'
copyright = '2023, Anand Maurya'
author = 'Anand Maurya'
release = '1.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',      # Enable automatic documentation generation from docstrings
    'sphinx.ext.autosummary',
    'sphinx.ext.napoleon',     # Support for Google-style docstrings
    'sphinx.ext.intersphinx',  # Support for linking to other documentation
]

autosummary_generate = True
autodoc_mock_imports = ["command_line"]

templates_path = ['_templates']
exclude_patterns = []

# Add the path to your package's source code
# sys.path.insert(0, os.path.abspath('../list_packages'))
sys.path.insert(0, os.path.abspath('..'))

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
