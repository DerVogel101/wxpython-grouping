# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import os
import sys

sys.path.insert(0, os.path.abspath('../..'))

project = 'Student Grouper'
copyright = '2025, DerVogel101'
author = 'DerVogel101'
release = '1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
        'sphinx.ext.autodoc',
        'sphinx.ext.todo',
        'sphinx.ext.viewcode',
        'sphinx.ext.napoleon',
        'sphinx.ext.autosummary',
        'sphinx.ext.autodoc.typehints',
        'sphinx.ext.mathjax',
        'sphinx_rtd_theme',
        'sphinx_autodoc_typehints',
        'sphinxcontrib.autodoc_pydantic',
        'sphinx.ext.deprecated'
]

templates_path = ['_templates']
exclude_patterns = ["__pycache__", ".idea"]

autodoc_default_options = {
    'undoc-members': True,
    'private-members': True,
}

todo_include_todos = True

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
