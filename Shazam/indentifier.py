from song_constellation import st_fourier_transform, create_constellation, read_audio
import scipy.io.wavfile as wav
import numpy as np
import os
from convert_wav import converter
import pandas as pd


def song_match(song_constellation, snippet_constellation):
    # Determine length of song and snippet
    len_song = len(song_constellation[0])
    len_snippet = len(snippet_constellation[0])
    difference = []
    for index in np.arange(0, (len_song - len_snippet), 15):
        max_snippet_index = index + len_snippet
        song_range = song_constellation[1][index:max_snippet_index]
        match_timepoint = abs(np.subtract(song_range, snippet_constellation[1]))
        difference.append(sum(match_timepoint))
    best_match = min(difference)
    return best_match


def song_detector(mp3_dir, wav_dir, mp3_snippet_dir):
    converter(mp3_dir, wav_dir)
    song_list = os.listdir(wav_dir)
    # Create constellation map for snippet
    sample_frequency_snippet, audio_snippet = read_audio(mp3_snippet_dir)
    f_snippet, t_snippet, Zxx_snippet = st_fourier_transform(sample_frequency_snippet, audio_snippet)
    snippet_constellation_map = np.asarray(create_constellation(f_snippet, Zxx_snippet)).T
    # Create empty dataframe to store match of the song compared to snippet
    matches = pd.DataFrame({'Song': [], 'Match': []})
    for song in song_list:
        # Create constellation map
        sample_frequency_song, audio_song = read_audio(wav_dir + '/' + song)
        f_song, t_song, Zxx_song = st_fourier_transform(sample_frequency_song, audio_song)
        song_constellation_map = np.asarray(create_constellation(f_song, Zxx_song)).T
        # Determine match
        current_match = song_match(song_constellation_map, snippet_constellation_map)
        new_row = {'Song': song, 'Match': current_match}
        matches = matches.append(new_row, ignore_index=True)
    return matches


My_matches = song_detector('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/input', 'C:/Users/mirth/Documents/GitHub'
                                                                                  '/Shazam/Shazam/output',
                           'C:/Users/mirth/Documents/GitHub/Shazam/Shazam/snippets/Bad_snippet.wav')
print(My_matches)
