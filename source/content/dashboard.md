# Dashboard Infrastructure

## Dashboard Tools Comparison

["Big Four" Dashboarding Tools (by Dharhas Pothina of Quansight)](https://quansight.com/post/dash-voila-panel-streamlit-our-thoughts-on-the-big-four-dashboarding-tools/)

> If you’re publishing with Jupyter Notebooks, go with Voila or Panel. If you want to build multi-page apps in Python using data-science-friendly tools, then choose Panel.

[Streamlit vs. Dash vs. Shiny vs. Voila vs. Flask vs. Jupyter (by Markus Schmitt of Data Revenue)](https://www.datarevenue.com/en-blog/data-dashboarding-streamlit-vs-dash-vs-shiny-vs-voila)

> Voila if you already have Jupyter Notebooks and you want to make them accessible to non-technical teams. Panel if you already have Jupyter Notebooks, and Voila is not flexible enough for your needs.

[Streamlit vs Dash vs Voila vs Panel — Battle of The Python Dashboarding Giants by Stephen Kilcommins of DataDrivenInvestor](https://medium.datadriveninvestor.com/streamlit-vs-dash-vs-voilà-vs-panel-battle-of-the-python-dashboarding-giants-177c40b9ea57#8026)

> Voilà: To be used in a scenario where you have a Jupyter/IPython notebook with some data analysis already conducted, and you want to share the data insights with colleagues without the code cells cluttering up the view. Panel: Creating dashboard applications which are not restricted to a single GUI.

```{seealso}
[HackerNews Discussion](https://news.ycombinator.com/item?id=28364923) \
Comparisons in the Panel documentation: [`panel` vs `dash`](https://panel.holoviz.org/explanation/comparisons/compare_dash.html#), [`panel` vs `ipywidgets`](https://panel.holoviz.org/explanation/comparisons/compare_ipywidgets.html), [`panel` vs `voila`](https://panel.holoviz.org/explanation/comparisons/compare_voila.html).
```

[![Star History Chart](https://api.star-history.com/svg?repos=holoviz/panel,plotly/dash,voila-dashboards/voila,voila-dashboards/voici,streamlit/streamlit,jupyter-widgets/ipywidgets&type=Date)](https://star-history.com/#holoviz/panel&plotly/dash&voila-dashboards/voila&voila-dashboards/voici&streamlit/streamlit&jupyter-widgets/ipywidgets&Date)

## Dashboard Deployment Comparison

| Dashboard Tool | WASM Status | Comment |
| -------------- | ----------- | ------- |
| `panel` | [Full Support (based on `pyodide`)](https://panel.holoviz.org/how_to/wasm/index.html) | |
| `voila` | [Full Support through `voici` (based on `xeus-python-kernel`)](https://voici.readthedocs.io/en/latest/) | Currently buggy |
| `dash` | [Alpha Stage Prototypes (3rd Party)](https://medium.com/plotly/dash-club-6-webassembly-summer-app-challenge-show-tell-60a3b1cd9f41) | see also [`webdash`](https://github.com/ibdafna/webdash) |
| `streamlit` | [Alpha Stage Prototypes (3rd Party)](https://discuss.streamlit.io/t/new-library-stlite-a-port-of-streamlit-to-wasm-powered-by-pyodide/25556) | see also [`stlite`](https://github.com/whitphx/stlite) |

See also:

- [ContainDS Dashboards](https://github.com/ideonate/cdsdashboards) (from the discussion here: https://github.com/voila-dashboards/voila/issues/112)

## Tools

### Voila

[Documentation](https://voila.readthedocs.io/) \
[GitHub Repo](https://github.com/voila-dashboards/voila)

### Voici (based on Voila)

[Documentation](https://voici.readthedocs.io/en/latest/) \
[GitHub Repo](https://github.com/voila-dashboards/voici)

### Panel

[Documentation](https://panel.holoviz.org) \
[GitHub Repo](https://github.com/holoviz/panel) \
["Awesome Panel" Documentation](https://awesome-panel.org)

Working examples (WASM):

 - https://panel.holoviz.org/pyodide/portfolio_optimizer

```{note}
Some examples are currently broken, see: https://github.com/holoviz/panel/issues/5521
```

#### WASM Workflow

Functionality development:

1. Develop Panel application, [using the `autoreload` command](https://panel.holoviz.org/how_to/server/commandline.html#launching-a-server-on-the-commandline) to enable live loading of the application.

WASM development and deployment:

2. Develop Panel application, [using the `panel convert ... --watch` command](https://panel.holoviz.org/how_to/wasm/convert.html#converting-panel-applications) to enable live loading of the application.
3. Use the `panel convert ... --to pyodide-worker` command to convert the Panel application to a Pyodide web worker (an `.html` + `.js` file). These files [can be deployed to a static web server (e.g. Github pages)](https://panel.holoviz.org/how_to/wasm/convert.html#example):

> You can now add the script.html (and script.js file if you used the pyodide-worker target) to your Github pages or similar. no separate server needed!

## Examples Projects

| Project | Authors | Dashboard Technology | Backend | 
| ---- | ------- | ---------- | ------- |
| [AeroMaps](https://github.com/AeroMAPS/AeroMAPS) | Univ. of Toulouse | [voila + iPywidgets in a Jupyter Notebook](https://github.com/AeroMAPS/AeroMAPS/blob/ba80176a1d02caeed706a88063f8834f50b82416/aeromaps/gui/graphical_user_interface.py#L754) | mybinder.org |
| [Cascade](https://cascade.boeing.com/strategy) | Boeing | [JavaScript](https://builtwith.com/?https%3a%2f%2fcascade.boeing.com%2fstrategy) | Server |

### AeroMaps Project

- [Dashboard: AeroMaps](https://aeromaps.isae-supaero.fr)
- [Dashboard Documentation](https://aeromaps.github.io/AeroMAPS/intro.html)
- [GitHub Repo](https://github.com/AeroMAPS/AeroMAPS?tab=readme-ov-file)