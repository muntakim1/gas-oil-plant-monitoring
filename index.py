import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import dash
from app import app
from app import server

from apps.gas_monitoring import gas_app

navBar = dbc.NavbarSimple(
    children=[
        
        dbc.NavItem(dbc.NavLink("Home", href="/")),
        dbc.NavItem(dbc.NavLink("Gas-system", href="/gas-monitoring")),
        dbc.NavItem(dbc.NavLink("Oil-system", href="/oil-monitoring")),
        
    ],
    brand="G.O.M",
    brand_href="/",
    color="primary",
    dark=True,
)
app.layout = html.Div(
    [
        dcc.Location(id='url', refresh=False),
        navBar,
        dbc.Container([
           html.Div(id='content')
       ])
    ]
)

error_page = html.Div([
        html.H1("404",style={"textAlign":"center"}),
        html.H3("Page Not Found!",style={"textAlign":"center"})
    ])

index_page = html.Div([
        html.H1("Home",style={"textAlign":"center","justifyContent":"center"}),
        html.H3("Page Not Found!",style={"textAlign":"center"})
    ])


@app.callback(dash.dependencies.Output('content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/gas-monitoring':
        return gas_app.layout
    elif pathname == "/oil-monitoring":
        return gas_app.layout
    elif pathname == '/':
        return index_page
    else:
        return error_page

if __name__ == '__main__':
    app.run_server(debug=True)