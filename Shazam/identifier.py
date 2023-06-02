from song_constellation import st_fourier_transform, create_constellation
import scipy.io.wavfile as wav
import numpy as np
import os
from converter import converter_wav
import pandas as pd


def song_match(song_constellation, snippet_constellation):
    # Determine length of song and snippet
    len_song = len(song_constellation)
    len_snippet = len(snippet_constellation)
    difference = []
    for index in np.arange(0, (len_song - len_snippet), 15):
        max_snippet_index = index + len_snippet
        song_range = song_constellation[index:max_snippet_index]
        match_timepoint = abs(np.subtract(song_range, snippet_constellation))
        difference.append(sum(match_timepoint))
    best_match = min(difference)
    return best_match


def song_detector(mp3_snippet_dir):
    converter_wav(r'input', r'output')
    song_list = os.listdir(r'output')
    # Create constellation map for snippet
    sample_frequency_snippet, audio_snippet = wav.read(mp3_snippet_dir)
    f_snippet, t_snippet, zxx_snippet = st_fourier_transform(sample_frequency_snippet, audio_snippet)
    snippet_constellation_map = np.asarray(create_constellation(f_snippet, zxx_snippet)).T
    # Create empty dataframe to store match of the song compared to snippet
    matches = pd.DataFrame({'Song': [], 'Match': []})
    for song in song_list:
        # Create constellation map
        sample_frequency_song, audio_song = wav.read(r'output/' + song)
        f_song, t_song, zxx_song = st_fourier_transform(sample_frequency_song, audio_song)
        song_constellation_map = np.asarray(create_constellation(f_song, zxx_song)).T
        # Determine match
        current_match = song_match(song_constellation_map, snippet_constellation_map)
        new_row = {'Song': song, 'Match': current_match}
        matches = matches.append(new_row, ignore_index=True)
        best_row = matches[matches['Match'] == matches['Match'].min()]
        best_song = list(best_row['Song'])
        best_match = list(best_row['Match'])
    return matches, best_song, best_match
