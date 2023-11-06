import os
import sys
sys.path.insert(0, os.path.abspath('../..'))
sys.path.append(os.path.dirname(os.path.dirname(__file__)))



# -- Project information -----------------------------------------------------

project = 'FastTrader'
copyright = 'Open-Source'
author = 'CS 595 Group 2'

# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1.0'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.autosummary',
]

intersphinx_mapping = {
    'pandas': ('https://pandas.pydata.org/docs/', None),
    'numpy': ('https://numpy.org/doc/stable/', None),
    # 'yfinance': ('https://pypi.org/project/yfinance/', None),
    'pyta': ('https://pyta.readthedocs.io/en/latest/', None),
    'matplotlib': ('https://matplotlib.org/stable/', None)
}

# The master toctree document.
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'classic'

# -- Extension configuration -------------------------------------------------

