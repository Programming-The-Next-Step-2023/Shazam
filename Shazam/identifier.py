from song_constellation import st_fourier_transform, create_constellation
import scipy.io.wavfile as wav
import numpy as np
import os
from converter import converter_wav
import pandas as pd
import pickle


def song_match(song_constellation, snippet_constellation):
    """
    Determine the match between a snippet of a song and a song based on a difference score.

    Parameters:
        song_constellation (list): Constellation map of frequencies for the song.
        snippet_constellation (list): Constellation map of frequencies for the snippet.

    Returns:
        best_match (float): The best match score between the snippet and the song.
    """

    # Determine length of song and snippet
    len_song = len(song_constellation)
    len_snippet = len(snippet_constellation)

    # Create empty list
    difference = []

    # Loop over every time sample and compare the snippet constellation to the song constellation
    for index in np.arange(0, (len_song - len_snippet), 15):
        max_snippet_index = index + len_snippet
        song_range = song_constellation[index:max_snippet_index]
        match_timepoint = abs(np.subtract(song_range, snippet_constellation))
        difference.append(sum(match_timepoint))  # Append difference of this time point
    best_match = min(difference)  # Find the best match within the song
    return best_match


def song_detector(mp3_snippet_dir):
    # Converts mp3 songs in the input folder, only if the folder is empty
    song_list = os.listdir(r'output')
    if len(song_list) == 0:
        converter_wav(r'input', r'output')
        song_list = os.listdir(r'output')

    # Create constellation map for snippet
    sample_frequency_snippet, audio_snippet = wav.read(mp3_snippet_dir)
    f_snippet, t_snippet, zxx_snippet = st_fourier_transform(sample_frequency_snippet, audio_snippet)
    snippet_constellation_map = np.asarray(create_constellation(f_snippet, zxx_snippet)).T

    # Create empty dataframe to store match of the song compared to snippet
    matches = pd.DataFrame({'Song': [], 'Match': []})

    # If the constellation map of the song is already in the constellation folder, it does not need to create the
    # constellation again. Loop over every song and determine if the constellation map should be constructed and stored.
    constellation_directory = 'constellation_maps'
    output_directory = 'output'

    for song in song_list:
        file_path = os.path.join(constellation_directory, song + '.pkl')
        if os.path.isfile(file_path):

            # Load the constellation map; if it was already stored.
            with open(file_path, 'rb') as file:
                song_constellation_map = pickle.load(file)

        # Otherwise, create the constellation map and store it.
        else:
            sample_frequency_song, audio_song = wav.read(os.path.join(output_directory, song))
            f_song, t_song, zxx_song = st_fourier_transform(sample_frequency_song, audio_song)
            song_constellation_map = np.asarray(create_constellation(f_song, zxx_song)).T

            # Store the constellation map
            with open(file_path, 'wb') as file:
                pickle.dump(song_constellation_map, file)

        # Determine match
        current_match = song_match(song_constellation_map, snippet_constellation_map)
        new_row = {'Song': song, 'Match': current_match}
        matches = matches.append(new_row, ignore_index=True)
        best_row = matches[matches['Match'] == matches['Match'].min()]
        best_song = list(best_row['Song'])
        best_match = list(best_row['Match'])
    return matches, best_song, best_match
