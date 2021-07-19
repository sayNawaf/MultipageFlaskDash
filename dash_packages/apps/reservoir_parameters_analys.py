from datetime import datetime as dt
from typing import Container

from pandas.io.formats import style
from seaborn.matrix import heatmap
import plotly.figure_factory as ff
import dash_table
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from matplotlib import pyplot as plt
import seaborn as sns
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from dash_packages import app
import pathlib

# Data from NYC Open Data portal
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../Datasets").resolve()
All_combined = "all_res"
Hemavathi = 'appended_HEMAVATHY'
KSR = "appended_KRS"
Harangi = "appended_HARANGI"
Kabini = 'appended_KABINI'
df = pd.read_csv(DATA_PATH.joinpath(KSR))

df['SUBMIT_DATE'] = pd.to_datetime(df['DATE'])
df.set_index('SUBMIT_DATE', inplace=True)
print(df.columns)
df = df.drop(["DATE"],axis =1)
#df1 = df[['T2M_MAX','T2M',"PS",'T2M_MIN_x','OUTFLOW_CUECS','INFLOW_CUSECS',"WS50M_MIN","MO",'QV2M','RH2M','PRECTOT','PRESENT_STORAGE_TMC','RES_LEVEL_FT']]
d = {"Correlation wrt res_lvl": list(df.corr()['RES_LEVEL_FT'].sort_values(ascending=False)[1:].values),"Parameters":list(df.corr()['RES_LEVEL_FT'].sort_values(ascending=False)[1:].index)}                                                               
dff = pd.DataFrame(d) 
# print(dff)
# print(df[:5][['BUSINESS_NAME', 'LATITUDE', 'LONGITUDE', 'APP_SQ_FT']])
print("sdddddddddddddddddddddddd")

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


