import numpy as np

def rms(sig_arr, window, sampling_rate=2148):
    '''
    sig_arr       -- signal array to process
    window        -- in terms of seconds
    sampling_rate -- the sampling rate of the recorded signal, default is 2148 Hz
    '''
    window *= sampling_rate
    window = int(window)
    rms = [np.sqrt(np.mean(sig_arr[idx - window:idx] ** 2)) for idx in range(window, sig_arr.shape[0], window)]
    return np.asarray(rms)

def iemg(sig_arr, window, sampling_rate=2148):
    '''
    sig_arr       -- signal array to process
    window        -- in terms of seconds
    sampling_rate -- the sampling rate of the recorded signal, default is 2148 Hz
    '''
    window *= sampling_rate
    window = int(window)
    iemg = [np.sum(abs(sig_arr[idx - window:idx])) for idx in range(window, sig_arr.shape[0], window)]
    return np.asarray(iemg)

def mav(sig_arr, window, sampling_rate=2148):
    '''
    sig_arr       -- signal array to process
    window        -- in terms of seconds
    sampling_rate -- the sampling rate of the recorded signal, default is 2148 Hz
    '''
    window *= sampling_rate
    window = int(window)
    mav = [np.sum(np.absolute(sig_arr[idx - window:idx]))/window for idx in range(window, sig_arr.shape[0], window)]
    return np.asarray(mav)