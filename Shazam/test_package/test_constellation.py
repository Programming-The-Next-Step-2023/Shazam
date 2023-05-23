import unittest
import numpy as np
import scipy.io.wavfile as wav
from Shazam import st_fourier_transform, create_constellation


class TestSum(unittest.TestCase):
    def test_fourier(self):
        test_sample_rate, test_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
        f_test, t_test, zxx_test = st_fourier_transform(test_sample_rate, test_samples)
        self.assertAlmostEqual(zxx_test[0][0:10].tolist(),
                               np.array([(2.372516086325049400e-03 + 0.000000000000000000e+00j),
                                         (5.641081929206848145e-02 + 0.000000000000000000e+00j),
                                         (-4.679023623466491699e-01 + 0.000000000000000000e+00j),
                                         (4.768476262688636780e-02 + 0.000000000000000000e+00j),
                                         (-7.247638106346130371e-01 + 0.000000000000000000e+00j),
                                         (-1.361043214797973633e+00 + 0.000000000000000000e+00j),
                                         (3.514563441276550293e-01 + 0.000000000000000000e+00j),
                                         (8.664387464523315430e-02 + 0.000000000000000000e+00j),
                                         (-1.088629722595214844e+00 + 0.000000000000000000e+00j),
                                         (-4.302865266799926758e-01 + 0.000000000000000000e+00j)]).tolist())


if __name__ == '__main__':
    unittest.main()
