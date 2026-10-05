import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

df = pd.read_csv('Salary_Data.csv')
app = Dash()
app.title = "Interactive Dashboard"
num_cols = df.select_dtypes(include='number').columns

app.layout = html.Div([
    html.H1("Interactive Dashboard with pie plot"),
    html.Label("select a value to show in the pie char"),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'Label':col,'value':col} for col in num_cols],
        value=num_cols[0]),
        dcc.Graph(id='pie-char')



])

if __name__ == '__main__':
    app.run(debug=True, port=8051)