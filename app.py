from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, State, Input
from dash_bootstrap_components._components.Card import Card
from io import BytesIO
import base64
from handlers.create_handler import get_handler
import json

transcrypt_handler = get_handler('dummy_handler')

app = Dash(__name__, suppress_callback_exceptions=True,
           external_stylesheets=[dbc.themes.BOOTSTRAP], title='РБК Xavier video annotator')
           
server = app.server

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
        html.Div(dbc.Spinner(id="output-data-upload", color="primary", ),
                 style={'align': 'center', 'margin': '10px'}),
        # html.Div(id=''),

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
        print(trans)
        result = str(trans['text'])
        source = content
        return dbc.Col([html.P(result), html.P(children=', '.join(trans['tags'])), html.Video(id="video_content", src=source, controls=True)])
    return html.P()


"""
<iframe width="560" height="315" src="https://www.youtube.com/embed/qj06URsDq_0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""


def feed_generate():
    jsn = open('preprocessed.json')
    videos = json.load(jsn)
    list_of_cards = []
    for video in videos:
        list_of_cards.append(
            dbc.Card(
                dbc.Row(
                    [
                        dbc.Col(html.Iframe(src="https://www.youtube.com/embed/" +
                                            video['id'], height=315, width=560)),
                        dbc.Col(video['text'])
                    ], style={'margin': '10px'}
                ), style={'marginBottom': '20px'}
            )
        )
    jsn.close()

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
            # html.Div(dbc.Spinner(color="primary"),
            #          id="cluster-cards", style={'align': 'center'}),

            html.Div(children=feed_generate())

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
    app.run_server(host='0.0.0.0', debug=False)
