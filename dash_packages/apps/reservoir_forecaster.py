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
import pathlib

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

df = pd.DataFrame()

#app = dash.Dash(__name__,external_stylesheets = [dbc.themes.BOOTSTRAP])dash_packages\apps\proccessed_HARANGI32
All_combined = "all_res"
Hemavathi = 'appended_HEMAVATHY'
KSR = "appended_KRS"
Harangi = "appended_HARANGI"
Kabini = 'appended_KABINI'

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../Datasets").resolve()
colors = {
    'background': '#192444',
    'text': '#7FDBFF',
    'card' : '#1F2C56'
}

dictres = {"KRS":["proccessed_KRS33",["Day Of Week","MO","PS",'T2M','T2M_MIN_x',"WS50M_MIN",'QV2M','RH2M','PRECTOT',"OUTFLOW_CUECS","INFLOW_CUSECS","PRESENT_STORAGE_TMC","RES_LEVEL_FT"],"xgboost_sarima8kr_var12",['ALLSKY_SFC_SW_DWN',"PS",'T2M_MIN_x','T2M',"WS10M_MIN","WS50M_MIN","TS",'QV2M','RH2M','PRECTOT',"OUTFLOW_CUECS","INFLOW_CUSECS","RES_LEVEL_FT","PRESENT_STORAGE_TMC"],62,5],
"HARANGI": ["proccessed_HARANGI32",['OUTFLOW_CUECS','INFLOW_CUSECS', 'WS50M','WS10M','T2MWET',"WS10M_MIN","WS50M_MIN",'WS10M_MAX','WS50M_MAX','QV2M','RH2M','PRECTOT','MO','PRESENT_STORAGE_TMC','RES_LEVEL_FT'],"xgboost_sarima8ha_var12",['OUTFLOW_CUECS','INFLOW_CUSECS', 'WS50M','WS10M','T2MWET',"WS10M_MIN","WS50M_MIN",'WS10M_MAX','WS50M_MAX','QV2M','RH2M','PRECTOT','PRESENT_STORAGE_TMC','RES_LEVEL_FT'],83,4],
"HEMAVATHY": ["proccessed_Hemavathi32",["Day Of Week","MO",'OUTFLOW_CUECS','INFLOW_CUSECS', 'WS50M','WS10M','T2MWET',"WS10M_MIN","WS50M_MIN",'WS10M_MAX','WS50M_MAX','QV2M','RH2M','PRECTOT','PRESENT_STORAGE_TMC','RES_LEVEL_FT'],"xgboost_sarima8he_var12",['OUTFLOW_CUECS','INFLOW_CUSECS', 'WS50M','WS10M','T2MWET',"WS10M_MIN","WS50M_MIN",'WS10M_MAX','WS50M_MAX','QV2M','RH2M','PRECTOT','PRESENT_STORAGE_TMC','RES_LEVEL_FT'],5,3],
"KABINI": ["proccessed_kabinii32",["Day Of Week","MO","TS",'OUTFLOW_CUECS','INFLOW_CUSECS','T2MWET', 'WS50M','WS10M',"WS50M_MIN",'WS10M_MIN','QV2M','RH2M','PRECTOT','PRESENT_STORAGE_TMC','RES_LEVEL_FT'],"xgboost_sarima8kb_var12",["TS",'OUTFLOW_CUECS','INFLOW_CUSECS','T2MWET', 'WS50M','WS10M',"WS50M_MIN",'WS10M_MIN',"WS50M_MAX",'WS10M_MAX','QV2M','RH2M','PRECTOT','PRESENT_STORAGE_TMC','RES_LEVEL_FT'],16,10],
}



