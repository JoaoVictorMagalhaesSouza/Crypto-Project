import dash
import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import plotly.express as px
import datetime

from utils import auxiliary_functions as af
from utils import data_acquisition as da

def init_app(server):
    FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"
    CRYPTO_LOGO = "https://w7.pngwing.com/pngs/193/794/png-transparent-bitcoin-cryptocurrency-computer-icons-logo-bitcoin-text-logo-bitcoin.png"
    app = dash.Dash(
        __name__, 
        suppress_callback_exceptions=True,
        title="Crypto Analisys",
        server=server,
        
        external_stylesheets=[dbc.themes.LITERA, dbc.icons.BOOTSTRAP, FONT_AWESOME]
    )
    server = app.server

    

    app.layout = html.Div([
        dcc.Location(id="url"),
        

    ])
    

    return app