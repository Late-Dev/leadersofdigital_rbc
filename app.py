from dash import html, dcc, Dash
import dash_bootstrap_components as dbc
from dash.dependencies import Output, State, Input


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
    dbc.Container(children="hello")
])

index_page = html.Div([
    navbar,
    dbc.Container(children=[
        dbc.Container(children=[
            dbc.Row([
                html.H1('Темы новостей', style={'margin': '10px'}),
                # html.Div('Здесь расположены карточки со статьями'),
                # html.Div('Сортировка карточек от новой к старой'),
                # html.Div('в карточке открыта новейшая и закрыты старые статьи'),
                # html.Div('Заголовок карточки - тематика'),
                dbc.Button('обновить', id='reload-button',
                           className="mb-3", style={'margin': '10px'}),
            ]),
            # dcc.Store(id='clusters'),
            html.Div(dbc.Spinner(color="primary"),
                     id="cluster-cards", style={'align': 'center'})

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
