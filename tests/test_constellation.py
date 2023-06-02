import unittest
from Shazam.converter import converter_wav
from Shazam.song_constellation import st_fourier_transform
import os


class TestSum(unittest.TestCase):
    def test_converter(self):
        converter_wav(r'Shazam/input', r'Shazam/output')

        # Check if files were saved in the output directory
        files = os.listdir(r'Shazam/output')
        self.assertTrue(len(files) > 0, "No files were saved in the output directory")

        # Check if files are indeed wav files
        for file in files:
            self.assertTrue(file.endswith(".wav"), f"{file} is not a WAV file")

    # def test_fourier:
        # f, t, zxx = st_fourier_transform(r'Shazam/output/BetterBeGoodToMe')





if __name__ == '__main__':
    unittest.main()
