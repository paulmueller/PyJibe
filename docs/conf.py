#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# PyJibe documentation build configuration file, created by
# sphinx-quickstart on Tue Sep 26 17:55:31 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

# Get version number from pyjibe._version file
import os.path as op
import sys
# include parent directory
pdir = op.dirname(op.dirname(op.abspath(__file__)))
# include extenstions
sys.path.append(op.abspath('extensions'))

# http://www.sphinx-doc.org/en/stable/ext/autodoc.html#confval-autodoc_member_order
# Order class attributes and functions in separate blocks
autodoc_member_order = 'groupwise'
autoclass_content = 'both'

# include source of matplotlib plots
plot_include_source = True

# Display link to GitHub repo instead of doc on rtfd
rst_prolog = """
:github_url: https://github.com/AFM-analysis/PyJibe
"""

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.autosummary',
              'sphinx.ext.intersphinx',
              'sphinx.ext.mathjax',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinxcontrib.bibtex',
              'matplotlib.sphinxext.plot_directive',
              'fancy_include',
              'github_changelog',
              'rtd_pdf',
              ]

# enable enumeration of figures
numfig = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'PyJibe'
github_project = 'AFM-analysis/PyJibe'
copyright = '2019, Paul Müller'
author = 'Paul Müller'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
# 
# The full version, including alpha/beta/rc tags.
# This gets 'version'
exec(open(op.join(pdir, "pyjibe/_version.py")).read())
release = version #@UndefinedVariable
# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_static_path = ['data']


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'pyjibedoc'


# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'pyjibe.tex', 'PyJibe Documentation',
     author, 'manual'),
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'pyjibe', 'PyJibe Documentation',
     [author], 1)
]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'pyjibe', 'PyJibe Documentation',
     author, 'pyjibe', 'post-measurement analysis of RT-DC data sets',
     'Scientific'),
]




# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {"python": ('https://docs.python.org/', None),
                       "numpy": ('https://docs.scipy.org/doc/numpy', None),
                       "scipy": ('https://docs.scipy.org/doc/scipy/reference/', None),
                       "nanite": ('https://nanite.readthedocs.io/en/stable', None),
                       "afmformats": ('https://afmformats.readthedocs.io/en/stable', None),
                       }
