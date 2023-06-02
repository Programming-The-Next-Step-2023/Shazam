import unittest
from Shazam.converter import converter_wav
import numpy as np
from Shazam.song_constellation import st_fourier_transform
import os
import scipy.io.wavfile as wav


class TestSum(unittest.TestCase):
    def test_converter(self):
        converter_wav(r'Shazam/input', r'Shazam/output')

        # Check if files were saved in the output directory
        files = os.listdir(r'Shazam/output')
        self.assertTrue(len(files) > 0, "No files were saved in the output directory")

        # Check if files are indeed wav files
        for file in files:
            self.assertTrue(file.endswith(".wav"), f"{file} is not a WAV file")

    def test_fourier(self):
        # This test the fourier transformation of one song

        # The output of the st fourier function
        sample_rate, audio = wav.read(r'Shazam/output/BetterBeGoodToMe.wav')
        f, t, zxx = st_fourier_transform(sample_rate, audio)

        # Load the expected array from file
        expected_array_zxx = np.load(r'tests/zxx_test_BetterBeGoodToMe.npy')
        expected_array_f = np.load(r'tests/f_test_BetterBeGoodToMe.npy')

        # Test if the arrays have the same shape, for zxx and f
        self.assertEqual(expected_array_zxx.shape, zxx.shape)
        self.assertEqual(expected_array_f.shape, f.shape)

        # Test if the arrays have the same values
        self.assertTrue(np.array_equal(expected_array_zxx, zxx))
        self.assertTrue(np.array_equal(expected_array_f, f))





if __name__ == '__main__':
    unittest.main()
