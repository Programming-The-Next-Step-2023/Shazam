# import scipy
# from song_constellation import st_fourier_transform, create_constellation, read_audio
# import scipy.io.wavfile as wav
# import numpy as np
# import pandas as pd
# from indentifier import song_detector
# import plotly.express as px
#
# # File to save code that might be useful later and to test things out.
# # Not necessary for peer review.
#
#
# # get data for testing
# # my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
# # test_1, test_2, test_3 = st_fourier_transform(my_sample_rate, my_samples)
# # test_3 = np.array(test_3[0][0:10])
# # print(test_3)
# # np.savetxt('test_array_3', test_3)
#
# # df = song_detector('BeatIt_snippet.wav')
# # best_row = df[df['Match']==df['Match'].min()]
# # best_song = list(best_row['Song'])
# # print(best['Song'])
#
# # My_matches, best_song, best_match = song_detector(r'snippets/PrivateDancer_snippet.wav')
# # print(My_matches)
# # fig = px.bar(My_matches, x='Song', y='Match')
# # fig.show()
#
# import base64
# import time
# import dash
# from dash import dcc
# from dash import html
# from dash import dash_table
# from indentifier import song_detector
# import pandas as pd
# import plotly.express as px
# from dash.dependencies import Input, Output, State
#
#
# app = dash.Dash(__name__)
#
# def create_bordered_div(title, children):
#     return html.Div(
#         children=[
#             html.H3(title),
#             html.Div(
#                 style={
#                     'border': '2px solid black',
#                     'padding': '10px'
#                 },
#                 children=children
#             )
#         ]
#     )
#
# app.layout = html.Div([
#     html.Div(
#         html.Img(src='assets/logo_shazam_2.png', alt='image')
#     ),
#     html.Div(
#         id='left-section',
#         style={'float': 'left', 'width': '45%'},
#         children=[
#             create_bordered_div('Predicted Song', html.Div(id='output-predicted-song')),
#             create_bordered_div('Dataframe Matches', html.Div(id='output-data-table'))
#         ]
#     ),
#     html.Div(
#         id='right-section',
#         style={'float': 'right', 'width': '45%'},
#         children=[
#             create_bordered_div('Input File', html.Div(id='output-file-name')),
#             html.Div(
#                 style={'margin-top': '10px'},
#                 children=dcc.Upload(
#                     id='upload-audio',
#                     children=html.Button('Upload File', style={'height': '40px', 'width': '120px'})
#                 )
#             ),
#             html.Div(
#                 id='loader-container',
#                 children=[
#                     dcc.Loading(
#                         id='loading',
#                         type='circle',
#                         color='#000000',
#                         children=[html.Div(id='loader-output')]
#                     )
#                 ]
#             )
#         ]
#     ),
#     html.Div(
#         dcc.Graph(id='output-bar-plot'), style={'display': 'none'})
# ])
#
# @app.callback(
#     Output('loader-output', 'children'),
#     Output('output-file-name', 'children'),
#     Output('output-data-table', 'children'),
#     Output('output-predicted-song', 'children'),
#     Output('output-bar-plot', 'figure'),
#     Output('output-bar-plot', 'style'),
#     Input('upload-audio', 'contents'),
#     State('upload-audio', 'filename'))
# def update_output(contents, filename):
#     if contents is not None:
#
#         # Save uploaded song file
#         content_type, content_string = contents.split(',')
#         with open('uploads/my_upload.wav', "wb") as f:
#             decode_string = base64.b64decode(content_string)
#             f.write(decode_string)
#
#         # Perform song_detector function to extract matches to snippet
#         df, best_song, best_match = song_detector('uploads/my_upload.wav')
#
#         # Display the name of the uploaded file
#         file_name_output = html.H5(f'Uploaded File: {filename}')
#         # Display the name of the predicted song
#         output_best_song = html.H5(best_song)
#
#         # Display the dataframe with matches
#         data_table_output = dash_table.DataTable(
#             id='data-table',
#             columns=[{'name': col, 'id': col} for col in df.columns],
#             data=df.to_dict('records')
#         )
#
#         # display plot
#         if not df.empty:
#             fig = px.bar(df, x='Song', y='Match')
#             plot_style = {'display': 'block'}
#         else:
#             fig = {}
#             plot_style = {'display': 'none'}
#
#         # Hide loader and show outputs
#         return None, file_name_output, data_table_output, output_best_song, fig, plot_style
#     else:
#         # Hide loader and do not display any outputs
#         return None, None, None, None, {}, {'display': 'none'}
#
# if __name__ == '__main__':
#     app.run_server(debug=True)
#
#
#
