import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
import dash_daq as daq
from dash.dependencies import Input, Output
import time
external_stylesheets=[dbc.themes.BOOTSTRAP]
gas_app = dash.Dash(__name__,title="Gas-monitoring System",external_stylesheets=external_stylesheets)



meter_1=daq.Gauge(
            color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}},
            label="Tank-1",
            units="PSI",
            value=5,
            showCurrentValue=True,
        )
meter_2=daq.Gauge(
    color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}},
    label="Tank-2",
            units="PSI",
        value=5,
        showCurrentValue=True,
        )
meter_3=daq.Gauge(
   color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}},
            label="Tank-3",
             units="PSI",
        value=5,
        showCurrentValue=True,
        )
meter_4=daq.Gauge(
    color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}},
        label="Tank-4",
            units="PSI",
        value=5,
        showCurrentValue=True,
        )


thm_1=daq.Thermometer(
    label="Tank-1",
        units="C",
        value=5,
        showCurrentValue=True,
        )
thm_2=daq.Thermometer(
        label="Tank-2",
        units="C",
        value=5,
        showCurrentValue=True,

        )
thm_3=daq.Thermometer(
        label="Tank-3",
             units="C",
        value=5,
        showCurrentValue=True,
        )
thm_4=daq.Thermometer(
        label="Tank-4",
        units="C",
        value=5,
        showCurrentValue=True,
        )  

tank_1 =  daq.Tank(
  id='my-daq-tank',
  min=0,
  max=10,
  label="TANK-1",
  showCurrentValue=True,
  units='gallons',
  value=5,
  style={'marginLeft': '50px','color':'white'}
) 
tank_2 =  daq.Tank(
  id='my-daq-tank',
  min=0,
  max=10,
  value=5,
  label="TANK-2",
  showCurrentValue=True,
  units='gallons',
  style={'marginLeft': '50px','color':'white'}


) 

tank_3 =  daq.Tank(
  id='my-daq-tank',
  min=0,
  max=10,
  value=5,
  label="TANK-3",
  showCurrentValue=True,
  units='gallons',
  style={'marginLeft': '50px','color':'white'}

)  

tank_4 =  daq.Tank(
  id='my-daq-tank',
  min=0,
  max=10,
  value=5,
  color={"ranges":{"green":[0,5],"yellow":[5,9],"red":[9,10]}},
  label="TANK-4",
  showCurrentValue=True,
  units='gallons',
  style={'marginLeft': '50px','color':'white'}

)  
col_1 =  dbc.Col([
    html.H3("GAS CONTAINER PRESSURES",style={"textAlign":"center"}),
                dbc.Row([
                    dbc.Col([
                        meter_1
                    ]),
                     html.Br(),
                    dbc.Col([
                        meter_2
                    ]),
             
                ]),
                 html.Br(),
                 dbc.Row([
                    dbc.Col([
                        meter_3
                    ]),
                     html.Br(),
                    dbc.Col([
                        meter_4
                    ]),
              
                ])
            ])
col_2= dbc.Col([
    html.H3("GAS CONTAINER TEMPERATURE",style={"textAlign":"center"}),
                dbc.Row([
                    dbc.Col([
                        thm_1
                    ]),
                    dbc.Col([
                        thm_2
                    ]),
                
                ]),
                html.Br(),
                 dbc.Row([
                    dbc.Col([
                        thm_3
                    ]),
                    dbc.Col([
                        thm_4
                    ]),
                
                ])
            ])


col_3=dbc.Col([
    dbc.Row([
        dbc.Col([
                        tank_1
                    ]),
                    dbc.Col([
                        tank_2
                    ]),
    ])
])

col_4=dbc.Col([
    dbc.Row([
        dbc.Col([
                        tank_3
                    ]),
                    dbc.Col([
                        tank_4
                    ]),
    ])
])


gas_app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False), 
        dcc.Interval(
            id='interval',
            interval=1 * 2000,
            n_intervals=0
        ),
        html.Br(),
        daq.LEDDisplay(
            id='control-panel-utc-component',
            value='16:23',
            label='Time',
            size=50,
        ),
        html.Br(),
        html.H1("NATURAL GAS CONTAINERS",style={"textAlign":"center"}),
        dbc.Row(
               [
                   col_3,
                   col_3,
               ]
        ),
        html.Br(),
        dbc.Row(
            
            [
        
        
           col_1,

            html.Br(),
           col_2

        ],
        style={'marginLeft':'40px','paddin':'50px'}
        
        )
    ],
    style={'backgroundColor': '#ddddd', 'color': 'black'}
)
@gas_app.callback(
    Output('clock_utc', 'value'),
    [Input('interval', 'n_intervals')],
)
def update_time(interval):
    hour = time.localtime(time.time())[3]
    hour = str(hour).zfill(2)

    minute = time.localtime(time.time())[4]
    minute = str(minute).zfill(2)
    return hour + ':' + minute