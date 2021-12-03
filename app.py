from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, State, Input
from dash_bootstrap_components._components.Card import Card
from io import BytesIO
import base64
from handlers.create_handler import get_handler

transcrypt_handler = get_handler('transcrypt_handler')

app = Dash(__name__, suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP], title='РБК Xavier video annotator')

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content'),
], style={'backgroundColor': 'white'})

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Admin", href="/admin")),

    ],
    brand="Newsfeed",
    brand_href="/",
    color="#008080",
    dark=True,)


adminPanel = html.Div([

    navbar,
    dbc.Container(children=[
        dcc.Upload(
            id="upload_file",
            children=html.Div([
                'Перетащите сюда или ',
                html.A('выберите файл')
            ]),
            style={
                'width': '100%',
                'height': '60px',
                'lineHeight': '60px',
                'borderWidth': '1px',
                'borderStyle': 'dashed',
                'borderRadius': '5px',
                'textAlign': 'center',
                'margin': '10px'
            },
            multiple=False
        ),
        html.Div(id='output-data-upload'),

    ])
])


@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload_file', 'contents'),
    State('upload_file', 'filename'),
)
def upload_file(content, filename):
    if(content != None):
        bts = base64.b64decode(content.split(';')[1][7:])
        # bytes = BytesIO(bts)
        trans = transcrypt_handler.handle(bts, filename)
        return str(trans[0]['transcription'])
    return


def feed_generate(videos):
    list_of_cards = []
    for video in range(videos):
        list_of_cards.append(
            dbc.Card(video)
        )

    return list_of_cards


index_page = html.Div([
    navbar,
    dbc.Container(children=[
        dbc.Container(children=[
            dbc.Row([
                html.H1('Лента новостей', style={'margin': '10px'}),

                # dbc.Button('обновить', id='reload-button',
                #            className="mb-3", style={'margin': '10px'}),
            ]),
            html.Div(dbc.Spinner(color="primary"),
                     id="cluster-cards", style={'align': 'center'}),
            dbc.Card(children=feed_generate(4))

        ])
    ])
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/admin':
        return adminPanel
    else:
        return index_page
    # You could also return a 404 "URL not found" page here


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
