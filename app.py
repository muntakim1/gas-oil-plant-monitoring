import dash
import dash_bootstrap_components as dbc
external_stylesheets=[dbc.themes.BOOTSTRAP]
app = dash.Dash(__name__,title="Gas-oil-monitoring System",external_stylesheets=external_stylesheets)

server = app.server