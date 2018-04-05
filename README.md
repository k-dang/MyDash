# Dash

apps are made of 2 parts

1. layout
    describes what the application looks like
2. interactivity
    describes the interavtivity of the application

dash provides python classes for all the visual components

layout is composed of a tree of components:

html.Div - can define a list of components
dcc.Graph

children property is special, is always the first attribute, so you can emit it

add css to the app object:
`app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})`

can also define some inline styles as python dictionary
add style as a parameter to the calls to dash_html_components