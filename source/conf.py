### path setup ####################################################################################

from glob import glob
import datetime
import os
 
###################################################################################################
### Project Information ###########################################################################
###################################################################################################

project = 'Sustainable Aviation Dashboard'
copyright = datetime.date.today().strftime("%Y") + ' Paul Scherrer Institute'
version: str = 'latest' # required by the version switcher

###################################################################################################
### Project Configuration #########################################################################
###################################################################################################

# needs_sphinx = '7.2.6' # update as soon as myst-nb has been updated to allow for sphinx 7

extensions = [
    # core extensions
    'sphinx.ext.mathjax',
    'sphinx.ext.viewcode',
    'sphinx.ext.intersphinx',
    'sphinx.ext.extlinks',
    'sphinx.ext.inheritance_diagram',
    # iPython extensions
    'IPython.sphinxext.ipython_directive',
    'IPython.sphinxext.ipython_console_highlighting',
    # Markdown support
    'myst_parser', # do not enable separately if using myst_nb, compare https://github.com/executablebooks/MyST-NB/issues/421#issuecomment-1164427544
    # responsive web component support
    'sphinx_design',
    # custom 404 page
    'notfound.extension',
    # custom favicons
    'sphinx_favicon',
    # copy button on code blocks
    "sphinx_copybutton",
    # wasm
    #"jupyterlite_sphinx",
    # dashboard
    # 'nbsite.pyodide',
]

root_doc = 'index'
html_static_path = ['_static']
templates_path = ['_templates']
exclude_patterns = ['_build']
html_theme = "pydata_sphinx_theme"

suppress_warnings = [
    "myst.header" # suppress warnings of the kind "WARNING: Non-consecutive header level increase; H1 to H3"
]

####################################################################################################
### Theme html Configuration #######################################################################
####################################################################################################

html_show_sphinx = False
html_show_copyright = True

html_css_files = [
    "css/custom.css",
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.1.1/css/all.min.css" # for https://fontawesome.com/ icons
]

html_sidebars = {
    "**": [
        "search-field.html",
        "sidebar-nav-bs.html",
    ],
}

footcent = str('test')

html_theme_options = {
    "announcement": "<p>⚠️ This Dashboard is in Public Beta ⚠️</p>",
    # page elements
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["navbar-icon-links.html"],
    "footer_start": ["copyright"],
    "footer_center": ["footer_center"],
    "footer_end": ["footer_end"],
    "navbar_persistent": ["theme-switcher"], # must not be removed and not contain "search-button", otherwise the search bar is shown https://pydata-sphinx-theme.readthedocs.io/en/stable/user_guide/search.html#configure-the-search-field-position
    "secondary_sidebar_items": ["page-toc"],
    "header_links_before_dropdown": 7,
    # page elements content
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/sustainableaviation/sustainable_aviation_dashboard",
            "icon": "fab fa-brands fa-github",
        },
    ],
    # various settings
    "collapse_navigation": True,
    "show_prev_next": False,
    "use_edit_page_button": True,
    "navigation_with_keys": True,
    "logo": {
        "text": "Sustainable Aviation Dashboard",
    },
}

# required by html_theme_options: "use_edit_page_button"
html_context = {
    "github_user": "sustainableaviation",
    "github_repo": "sustainable_aviation_dashboard",
    "github_version": "main",
    "doc_path": "docs",
}

####################################################################################################
### Extension Configuration ########################################################################
####################################################################################################

# pyviz.nbsite Configuration ############################################
# https://panel.holoviz.org/how_to/wasm/sphinx.html#configuration

# nbsite_pyodide_conf = {
#     "PYODIDE_URL": "https://cdn.jsdelivr.net/pyodide/v0.24.1/full/", # https://pyodide.org/en/stable/usage/downloading-and-deploying.html#cdn
#     "autodetect_deps": True,
#     "enable_pwa": True,
# }

# linkcheck Configuration ###############################################
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-the-linkcheck-builder

linkcheck_retries = 1
linkcheck_workers = 20
linkcheck_exclude_documents = []

# notfound Configuration ################################################
# https://sphinx-notfound-page.readthedocs.io

notfound_context = {
    'title': 'Page Not Found',
    'body': '''                                                                                                                                           
        <h1>🛬 Page Not Found (404)</h1>
        <p>
        Apologies, it seems our sustainable aviation page is experiencing turbulence.
        Head back to the homepage or use the search bar to find your destination.
        </p>
    ''',
}

# myst_parser Configuration ############################################
# https://myst-parser.readthedocs.io/en/latest/configuration.html

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown'
}

myst_enable_extensions = [
    "amsmath",
    "colon_fence",
    "deflist",
    "dollarmath",
    "html_image",
    "linkify",
]

# sphinx-favicon configuration #########################################
# https://github.com/tcmetzger/sphinx-favicon