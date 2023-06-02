import unittest
from Shazam.converter import converter_wav
import numpy as np
from Shazam.song_constellation import st_fourier_transform, create_constellation
import os
import pickle
import scipy.io.wavfile as wav


class TestAudioProcessing(unittest.TestCase):
    def test_converter(self):
        """This function tests if the converter stores the converted files in the output folder"""

        converter_wav(r'Shazam/input', r'Shazam/output')

        # Check if files were saved in the output directory
        files = os.listdir(r'Shazam/output')
        self.assertTrue(len(files) > 0, "No files were saved in the output directory")

        # Check if files are indeed wav files
        for file in files:
            self.assertTrue(file.endswith(".wav"), f"{file} is not a WAV file")

    def test_fourier(self):
        """"This tests the fourier transformation for one song"""

        # The output of the st fourier function
        sample_rate, audio = wav.read(r'Shazam/output/BetterBeGoodToMe.wav')
        f, t, zxx = st_fourier_transform(sample_rate, audio)

        # Load the expected array from file
        expected_array_zxx = np.load(r'tests/zxx_test_BetterBeGoodToMe.npy')
        expected_array_f = np.load(r'tests/f_test_BetterBeGoodToMe.npy')

        # Test if the arrays have the same shape, for zxx and f
        self.assertEqual(expected_array_zxx.shape, zxx.shape, "the zxx has the incorrect shape")
        self.assertEqual(expected_array_f.shape, f.shape, "the f has the incorrect shape")

        # Test if the arrays have the same values
        self.assertTrue(np.array_equal(expected_array_zxx, zxx), "the zxx has the incorrect values")
        self.assertTrue(np.array_equal(expected_array_f, f), "the f has the incorrect values")

    def test_create_constellation(self):
        """This tests the constellation for one song"""

        # Create constellation based on function
        sample_rate, audio = wav.read(r'Shazam/output/BetterBeGoodToMe.wav')
        f, t, zxx = st_fourier_transform(sample_rate, audio)
        constellation = create_constellation(f, zxx)

        # Read in priorly created constellation for song 'better be good to me'
        with open(r'tests/constellation_test_BetterBeGoodToMe.pkl', 'rb') as file:
            expected_constellation = pickle.load(file)

        # Test if the arrays have the same shape
        self.assertEqual(len(expected_constellation), len(constellation), "the song constellation has a "
                                                                          "incorrect length")
        # It is not possible to check for the values because the function returns different values every time.


if __name__ == '__main__':
    unittest.main()
