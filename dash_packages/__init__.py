from flask import Flask
import dash
import dash_bootstrap_components as dbc

server = Flask(__name__)

app = dash.Dash(__name__, server = server, url_base_pathname='/dashboard/',external_stylesheets = [dbc.themes.BOOTSTRAP])
# app2 = dash.Dash(__name__, server = server, url_base_pathname='/dashboard2/',external_stylesheets = [dbc.themes.BOOTSTRAP])
app.config['suppress_callback_exceptions'] = True

from dash_packages import routes