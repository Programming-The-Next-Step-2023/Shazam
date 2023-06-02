import numpy as np
from scipy import signal


def st_fourier_transform(sample_freq, audio, window_length=0.5):
    """
    Perform the Short-Time Fourier Transform (STFT) on an audio signal.

    Parameters:
        sample_freq (int): The sample frequency of the audio signal.
        audio (ndarray): The audio signal data
        window_length (float): The length of the window for STFT in seconds. Default is 0.5 seconds.

    Returns:
        f (ndarray): The array of frequencies.
        t (ndarray): The array of time segments.
        zxx (ndarray): The STFT matrix containing the transformed values.
    """

    # Normalize the audio data by dividing the audio by the maximum absolute value of the signal
    normalized_audio = audio / np.max(np.abs(audio))

    # Decide number of samples needed to cover the desired window length
    window_length_samples = int(window_length * sample_freq)

    # Perform the Short-Time Fourier Transform (STFT)
    f, t, zxx = signal.stft(normalized_audio, sample_freq,
                            window='hann',  # Apply a Hann window for better frequency resolution
                            nperseg=window_length_samples,  # Set the window length for each segment
                            noverlap=window_length_samples // 2,  # Set the overlap between segments
                            return_onesided=True)

    return f, t, zxx


def create_constellation(frequencies, stft_transform):
    """
    Return a list of peak frequencies produced by the Short-Time Fourier Transform
    referred to as the constellation of frequency peaks at each time point.

    Parameters:
        frequencies (ndarray): Array of frequencies.
        stft_transform (ndarray): Short-Time Fourier Transform.

    Returns:
        constellation_map (list): List of [time_idx, frequency] pairs.
    """
    constellation_map = []
    num_peaks = 15  # Maximum number of peaks per time slice

    # Iterate over each time index and window in the short-time Fourier transform
    for time_idx, window in enumerate(stft_transform.T):
        spectrum = abs(window)  # Calculate the magnitude spectrum of the window

        # Find the peaks in the spectrum
        peaks, _ = signal.find_peaks(spectrum, prominence=0, distance=200)

        # Determine the number of peaks to consider
        n_peaks = min(num_peaks, len(peaks))

        # Select the largest peaks based on their magnitudes
        largest_peaks = peaks[np.argsort(-spectrum[peaks])[:n_peaks]]

        # Append the [time_idx, frequency] pairs of the largest peaks to the constellation map
        for peak in largest_peaks:
            constellation_map.append(frequencies[peak])

    return constellation_map