card1 = dbc.Card([
    html.Br(),
    html.Br(),
    dbc.Row(
        dbc.Col(
    html.H1("Total Bangalore Water avaiblity Forecast", className = "text-center  mb-3",style={'font-weight': 'bold', "text-align": "center","color":"white",'fontSize': 60}),
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
        max_date_allowed=dt(2021, 12, 16),  # maximum date allowed on the DatePickerRange component
        initial_visible_month=dt(2020, 5, 1),  # the month initially presented when the user opens the calendar
        start_date=dt(2020, 12, 16).date(),
        end_date=dt(2021, 3, 16).date(),
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
       
    dcc.Dropdown(id='dpdn1', value=[All_combined], multi=True,
                 options=[{'label': "Combined Reservoirs Total", 'value': All_combined},
                     {'label': "KSR", 'value': KSR},
                          {'label': "Hemavati", 'value': Hemavathi},
                          {'label': "Harangi", 'value': Harangi },  
                          {'label': "Kabini", 'value': Kabini}],                          style={'backgroundColor': 'white', 'color': 'black'},
                          className = "dropdown"
                          ),
                          html.Br()],width = 6
        ),
    
        
    

],justify = "start"),
dbc.Row(
    dcc.Graph(id='Line_chart11'),justify = 'center'
),

html.Br(),
html.Br()
],color = colors["card"])

card2 = dbc.Card([
    html.Br(),
     html.H2(['Dates Perfomance'],style={'font-weight': 'bold', "text-align": "center","color":"white",'fontSize': 50}),
    html.H6(['Select a Date from table'],style={'font-weight': 'light', "text-align": "center","color":"white",'fontSize': 20}),
     html.Br(),
     html.Br(),
    html.Div(id='textarea-output', style={'font-weight': 'bold', "text-align": "center","color":"red",'fontSize': 20}),
    html.Br(),
    html.Br(),
    #html.Div(id='textarea-output1', style={'whiteSpace': 'pre-line'}),
    
],color = colors["card"])

card3 = dbc.Card([
                        dash_table.DataTable(
            id='table21',
            columns=[],
            
            data=[],
            style_cell={'textAlign': 'center','backgroundColor': colors["card"],"color" : "white"},
            page_size=30,
            row_selectable='single',
            selected_rows = [0]
            
            
        )
            ],color = colors["card"],body=True)

card4 = dbc.Card([
                        dash_table.DataTable(
            id='table22',
            columns=[],
            
            data=[],
            style_cell={'textAlign': 'center','backgroundColor': colors["card"],"color" : "white"},
            page_size=30,
            row_selectable='single',
            selected_rows = [0]
            
            
            
            
        )
            ],color = colors["card"],body=True)

card5 = dbc.Card([
    dcc.Graph(id="barChart1"),
],color = colors["card"],body=True)

card6 = dbc.Card([
    dcc.Graph(id="barChart2"),
],color = colors["card"],body=True)

card7 = dbc.Card([
    html.Br(),
     html.H2(['Dates Perfomance (water dep/gain)'],style={'font-weight': 'bold', "text-align": "center","color":"white",'fontSize': 50}),
    html.H6(['Select a Date from table'],style={'font-weight': 'light', "text-align": "center","color":"white",'fontSize': 20}),
     html.Br(),
     html.Br(),
    html.Div(id='textarea-output2', style={'font-weight': 'bold', "text-align": "center","color":"red",'fontSize': 20}),
    html.Br(),
    html.Br(),
    #html.Div(id='textarea-output1', style={'whiteSpace': 'pre-line'}),
    
],color = colors["card"])

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
        [dbc.Col([dbc.Row(card2),
        dbc.Row(card5)
        ],width = 6),
            
            dbc.Col(card3,width = 4),
            
            
        ],justify = "center"
    ),
    html.Br(),
    html.Br(),
    dbc.Row(
        [dbc.Col([dbc.Row(card7),
        dbc.Row(card6)
        ],width = 6),
            
            dbc.Col(card4,width = 4),
            
            
        ],justify = "center"
    ),
    html.Br(),
    html.Br(),

],fluid = True)])

