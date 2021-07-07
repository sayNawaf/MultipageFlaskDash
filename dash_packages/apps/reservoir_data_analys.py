from datetime import datetime as dt
from typing import Container

from pandas.io.formats import style

import plotly.figure_factory as ff
import dash_table
import plotly.express as px
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
from matplotlib import pyplot as plt
from dash_packages import app
import pandas as pd
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.DataFrame()

#app = dash.Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP])
Hemavathi = r"C:\Users\sayna\project\Dash\dash_packages\Datasets\proccessed_Hemavathi32"
KSR = r"C:\Users\sayna\project\Dash\dash_packages\Datasets\proccessed_KRS32"
Harangi = r"C:\Users\sayna\project\Dash\dash_packages\Datasets\proccessed_HARANGI32"
Kabini = r"C:\Users\sayna\project\Dash\dash_packages\Datasets\proccessed_kabinii32"
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
    html.H1("Compare Reservoir Water Level Forecast ", className = "text-center  mb-3",style={ 'color': 'white'}),
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
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(2014, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2020, 12, 16),  # maximum date allowed on the DatePickerRange component
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
        )],width = {"size":3,"offset":1}),
    html.Br(),
    
        dbc.Col([
            html.Label(['Select Reservoirs:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
       
    dcc.Dropdown(id='dpdn1', value=[KSR], multi=True,
                 options=[{'label': "KSR", 'value': KSR},
                          {'label': "Hemavati", 'value': Hemavathi},
                          {'label': "Harangi", 'value': Harangi },  
                          {'label': "Kabini", 'value': Kabini}],                          style={'backgroundColor': 'white', 'color': 'black'},
                          className = "dropdown"
                          ),
                          html.Br()],width = 6
        ),
    
        
    

],justify = "start"),
dbc.Row(
    dcc.Graph(id='Line_chart1'),justify = 'center'
),

html.Br(),
html.Br()
],color = colors["card"])

card2 = dbc.Card([
    html.Br(),
    html.Br(),

    dbc.Row(
        dbc.Col(
    html.H2("DATES PERFOMANCE ANALYSIS",  className = "text-center  mb-3",style={ 'color': 'white'}),
    width = 12),
    justify = "center"
    ),

    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([

            
        html.Br(),
        dcc.DatePickerRange(
        id='my-date-picker-range2',  # ID to be used for callback
        calendar_orientation='horizontal',  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  # text that appears when no end date chosen
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  # number of months shown when calendar is open
        min_date_allowed=dt(2014, 1, 1),  # minimum date allowed on the DatePickerRange component
        max_date_allowed=dt(2020, 12, 16),  # maximum date allowed on the DatePickerRange component
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
         # singledate or bothdates. Determines when callback is triggered
        )],width = {"size":2}
        ),

    dbc.Col([
        html.Br(),
        html.Label(['Select No of Top Outputs:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
        
    dcc.Input(id="inputBar", type="number", placeholder="Enter no of outputs",value = 25),
    ],width = 3),
    dbc.Col([
        html.Label(['Perfomance With Respect To:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
        
    dcc.Dropdown(id='dpdn3', value="MAXwaterlvl", multi=False,
                 options=[{'label': 'Maximum Water Level', 'value': 'Maximum Water Level'},
                        {'label': 'Least Water Level', 'value': "Least Water Level"},
                        {'label': 'Highest  Water Depletion', 'value': "Highest  Water Depletion"},
                        {'label': 'Highest Water Gain', 'value': "Highest Water Gain"},
                          ],
                          style={'backgroundColor': 'white', 'color': 'black'},
                          className = "dropdown"
                )],width = 3),

        dbc.Col([
        html.Label(['Select Reservoir:'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
    
     dcc.Dropdown(id='dpdn4', value=KSR, multi=False ,
                 options=[{'label': "KSR", 'value': KSR},
                          {'label': "Hemavati", 'value': Hemavathi},
                          {'label': "Harangi", 'value': Harangi},
                          {'label': "Kabini", 'value': Kabini}],                          style={'backgroundColor': 'white', 'color': 'black'},
                          className = "dropdown"
                          ),
    ],width = 3),
    


    
    ],justify = 'center'),
    html.Br(),  
    html.Br(),
],color = colors["card"]),

card3 = dbc.Card([
    html.Br(),
    html.H2(['Top Dates Perfomance'],style={'font-weight': 'bold', "text-align": "center","color":"white"}),
    dcc.Graph(id = "Pie_chart")
],color = colors["card"],body = True)

card4 = dbc.Card([
                        dash_table.DataTable(
            id='table1',
            columns=[],
            
            data=[],
            style_cell={'textAlign': 'center','backgroundColor': colors["card"],"color" : "white"},
            page_size=39
            
        )
            ],color = colors["card"],body=True)





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
    dbc.Row(
    [
        dbc.Col(card2, width=11),
        
    ],justify = "center"),
    html.Br(),
    html.Br(),
    dbc.Row(
    [
        dbc.Col(card3,
         width=8),
        dbc.Col([
            dbc.Row([
                card4
            ],justify = "center"),   
           
        ],width = 3)
        
    ],justify = "center"),
    
],fluid = True)])

