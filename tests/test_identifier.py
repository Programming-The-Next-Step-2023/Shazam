import unittest
from Shazam.identifier import song_detector
import pickle
import os


class TestIndentify(unittest.TestCase):
    def test_song_detector(self):
        """test if the correct prediction is made"""
        expected = ['BetterBeGoodToMe.wav']
        actual = song_detector(r'../Shazam/snippets/BetterBeGoodToMe_snippet.wav')[1]

        self.assertEqual(expected, actual, "This is the wrong prediction")

    def test_input(self):
        """test if the correct file format is uploaded"""
        wav_file_path = r'../my_upload.wav'

        # Check if the file has a .wav extension
        self.assertTrue(wav_file_path.lower().endswith('.wav'), "Input is not a WAV file")





if __name__ == '__main__':
    unittest.main()
