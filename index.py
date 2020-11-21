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
        html.Div(
        id='content',
 
       )
    ]
)

error_page = html.Div([
        html.H1("404",style={"textAlign":"center"}),
        html.H3("Page Not Found!",style={"textAlign":"center"})
    ])

index_page = html.Div(
    [
        html.Div([
            
            html.H2("Welcome to Gas Oil plant monitoring System."),
            html.P("""Lorem ipsum dolor sit amet ac maximusrdiet convallis. Duis rutrum neque consectetur mauris tempor laoreet. Vestibulum quis nulla eu orci efficitur varrisque vel nibh. Integer eu velit eget ex consectetur consectetur sit amet vitae lectus. Mauris egestas purus et mi pulvinar, a posuere justo convallis. Nunc nec laoreet lectus. Mauris purus est, bibendum hendrerit fermentum quis, porttitor at massa.""")
        ],
        style={
            'text-align': 'center',
            'position': 'absolute',
            'top': '50%',
            'left': '50%',
            'transform': 'translate(-50%, -50%)',
            'color': 'white',
            
        })
       
    ],
    
    style={"textAlign":"center",
            'backgroundImage': 'url("assets/images/background.jpg")',
            'backgroundRepeat': 'no-repeat',
            'backgroundPosition': 'center',
            'backgroundSize' : 'cover',
            'height':'50vh',
            'position':'relative',
            },
    )


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