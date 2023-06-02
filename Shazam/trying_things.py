import scipy
from song_constellation import st_fourier_transform, create_constellation
import scipy.io.wavfile as wav
import pickle
import numpy as np
import pandas as pd
# from identifier import song_detector, song_match
import plotly.express as px
import os

# File to save code that might be useful later and to test things out.
# Not necessary for peer review.


# get data for testing
# my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
# test_1, test_2, test_3 = st_fourier_transform(my_sample_rate, my_samples)
# test_3 = np.array(test_3[0][0:10])
# print(test_3)
# np.savetxt('test_array_3', test_3)

# df = song_detector('BeatIt_snippet.wav')
# best_row = df[df['Match']==df['Match'].min()]
# best_song = list(best_row['Song'])
# print(best['Song'])

# My_matches, best_song, best_match = song_detector(r'snippets/PrivateDancer_snippet.wav')
# print(My_matches)
# fig = px.bar(My_matches, x='Song', y='Match')
# fig.show()

# sample_rate, audio = wav.read(r'snippets/BetterBeGoodToMe_snippet.wav')
# f, t, zxx = st_fourier_transform(sample_rate, audio)
#
# # np.save(r'../tests/f_test_BetterBeGoodToMe.npy', f)
# constellation_snippet = create_constellation(f, zxx)
#
#
# # print(type(constellation))
# with open(r'../tests/constellation_test_BetterBeGoodToMe_snippet.pkl', 'wb') as file:
#     pickle.dump(constellation_snippet, file)
#

# # Create song match with the use of the function
# with open(r'../tests/constellation_test_BetterBeGoodToMe.pkl', 'rb') as file:
#     constellation_song = pickle.load(file)
#
# with open(r'../tests/constellation_test_BetterBeGoodToMe_snippet.pkl', 'rb') as file:
#     constellation_snippet = pickle.load(file)

# print(constellation_song)
# print(constellation_snippet)
# my_match = song_match(constellation_song, constellation_snippet)

# len_song = len(constellation_song[0])
# len_snippet = len(constellation_snippet[0])
# difference = []
# for index in np.arange(0, (len_song - len_snippet), 15):
#     max_snippet_index = index + len_snippet
#     song_range = constellation_song[1][index:max_snippet_index]
#     match_timepoint = abs(np.subtract(song_range, constellation_snippet[1]))
#     difference.append(sum(match_timepoint))
#     print(difference)
# print(difference)
# best_match = min(difference)
# print(difference)

# print(my_match)

#
# sample_rate, audio = wav.read(r'../Shazam/output/PrivateDancer.wav')
# f, t, zxx = st_fourier_transform(sample_rate, audio)
# constellation = create_constellation(f, zxx)
# print(constellation)

song = 'test'
print(str(r'constellation_maps' + song + '.pkl'))

