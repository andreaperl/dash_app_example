#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(__name__)
server =app.server

app.layout = html.Div([
    dcc.Input(id='my-id', value='initial value', type="text"),
    html.Div(id='my-div')
])
#mn output is empty until here

@app.callback(
    Output(component_id='my-div', component_property='children'), #if we want output to be a graph, do it here
    [Input(component_id='my-id', component_property='value')]
)
def update_output_div(input_value):
    return 'You\'ve entered. WOW!!! "{}"'.format(input_value) #--and here: we would need to write fun to regenerate graph every time input is changed 

if __name__ == '__main__':
    app.run_server()

