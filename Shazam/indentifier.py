from song_constellation import st_fourier_transform, create_constellation, read_audio
import scipy.io.wavfile as wav
import numpy as np
import pandas as pd


# Create constellation for song
my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/Bad.wav')
f, t, Zxx = st_fourier_transform(my_sample_rate, my_samples)
my_song_constellation_map = create_constellation(f, Zxx)
my_song_constellation_map = np.asarray(create_constellation(f, Zxx)).T

# Create constellation for snippet
my_sample_rate_snippet, my_samples_snippet = wav.read(
    'C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/Bad_snippet.wav')
f_snippet, t_snippet, Zxx_snippet = st_fourier_transform(my_sample_rate_snippet, my_samples_snippet)
my_snippet_constellation_map = np.asarray(create_constellation(f_snippet, Zxx_snippet)).T


def song_match(song_constellation, snippet_constellation):
    # Determine length of song and snippet
    len_song = int(np.max(my_song_constellation_map, axis=1)[0])  # in timepoints, not in datapoints
    len_snippet = int(np.max(my_snippet_constellation_map, axis=1)[0])
    difference = []
    for index in np.arange(0, len_song, 15):
        max_snippet_index = index + ((len_snippet + 1) * 15)  # length +1 because the last timepoint has
        # 15 datapoints as well
        song_range = my_song_constellation_map[1][index:max_snippet_index]
        match_timepoint = abs(np.subtract(song_range, my_snippet_constellation_map[1]))
        difference.append(sum(match_timepoint))
    best_match = min(difference)
    return(best_match)

print(song_match(my_song_constellation_map, my_snippet_constellation_map))

