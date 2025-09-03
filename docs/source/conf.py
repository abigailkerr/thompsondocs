# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Thompson Group Reference Documentation'
copyright = '2025, University of Kansas'
author = 'Abigail L. Kerr, Ward H. Thompson'
version = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_favicon = 'ku.png'
html_theme = 'sphinx_rtd_theme'
html_logo = 'TG_logo.png'
html_theme_options = { 'logo_only': True }
html_static_path = ['_static']
