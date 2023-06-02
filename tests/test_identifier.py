import unittest
from Shazam.converter import converter_wav
import numpy as np
from Shazam.song_constellation import st_fourier_transform, create_constellation
from Shazam.identifier import song_match
import pickle
import os
import scipy.io.wavfile as wav


class TestIndentify(unittest.TestCase):
    def test_song_match(self):
        """describe this function"""

        # Create song match with the use of the function
        # with open(r'tests/constellation_test_BetterBeGoodToMe.pkl', 'rb') as file:
        #     constellation_song = pickle.load(file)
        #
        # with open(r'tests/constellation_test_BetterBeGoodToMe.pkl', 'rb') as file:
        #     constellation_snippet = pickle.load(file)

        my_match = song_match(constellation_song, constellation_snippet)

        # Load in expected song match



if __name__ == '__main__':
    unittest.main()
