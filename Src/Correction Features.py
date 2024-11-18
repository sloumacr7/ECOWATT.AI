#  Reactive Power
import numpy as np

def calculate_power_factors(voltage, current):
    """
    Calculate power factor based on voltage and current waveforms.
    """
    active_power = np.mean(voltage * current)
    apparent_power = np.sqrt(np.mean(voltage**2) * np.mean(current**2))
    power_factor = active_power / apparent_power
    return power_factor

#   Harmonic distortion  

from scipy.fftpack import fft

def calculate_thd(signal, sampling_rate):
    """
    Calculate Total Harmonic Distortion (THD) of a signal.
    """
    N = len(signal)
    freqs = fft(signal)
    harmonics = np.abs(freqs[1:int(N/2)])
    fundamental = harmonics[0]
    thd = np.sqrt(np.sum(harmonics[1:]**2)) / fundamental
    return thd
