from dash import Dash, html, dcc,Input
from dash.dependencies import Input, Output


app = Dash(__name__)
app.layout =html.Div([
    html.Button('Submit',id ='number'),
    dcc.Input(placeholder ="Enter a vaild number",
               id = 'Data',type ='number'),
    html.H1(id ='Resuit')])

@app.callback(Output ('Resuit','chaidern') ,
              Input('number','n_clicks'))
def play_data(n,data):
    if n:
        return f"your enter:{data}"
    return ""
app.run(debug=True)