#app = dash.Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP])
colors = {
    'background': '#192444',
    'text': '#7FDBFF',
    'card' : '#1F2C56'
}
card1 = dbc.Card([
    html.Br(),
    html.Br(),
    

    dbc.Row(
        dbc.Col(
    html.H1("Historical Data Analysis", className = "text-center  mb-3",style={'font-weight': 'bold', "text-align": "center","color":"white",'fontSize': 50}),
    width = 12),
    justify = "center"),

    html.Br(),
    html.Br(),
    dbc.Row([
        
        dbc.Col([
            html.Br(),
    dcc.DatePickerRange(
        
        id='my-date-picker-range',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=2,  # number of months shown when calendar is open
        min_date_allowed=dt(2014, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2021, 3, 6),  # maximum date allowed on the DatePickerRange component
        initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
        start_date=dt(2018, 8, 7).date(),
        end_date=dt(2020, 12, 16).date(),
        display_format='MMM Do, YY',  # how selected dates are displayed in the DatePickerRange component.
        month_format='MMMM, YYYY',  # how calendar headers are displayed when the calendar is opened.
        minimum_nights=2,  # minimum number of days between start and end date
        persistence=True,
        persisted_props=['start_date'],
        persistence_type='session',  # session, local, or memory. Default is 'local'

        updatemode='singledate',
        style={'backgroundColor': '#192444', 'color': '#192444'},
        className = "dropdown" # singledate or bothdates. Determines when callback is triggered
        )],width = {"size":2,"offset":1}),
    html.Br(),
    
        dbc.Col([
            html.Label(['Select Water Level Dependancies:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
    dcc.Dropdown(id='dpdn1',value = [], multi=True,
                 options=[],        
                 placeholder = "Select a variable",               style={'backgroundColor': 'white', 'color': 'black'},
                          className = "dropdown"
                          )],width = 6
        ),

        dbc.Col([
            html.Label(['Select Reservoirs:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
       
    dcc.Dropdown(id='dpdn2', value=KSR, multi=False,
                 options=[
                     {'label': "KSR", 'value': KSR},
                          {'label': "Hemavati", 'value': Hemavathi},
                          {'label': "Harangi", 'value': Harangi },  
                          {'label': "Kabini", 'value': Kabini}],                          style={'backgroundColor': 'white', 'color': 'black'},
                          className = "dropdown"
                          ),
                          html.Br()],width = 2
        ),
    
        
    

],justify = "start"),
html.Br(),


dbc.Row(
    
    dcc.Graph(id='line-chart1'),justify = 'center'
    ),
html.Br(),
html.Br(),

],
color = colors["card"]),


card2 = dbc.Card([
            dcc.Graph(id="heatmap")

],color = colors["card"],body=True)
        
        
card3 = dbc.Card([
                        dash_table.DataTable(
            id='table',
            columns=[{"name": x, "id": x} for x in dff.columns],
            
            data=[],
            style_cell={'textAlign': 'center','backgroundColor': colors["card"],"color" : "white"},
            
        )
            ],color = colors["card"],body=True)
        
        
card4 =  dbc.Card([
            dcc.Graph(id = "bar_chart",
                )
            ],color = colors["card"],body=True)
        
card5 = dbc.Card([
    html.Br(),
    html.Label(['Select Time Period'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
    html.Br(),
    dcc.RangeSlider(
            id='my-range-slider', # any name you'd like to give it
            
            
            marks={
                2011: {'label': '2011', 'style': {'color': 'white'}},
                2012: {'label': '2012', 'style': {'color': 'white'}},     # key=position, value=what you see
                2013: {'label': '2013', 'style': {'color': 'white'}},
                2014: {'label': '2014', 'style': {'color': 'white'}},
                2015: {'label': '2015', 'style': {'color': 'white'}},
                2016: {'label': '2016', 'style': {'color': 'white'}},
                2017: {'label': '2017', 'style': {'color': 'white'}},
                2018: {'label': '2018', 'style': {'color': 'white'}},
                2019: {'label': '2019', 'style': {'color': 'white'}},
                2020: {'label': '2020', 'style': {'color': 'white'}},
            },
            step=1,                # number of steps between values
            min=2011,
            max=2020,
            value=[2011,2020],     # default value initially chosen
            dots=True,
            allowCross=True,      # True,False - Manage handle crossover
            disabled=False,        # True,False - disable handle
            pushable=False,            # any number, or True with multiple handles
            updatemode='mouseup',  # 'mouseup', 'drag' - update value method
            included=True,         # True, False - highlight handle
            vertical=False,        # True, False - vertical, horizontal slider
            verticalHeight=1500,    # hight of slider (pixels) when vertical=True
            className='None',
            
            
)],color = colors["card"],body=True)



layout = html.Div( style={'backgroundColor': colors['background']},children = [dbc.Container([
    html.Br(),
    html.Br(),
    html.Br(),
    dbc.Row(
    [
        dbc.Col(card1, width=11),
        
    ],justify = "center"),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col(card5,width = 11)
    ],justify = "center"),
    html.Br(),
    html.Br(),
    dbc.Row(
    [
        dbc.Col(card2,
         width=7),
        dbc.Col([
            dbc.Row([
                card3
            ],justify = "center"),
            html.Br(),
            
            dbc.Row([
                card4
            ],justify = "center")
        ],width = 5)
        
    ],justify = "center"),


],fluid = True)])

@app.callback(
    Output('dpdn1','options'),
    Output('dpdn1','value'),
    Input('dpdn2','value')
)
def update_variables(reservoir):
    df = pd.read_csv(DATA_PATH.joinpath(reservoir))
    df = df.drop(["Unnamed: 0"],axis = 1)
    return [{'label': x, 'value': x} for x in
                          df.columns],"RES_LEVEL_FT"


@app.callback(
    Output("line-chart1", "figure"),
    [Input('my-date-picker-range', 'start_date'),
     Input('my-date-picker-range', 'end_date'),
     Input('dpdn1','value'),
     Input('dpdn2','value')]

)
def update_output(start_date, end_date, variables, reservoir):

    print("Start date: " + start_date)
    print("End date: " + end_date)

    df = pd.read_csv(DATA_PATH.joinpath(reservoir))

    df['SUBMIT_DATE'] = pd.to_datetime(df['DATE'])
    df.set_index('SUBMIT_DATE', inplace=True)
    dff = df.loc[start_date:end_date]
    fig = make_subplots(rows=len(variables), cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.03)

    for no,variable in enumerate(variables):
        fig.add_trace(go.Line(x = dff["DATE"],y = dff[variable]),
                    row=no+1, col=1)


    for no,variable in enumerate(variables):
        fig.update_yaxes(title_text=variable, row=no+1, col=1,color = 'white')
    
    fig.update_xaxes(title_text="DATE", row=len(variables), col=1,color = 'white'  )
    fig.update_layout(height=800, width=1800, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"] )
   
    return fig




def year(strr):
    return strr.year

@app.callback(
    Output("bar_chart", "figure"),
    Output("heatmap", "figure"),
    Output("table","data"),
    [Input("my-range-slider","value"),
    Input('dpdn2','value')]
)
def update_output(value, reservoir):
    start_year = value[0]
    end_year = value[1]
    df1 = pd.read_csv(DATA_PATH.joinpath(reservoir))
    df1 = df1.round(3)
    df1["DATE"] = pd.to_datetime(df1["DATE"])
    df1["year"] = df1["DATE"].apply(year)
    df1 = df1.drop(["Unnamed: 0"],axis = 1)
    df1 = df1[(df1["year"] >=start_year) & (df1["year"] <= end_year)]
    
    df1 = df1.drop(["DATE"],axis = 1)
    fig3 = px.bar(x = df1.corr()['RES_LEVEL_FT'].abs().sort_values(ascending = False)[1:].index,y = df1.corr()['RES_LEVEL_FT'].abs().sort_values(ascending = False)[1:].values)
    fig3.update_layout(
        
    title = "Parameters correlation wrt Res water level",
    xaxis_title="Parameters",
    yaxis_title="Correlation",
    height=700, width=800, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"],font_color="white",),
    fig3.update_xaxes(color = 'white'  ),
    fig3.update_yaxes(color = 'white'  )
    

    heatmap = px.imshow(df1.corr())
    heatmap.update_layout(
        height=1300, width=1200, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"],font_color="white",
    )
    heatmap.update_xaxes(color = 'white'  ),
    heatmap.update_yaxes(color = 'white'  )

    d = {"Correlation wrt res_lvl": list(df1.corr()['RES_LEVEL_FT'].sort_values(ascending = False)[1:].values),"Parameters":list(df1.corr()['RES_LEVEL_FT'].sort_values(ascending = False)[1:].index)}                                                               
    dff = pd.DataFrame(d)
    print(dff)
    
    return fig3,heatmap,dff.to_dict('records')





# if __name__ == '__main__':
#     app.run_server(debug=True)

