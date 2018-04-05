import random

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

app = dash.Dash()

colors = {
    'background':'#111111',
    'text':'#7FDBFF'
}

# read in CSV
df = pd.read_csv(
    'https://gist.githubusercontent.com/chriddyp/'
    'c78bf172206ce24f77d6363a2d754b59/raw/'
    'c353e8ef842413cae56ae3920b8fd78468aa4cb2/'
    'usa-agricultural-exports-2011.csv')

def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]


    )

def generate_prediction():
    return random.random()

# style={'backgroundColor': colors['background']}
app.layout = html.Div(children=[
    html.H1(
        'Hello Dash',
        style={
            'textAlign': 'center',
            # 'color': colors['text']
        }
    ),

    html.Div(
        'Dash: A web application framework for Python.',
        style={
            'textAlign': 'center',
            # 'color': colors['text']
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1,2,3], 'y': [4,1,2], 'type': 'bar', 'name': 'SF'},
                {'x': [1,2,3], 'y': [2,4,5], 'type': 'bar', 'name': u'Montreal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                }
            }
        }
    ),

    html.Div(
        [
            html.H4('US Agriculture Exports (2011)'),
            generate_table(df)
        ]
    )

    # html.Div(
    #     [
    #         'Table from Pandas',
    #         html.H2('Prediction : {0:.2f}'.format(generate_prediction()))
    #     ],
    #     style={
    #         'textAlign': 'center',
    #     }
    # ),

])

app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)