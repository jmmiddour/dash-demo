import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# import app and server from application
from app import app, server
# import pages
from pages import page1, page2, callbacks, index


"""
    Creating the base layout
"""
navbar = dbc.NavbarSimple(
    brand="My Awesome Brand",
    brand_href='/',
    children=[
        dbc.NavItem(
            dcc.Link(
                "Page 1",
                href="/page1",
                className="nav-link"
            )
        ),
        dbc.NavItem(
            dcc.Link(
                "Page 2",
                href="/page2",
                className="nav-link"
            )
        ),
        dbc.NavItem(
            dcc.Link(
                "Hollaback",
                href="/holla",
                className="nav-link"
            )
        )
    ],
    sticky="top")

footer = dbc.Container(
    dbc.Row(
        dbc.Col(
            html.P(
            [
                html.Span(
                    "I am awesome",
                    className="mr-2 text-muted small"
                ),
                html.A(
                    html.I(
                        className="fa-envelope mr-1"
                    ),
                href="mailto:bmulas@mail.com"
                ),
                html.A(
                    html.I(
                        className="fa-github mr-1"
                    ),
                href="http://www.google.com"
                ),
                html.A(
                    html.I(
                        className="fa-linkedin mr-1"
                    ),
                href="http://www.google.com"
                ),
                html.A(
                    html.I(
                        className="fa-twitter mr-1"
                    ),
                href="http://www.google.com"
                )
            ],
            className="lead"
            )
        )
    )
)

# Establish layout
app.layout = html.Div([dcc.Location(id='url', refresh=False),
                       navbar,
                       dbc.Container(id="page-content", className='mt-2'),
                       html.Hr(),
                       footer])

# Do the displaying of the pages thing
@app.callback(Output("page-content", "children"),
             [Input("url", "pathname")])
def display_page(pathname):
    if pathname == "/":
        return index.layout
    elif pathname == "/page1":
        return page1.layout
    elif pathname == "/page2":
        return page2.layout
    elif pathname == "/holla":
        return callbacks.layout
    else:
        return dcc.Markdown("### Nope.")

# Do the run thing
if __name__ == "__main__":
    app.run_server(debug=True)
