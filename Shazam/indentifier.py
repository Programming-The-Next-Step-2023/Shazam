from song_constellation import st_fourier_transform, create_constellation
import scipy.io.wavfile as wav
import numpy as np
import pandas as pd

my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
f, t, Zxx = st_fourier_transform(my_sample_rate, my_samples)
my_song_constellation_map = create_constellation(f, Zxx)

match_result = pd.DataFrame()

# def match_snippet(snippet_constellation, song_constellation):
#     len_song = max(song_constellation)[0]
#     len_snippit = max(snippet_constellation)[0]
#     timepoints = range(0, len_song)
#     index =
#     for timepoint in timepoints:
#         max_snippit_range = timepoint + len_snippit



my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
f, t, Zxx = st_fourier_transform(my_sample_rate, my_samples)
my_song_constellation_map = create_constellation(f, Zxx)
my_song_constellation_map = np.asarray(create_constellation(f, Zxx)).T
# print(my_song_constellation_map)

my_sample_rate_snippet, my_samples_snippet = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt_snippet.wav')
f_snippet, t_snippet, Zxx_snippet = st_fourier_transform(my_sample_rate_snippet, my_samples_snippet)
my_snippet_constellation_map = np.asarray(create_constellation(f_snippet, Zxx_snippet)).T
# print(my_snippet_constellation_map)

len_song = int(np.max(my_song_constellation_map, axis=1)[0])
len_snippet = int(np.max(my_snippet_constellation_map, axis=1)[0])
# print(range(0, (len_song - len_snippet)))
match = []
for timepoint in range(0, (len_song - len_snippet)):
    max_snippet_index = (timepoint + len_snippet) * 15
    song_range = my_song_constellation_map[timepoint:max_snippet_index]
    difference = np.subtract(song_range[1], my_snippet_constellation_map[1])
    # match.append()
    if (timepoint % 1000 == 0):
        print(difference)


