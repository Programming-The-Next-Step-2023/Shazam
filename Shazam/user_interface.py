import base64
import dash
from dash import dcc
from dash import html
from dash import dash_table
from indentifier import song_detector
import pandas as pd
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)


def create_bordered_div(title, children):
    return html.Div(
        children=[
            html.H3(title),
            html.Div(
                style={
                    'border': '2px solid black',
                    'padding': '10px'
                },
                children=children
            )
        ]
    )


app.layout = html.Div([
    html.Div(
            html.Img(src=r'assets/logo_shazam.png', alt='image')
    ),
    html.Div(
        id='left-section',
        style={'float': 'left', 'width': '45%'},
        children=[
            create_bordered_div('Predicted Song', html.Div(id='output-predicted-song')),
            create_bordered_div('Dataframe Matches', html.Div(id='output-data-table'))
        ]
    ),
    html.Div(
        id='right-section',
        style={'float': 'right', 'width': '45%'},
        children=[
            create_bordered_div('Input File', html.Div(id='output-file-name')),
            html.Div(
                style={'margin-top': '10px'},
                children=dcc.Upload(
                    id='upload-audio',
                    children=html.Button('Upload File', style={'height': '40px', 'width': '120px'})
                )
            )
        ]
    )
])

@app.callback(Output('output-file-name', 'children'),
              Output('output-data-table', 'children'),
              Output('output-predicted-song', 'children'),
              Input('upload-audio', 'contents'),
              State('upload-audio', 'filename'))
def update_output(contents, filename):
    if contents is not None:
        content_type, content_string = contents.split(',')
        with open(r'uploads/my_upload.wav', "wb") as f:
            decode_string = base64.b64decode(content_string)
            f.write(decode_string)

            # Perform song matching or any other required processing here
            # For now, we will create a sample dataframe
            df, best_song, best_match = song_detector(r'uploads/my_upload.wav')

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
