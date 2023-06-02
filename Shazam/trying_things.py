import scipy
from song_constellation import st_fourier_transform, create_constellation
import scipy.io.wavfile as wav
import numpy as np
import pandas as pd
from identifier import song_detector
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

sample_rate, audio = wav.read(r'output/BetterBeGoodToMe.wav')
f, t, zxx = st_fourier_transform(sample_rate, audio)
print(type(zxx))
np.save('frequency_test.npy', zxx)
