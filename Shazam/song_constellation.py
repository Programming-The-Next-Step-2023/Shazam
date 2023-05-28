import numpy as np
import scipy
from matplotlib import pyplot as plt
from scipy.io.wavfile import read
from scipy import signal
import scipy.io.wavfile as wav


# to do later
# 1. figure out if read_audio function is really necessary

def read_audio(path):
    """This function reads a .wav audio file and returns the sample rate and the data of the audio

        Parameters:
            path(str): the path leading to the .wav audio file

        Returns:
            sample_freq(int): the sample frequency of the audio file
            audio(ndarray): contains data in .wav file
        """
    sample_freq, audio = wav.read(path)
    return sample_freq, audio


def st_fourier_transform(sample_freq, audio):
    """This function makes a list of all frequencies and short fourier transform
        Parameters:
            sample_freq(int): the sample frequency of the audio file
            audio(ndarray): contains data in .wav file


        Returns:
            freq(files): contains a list of all frequencies
            st_fourier_transform(files): contains a list of the short time fourier transform. A list of the fourier
            transform of all time segments that are normalised into positive and negative frequencies.
     """
    win_len_sec = 0.5  # length of the window for short time fourier transform
    win_len_samples = int(win_len_sec * sample_freq)
    win_len_samples += win_len_samples % 2

    # Pad the song to divide evenly into windows
    amount_to_pad = win_len_samples - audio.size % win_len_samples
    audio_input = np.pad(audio, (0, amount_to_pad))
    # Perform a short time fourier transform (stft)
    f, t, Zxx = signal.stft(audio_input, sample_freq,
                            nperseg=win_len_samples,
                            nfft=win_len_samples,
                            return_onesided=True
                            )

    return f, t, Zxx

# testing things without function

# my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
# f, t, Zxx = scipy.signal.stft(my_samples, my_sample_rate)  # possible to add window
# plt.pcolormesh(t, f, np.abs(Zxx), cmap='RdBu')
# plt.title('STFT Magnitude')
# plt.ylabel('Frequency [Hz]')
# plt.xlabel('Time [sec]')
# plt.show()


def create_constellation(frequencies, stft_transform):
    '''Return a list of peak frequencies produced by short time fourier transform
    at different time points throughout the audio,
    refered to as constellation of frequency peaks at each time point
    '''
    constellation_map = []
    num_peaks = 15  # maximum of peaks per time slice

    for time_idx, window in enumerate(stft_transform.T):
        # Spectrum is by default complex; We want real values only
        spectrum = abs(window)
        # Find peaks - these correspond to interesting features
        # Note the distance - want an even spread across the spectrum
        peaks, props = signal.find_peaks(spectrum, prominence=0, distance=200)
        # We only want the most prominent peaks, with a maximum of 15 per time slice
        n_peaks = min(num_peaks, len(peaks))
        # Get the n_peaks largest peaks from the prominences
        largest_peaks = np.argpartition(props["prominences"], -n_peaks)[-n_peaks:]

        for peak in peaks[largest_peaks]:
            frequency = frequencies[peak]
            constellation_map.append([time_idx, frequency])

    return constellation_map

# # one example for testing
# my_sample_rate, my_samples = wav.read('C:/Users/mirth/Documents/GitHub/Shazam/Shazam/output/BeatIt.wav')
# f, t, Zxx = st_fourier_transform(my_sample_rate, my_samples)
# # plt.pcolormesh(t, f, np.abs(Zxx), cmap='RdBu')
# # plt.title('STFT Magnitude')
# # plt.ylabel('Frequency [Hz]')
# # plt.xlabel('Time [sec]')
# # plt.show()
# my_constellation_map = create_constellation(f, Zxx)

