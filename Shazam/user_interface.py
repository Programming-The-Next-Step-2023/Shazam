import dash
from dash import dcc
from dash import html
from dash import dash_table
from indentifier import song_detector
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Upload(
        id='upload-audio',
        children=html.Button('Upload File')
    ),
    html.Div(id='output-file-name'),
    html.Div(id='output-data-table'),
    html.Div([
        html.H3('Predicted Song'),
        html.Div(
            id='output-predicted-song',
            style={
                'border': '2px solid black',
                'padding': '10px'
            }
        )
    ])
])


@app.callback(Output('output-file-name', 'children'),
              Output('output-data-table', 'children'),
              Output('output-predicted-song', 'children'),
              Input('upload-audio', 'contents'),
              State('upload-audio', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        # Perform song matching or any other required processing here
        # For now, we will create a sample dataframe
        df, best_song, best_match = song_detector(filename)

        # Display the name of the uploaded file
        file_name_output = html.H5(f'Uploaded File: {filename}')
        # Display the name of the predicted song
        output_best_song = html.H5(best_song)

        # Display the resulting dataframe
        data_table_output = dash_table.DataTable(
            id='data-table',
            columns=[{'name': col, 'id': col} for col in df.columns],
            data=df.to_dict('records')
        )

        return file_name_output, data_table_output, output_best_song

    return None, None, None


if __name__ == '__main__':
    app.run_server(debug=True)