@app.callback(
    Output("Line_chart11",'figure'),
    Output("table21","data"),
    Output("table21","columns"),
    Output("table22","data"),
    Output("table22","columns"),
    [Input("dpdn1","value"),
    Input("my-date-picker-range",'start_date'),
    Input("my-date-picker-range",'end_date')]
)
def update(dataframe,start_date,end_date):
    comb_df = pd.read_csv(DATA_PATH.joinpath(All_combined))
    
    comb_df = comb_df.round(3)
    comb_df['id'] = pd.to_datetime(comb_df['DATE'])
    comb_df.set_index('id', inplace=True)
    comb_df = comb_df[start_date:end_date]
    dff_lvl = comb_df.sort_values(ascending = True,by = ["RES_lvl_total"])
    dff_change = comb_df.sort_values(ascending = True,by = ["RES_lvl_change_total"])
    fig = make_subplots(rows=len(dataframe), cols=1,
                    shared_xaxes=True,
                    vertical_spacing=0.03)
    for no,variable in enumerate(dataframe):
        df = pd.read_csv(DATA_PATH.joinpath(variable))
        df['id'] = pd.to_datetime(df['DATE'])
        df.set_index('id', inplace=True)
        df = df.loc[start_date:end_date]

        
        #df1 = df[['T2M_MAX','T2M',"PS",'T2M_MIN_x','OUTFLOW_CUECS','INFLOW_CUSECS',"WS50M_MIN","MO",'QV2M','RH2M','PRECTOT','RES_LEVEL_FT','PRESENT_STORAGE_TMC']]
        if variable == All_combined:
            fig.add_trace(go.Line(x = df["DATE"],y = df["RES_lvl_total"]),
                        row=no+1, col=1),
                        
        else:
            fig.add_trace(go.Line(x = df["DATE"],y = df['RES_LEVEL_FT']),
                        row=no+1, col=1)
    
    for no,variable in enumerate(dataframe):
        fig.update_yaxes(title_text=variable, row=no+1, col=1,color = 'white')
    
    fig.update_xaxes(title_text="DATE", row=len(dataframe), col=1,color = 'white' )
    fig.update_layout(height=1000, width=1800, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"] )
    d = {"DATE":list(dff_lvl["DATE"].values),"Lowest Water level (FT)": list(dff_lvl["RES_lvl_total"].values)}                                                              
    table1 = pd.DataFrame(d)
    column1 = [{"name": x, "id": x} for x in table1.columns]
    table1["id"] = table1["DATE"]
    table1.set_index('id', inplace=True)
    
    #[{"name": "DATE", "id": "table1Col2"},{"name": "Lowest Water level (FT)", "id": "table1Col1"}]

    d2 = {"DATE":dff_change["DATE"],"Highest Water Depletion (FT)": dff_change["RES_lvl_change_total"]}                                                              
    table2 = pd.DataFrame(d2)
    column2 = [{"name": x, "id": x} for x in table2.columns]
    table2["id"] = table2["DATE"]
    table2.set_index('id', inplace=True)
    
    return fig,table1.to_dict('records'),column1,table2.to_dict('records'),column2




@app.callback(
    Output('textarea-output',"children"),
    Output('barChart1',"figure"),
    [Input("table21",'selected_rows'),
    Input("my-date-picker-range",'start_date'),
    Input("my-date-picker-range",'end_date')]

)
def val_update(id,start_date,end_date):
    id=id[0]
    print(id)
    
    data = []

    comb_df = pd.read_csv(DATA_PATH.joinpath(All_combined))
    comb_df = comb_df.round(3)
    
    # comb_df['id'] = pd.to_datetime(comb_df['DATE'])
    # comb_df.set_index('id', inplace=True)
    comb_df = comb_df[(comb_df["DATE"]>=start_date) & (comb_df["DATE"]<=end_date)]
    
    
    dff_lvl = comb_df.sort_values(ascending = True,by = ["RES_lvl_total"])
    dff_lvl.reset_index(drop=True, inplace=True)
    print(dff_lvl)
    date = dff_lvl.loc[id,"DATE"]
    print(date)
    res_lvl = dff_lvl[dff_lvl["DATE"] == date]["RES_lvl_total"].iloc[0]
    dep_lvl = dff_lvl[dff_lvl["DATE"] == date]["RES_lvl_change_total"].iloc[0]

    KSR_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_KRS"].iloc[0]
    Hemavathy_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_Hemavathy"].iloc[0]
    Harangi_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_Harangi"].iloc[0]
    kabini_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_Kabini"].iloc[0]

    data = [KSR_wtr,Hemavathy_wtr,Harangi_wtr,kabini_wtr]
    # for res in [Hemavathy, ksr, harangi, kabini]:
    #     data.append(res[res["DATE"] == date]["RES_LEVEL_FT"].iloc[0])
    print(data)
    dff = pd.DataFrame({"Reservoir Water lvl(ft)": data,"Reservoirs": ["KSR", "Hemavathy",  "Harangi", "Kabini"]})
    barChart = px.bar(dff, y="Reservoir Water lvl(ft)", x="Reservoirs")
    barChart.update_yaxes( color = 'white')
    barChart.update_xaxes(color = 'white' )
    barChart.update_layout(height=700, width=1100, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"] )
    text = f"Total RESERVOIR WATER LEVEL on {date} is {res_lvl}, \n Total WATER LEVEL DEPLETED\GAIN on {date} is {dep_lvl} \n KSR DEP\GAIN in water lvl(ft) :-{KSR_wtr},\n HEMAVATHY DEP\GAIN in water lvl(ft) :-{Hemavathy_wtr},\n HARANGI DEP\GAIN in Water lvl(ft) :-{Harangi_wtr},\n KABINI DEP\GAIN in Water lvl(ft) :-{kabini_wtr}"
    print(text)
    return text,barChart



@app.callback(
    Output('textarea-output2',"children"),
    Output('barChart2',"figure"),
    [Input("table22",'selected_rows'),
    Input("my-date-picker-range",'start_date'),
    Input("my-date-picker-range",'end_date')]

)
def val_update(id,start_date,end_date):
    id=id[0]
    print(id)
    
    data = []

    comb_df = pd.read_csv(DATA_PATH.joinpath(All_combined))
    comb_df = comb_df.round(3)
    
    # comb_df['id'] = pd.to_datetime(comb_df['DATE'])
    # comb_df.set_index('id', inplace=True)
    comb_df = comb_df[(comb_df["DATE"]>=start_date) & (comb_df["DATE"]<=end_date)]
    
    
    dff_lvl = comb_df.sort_values(ascending = True,by = ["RES_lvl_change_total"])
    dff_lvl.reset_index(drop=True, inplace=True)
    print(dff_lvl)
    date = dff_lvl.loc[id,"DATE"]
    print(date)
    res_lvl = dff_lvl[dff_lvl["DATE"] == date]["RES_lvl_total"].iloc[0]
    dep_lvl = dff_lvl[dff_lvl["DATE"] == date]["RES_lvl_change_total"].iloc[0]

    KSR_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_change_KRS"].iloc[0]
    Hemavathy_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_change_Hemavathy"].iloc[0]
    Harangi_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_change_Harangi"].iloc[0]
    kabini_wtr = comb_df[comb_df["DATE"] == date]["RES_LEVEL_FT_change_Kabini"].iloc[0]

    data = [KSR_wtr,Hemavathy_wtr,Harangi_wtr,kabini_wtr]
    # for res in [Hemavathy, ksr, harangi, kabini]:
    #     data.append(res[res["DATE"] == date]["RES_LEVEL_FT"].iloc[0])
    print(data)
    dff = pd.DataFrame({"Reservoir Water dep/gain lvl(ft)": data,"Reservoirs": ["KSR", "Hemavathy",  "Harangi", "Kabini"]})
    barChart = px.bar(dff, y="Reservoir Water dep/gain lvl(ft)", x="Reservoirs")
    barChart.update_yaxes( color = 'white')
    barChart.update_xaxes(color = 'white' )
    barChart.update_layout(height=700, width=1100, plot_bgcolor = colors["card"],paper_bgcolor = colors["card"] )
    text = f"Total RESERVOIR WATER LEVEL on {date} is {res_lvl}, \n Total WATER LEVEL DEPLETED\GAIN on {date} is {dep_lvl} \n KSR water lvl(ft) :-{KSR_wtr},\n HEMAVATHY water lvl(ft) :-{Hemavathy_wtr},\n HARANGI Water lvl(ft) :-{Harangi_wtr},\n KABINI Water lvl(ft) :-{kabini_wtr}"
    print(text)
    return text,barChart