res_names = {'proccessed_KRS33':"KRS",
                          'proccessed_Hemavathi32':"Hemavati",
                           'proccessed_HARANGI32':"Harangi",
                           'proccessed_kabinii32':"Kabini"}
@app.callback(
    Output("Line_chart1",'figure'),
    [Input("dpdn1","value"),
    Input("my-date-picker-range",'start_date'),
    Input("my-date-picker-range",'end_date')]

)
def update_val(dataframe,start_date,end_date):
    fig = make_subplots(rows=len(dataframe), cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.03)
    for no,variable in enumerate(dataframe):
        df = pd.read_csv(variable)
        df['SUBMIT_DATE'] = pd.to_datetime(df['DATE'])
        df.set_index('SUBMIT_DATE', inplace=True)
        df = df.loc[start_date:end_date]
        print(df)
        print(f"{variable},",df.columns)
        #df1 = df[['T2M_MAX','T2M',"PS",'T2M_MIN_x','OUTFLOW_CUECS','INFLOW_CUSECS',"WS50M_MIN","MO",'QV2M','RH2M','PRECTOT','RES_LEVEL_FT','PRESENT_STORAGE_TMC']]
        fig.add_trace(go.Line(x = df["DATE"],y = df['RES_LEVEL_FT']),
                        row=no+1, col=1)
    
    for no,variable in enumerate(dataframe):
        fig.update_yaxes(title_text=variable, row=no+1, col=1,color = 'white')
    
    fig.update_xaxes(title_text="DATE", row=len(dataframe), col=1,color = 'white' )
    fig.update_layout(height=800, width=1800, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"] )
    return fig

def dat(no):
    if no == 0:
        return "Saturday"
    elif no == 1:
        return "Sunday"
    elif no == 2:
        return "Monday"
    elif no == 3:
        return "Tuesday"
    elif no == 4:
        return "Wednesday"
    elif no == 5:
        return "Thursday"
    elif no == 6:
        return "friday"

@app.callback(
   Output("Pie_chart","figure"),
    Output("table1",'columns'),
    Output("table1",'data'),

    [Input("inputBar","value"),
    Input("dpdn3","value"),
    Input("dpdn4","value"),
    Input("my-date-picker-range",'start_date'),
    Input("my-date-picker-range",'end_date')]

)
def update_val(top, metric, df, start_date, end_date):
    
    df = pd.read_csv(df)
    
    df['SUBMIT_DATE'] = pd.to_datetime(df['DATE'])
    df.set_index('SUBMIT_DATE', inplace=True)
    df = df[start_date:end_date]
    df["RES_LEVEL_DEP"] = df["RES_LEVEL_FT"].diff()

    
    if metric == 'Maximum Water Level':
        datesTop = df["RES_LEVEL_FT"].sort_values(ascending = False).index[:top]
        valuesTop = df["RES_LEVEL_FT"].sort_values(ascending = False).values[:top]

        dates = df["RES_LEVEL_FT"].sort_values(ascending = False).index
        values = df["RES_LEVEL_FT"].sort_values(ascending = False).values

    elif metric == 'Least Water Level':
        datesTop = df["RES_LEVEL_FT"].sort_values(ascending = True).index[:top]
        valuesTop = df["RES_LEVEL_FT"].sort_values(ascending = True).values[:top]

        dates = df["RES_LEVEL_FT"].sort_values(ascending = False).index
        values = df["RES_LEVEL_FT"].sort_values(ascending = True).values
        
    elif metric == 'Highest  Water Depletion':
        
        datesTop = df["RES_LEVEL_DEP"].sort_values(ascending = False).index[:top]
        valuesTop = df["RES_LEVEL_DEP"].sort_values(ascending = False).abs().values[:top]

        dates = df["RES_LEVEL_DEP"].sort_values(ascending = False).index
        values = df["RES_LEVEL_DEP"].sort_values(ascending = True).values

    else:
        
        datesTop = df["RES_LEVEL_DEP"].sort_values(ascending = True).index[:top]
        valuesTop = df["RES_LEVEL_DEP"].sort_values(ascending = True).abs().values[:top]

        dates = df["RES_LEVEL_DEP"].sort_values(ascending = False).index
        values = df["RES_LEVEL_DEP"].sort_values(ascending = True).values

                  
    # else:
    #     df["weekday"] = df.index.dayofweek
    #     df["weekday"] = df["weekday"].apply(dat)
    #     if metric == "HIGHwaterdep" or metric == "LEASTwaterdep":
    #         series = df.groupby("weekday")['RES_LEVEL_DEP'].mean()
    #     else:
    #         series = df.groupby("weekday")['RES_LEVEL_FT'].mean()

    #     if metric == 'MAXwaterlvl':
    #         dates = series.sort_values(ascending = False).index
    #         values = series.sort_values(ascending = True).values

    #         dates = series.sort_values(ascending = False).index
    #         values = series.sort_values(ascending = True).values


    #     elif metric == 'LEASTwaterlvl':
    #         datesTop = series.sort_values(ascending = True).index
    #         valuesTop = series.sort_values(ascending = True).values

    #         dates = series.sort_values(ascending = True).index
    #         values = series.sort_values(ascending = True).values
            
    #     elif metric == 'HIGHwaterdep':
            
    #         datesTop = series.sort_values(ascending = False).index
    #         valuesTop = series.sort_values(ascending = False).abs().values

    #         datesTop = series.sort_values(ascending = False).index
    #         valuesTop = series.sort_values(ascending = False).abs().values
    #     else:
    #         datesTop = series.sort_values(ascending = True).index
    #         valuesTop = series.sort_values(ascending = True).abs().values

    #         dates = series.sort_values(ascending = True).index
    #         values = series.sort_values(ascending = True).abs().values



    pie_chart = px.pie(df, values=abs(valuesTop), names=datesTop,)
    pie_chart.update_traces(textposition='inside', textinfo='percent+label')
    pie_chart.update_layout(height=1100, width=1300, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"] )

    # columns = [{"name": output_type,"id": output_type},{"name": metric,"id": metric}]
    # data = [{output_type: dates,metric : values}]

    d = {"Dates": dates,metric : values}                                                              
    dff1 = pd.DataFrame(d)

   

    columns1 = [{"name": x, "id": x} for x in dff1.columns]
    
    return pie_chart,columns1,dff1.to_dict('records')






if __name__ == '__main__':
    app.run_server(debug=True)