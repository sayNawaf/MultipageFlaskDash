import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_packages import app

from dash_packages.routes import *
# Connect to main app.py file


# Connect to your app pages
from dash_packages.apps import reservoir_parameters_analys, reservoir_data_analys


app.layout = html.Div([
    dcc.Location(id='url', refresh=True),
    html.Div([
        dcc.Link('reservoir parameter analys|', href='/apps/reservoir_parameters_analys'),
        dcc.Link('reservoir data analys|', href='/apps/reservoir_data_analys'),
        dcc.Link('Homepage', href='http://127.0.0.1:8050/1',refresh = True),
        
    ], className="row"),
    html.Div(id='page-content', children=[])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/reservoir_parameters_analys':
        return reservoir_parameters_analys.layout
    if pathname == '/apps/reservoir_data_analys':
        return reservoir_data_analys.layout
    else:
        return "404"

if __name__ == "__main__":
    app.run_server(debug = True)
