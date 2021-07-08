from flask import Flask
import dash
import dash_bootstrap_components as dbc

server = Flask(__name__)

app = dash.Dash(__name__, server = server, url_base_pathname='/dashboard/',external_stylesheets = [dbc.themes.BOOTSTRAP], meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}])
# app2 = dash.Dash(__name__, server = server, url_base_pathname='/dashboard2/',external_stylesheets = [dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True
server = app.server

from dash_packages import routes