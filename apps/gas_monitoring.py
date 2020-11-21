import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
external_stylesheets=[dbc.themes.BOOTSTRAP]
gas_app = dash.Dash(__name__,title="Gas-monitoring System",external_stylesheets=external_stylesheets)

gas_app.layout = html.Div(
    html.H1('Gas')
)