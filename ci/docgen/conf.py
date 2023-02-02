# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import sys
import json
from os.path import join as joinpath
from os.path import exists as existspath
from os.path import abspath, dirname

# -- Project information -----------------------------------------------------

project = 'rain'
copyright = '2022, Wu Wei'
author = 'Wu Wei'

# The full version, including alpha/beta/rc tags
release = '0.0.1'

# Load config genrated by docgen builder
conf_dir = abspath(dirname(__file__))
config_file = joinpath(conf_dir, "sphinx-config.json")
config = {}

if existspath(config_file):
    with open(config_file, mode = 'r', encoding = 'utf-8') as stream:
        config = json.load(stream)
    print(f"config updated from {config_file}:")
    print(f"{config}")

# Update sys.path from sphinx-config.json
if 'search_paths' in config:
    for search_path in config['search_paths']:
        if search_path not in sys.path:
            sys.path.insert(0, search_path)
    print(f"system path updated: {sys.path}")

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'breathe',
    'sphinx.ext.autodoc',
    'sphinx.ext.imgmath',
    'sphinx.ext.todo',
]

# Breathe Configuration
breathe_default_project = 'rain'
breathe_projects = {}

# Update breathe_projects from sphinx-config.json
if 'breathe_projects' in config:
    breathe_projects.update(config['breathe_projects'])
    print(f"breathe_projects updated: {breathe_projects}")

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['.build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']