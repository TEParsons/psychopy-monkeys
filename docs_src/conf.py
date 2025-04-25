# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PsychoPy Example Plugin'
copyright = '2024, Open Science Tools Ltd.'
author = 'Open Science Tools Ltd.'
release = '0.0.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = []

templates_path = ['_templates']
exclude_patterns = []

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.mathjax',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx_design'
]

html_static_path = ["static"]



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'psychopy'
html_theme_options = {
    'social_links': [
        {'name': "github", 'icon': "github", 'url': "https://github.com/teparsons/psychopy-monkeys"},
        {'name': "bluesky", 'icon': "bluesky", 'url': "https://web-cdn.bsky.app/profile/teparsons.bsky.social"},
        {'name': "linkedin", 'icon': "linkedin", 'url': "https://uk.linkedin.com/in/todd-parsons-056a459a"}, 
    ]
}
