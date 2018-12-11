#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utility functions to process speech waveforms.

For Metis Weeks 9-12, Project Kojak.

@author: Steven Bierer
Created on Wed Nov  28, 2018
"""

import numpy as np
import glob

import pyaudio 
#import librosa
import soundfile as sf

from scipy import signal
from sklearn.decomposition import NMF



def play_nstaudio(wav, sample_rate, buffer_size=1024):
    """ Play "wav" data ('nist sphere' format) over audio speakers."""
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1, rate=sample_rate,
                    frames_per_buffer=buffer_size,
                    output=True, output_device_index=1
                    )
    
    stream.write(wav.astype(np.float32).tostring())
    stream.stop_stream() 
    stream.close()
    p.terminate()


def log_spectrogram(wav, sample_rate, window_size=40, nfft=None,
                 step_size=20, freq_lim=None, eps=1e-10):
    """Create a log-amplitude spectrogram from an audio waveform.
    
    Arguments:  wav = audio time series data as an array; sample_rate in Hz;
                window_size and step_size in msec (step<window -> overlap);
                nfft as integer (None=samples in window);
                freq_lim = tuple of low and high frequencies to keep, in Hz;
                eps = small value to facilitate taking log amplitude
    
    Adapted from davids1992 on Kaggle.com.
    """
    nperseg = int(round(window_size * sample_rate / 1e3))
    noverlap = int(round(step_size * sample_rate / 1e3))
    freqs, times, spec = signal.spectrogram(wav, fs=sample_rate, window='hann',
            nfft=nfft, nperseg=nperseg, noverlap=noverlap, detrend=False)
    
    if freq_lim:
        fa_idx = freqs.searchsorted(freq_lim[0])
        fb_idx = min(freqs.searchsorted(freq_lim[1]),len(freqs)-1)
        freqs = freqs[fa_idx:fb_idx+1]
        spec = spec[fa_idx:fb_idx+1,:]
#        print(f'Spectrogram truncated to {fb_idx-fa_idx+1} frequency bins.')
    
    return freqs, times, np.log(spec.astype(np.float32) + eps)

def get_wavfiles(base, region, speaker):
    """Return list of audio files (full path) from TIMIT corpus."""
    wavdir = base + '/'.join((region, speaker))
    wavlist = glob.glob(wavdir+'/*.WAV')
    
    return wavlist

def nmf_decomp(X, n_components=6, alpha=0, l1_ratio=0):
    """Nonnegative matrix factorization of X = W * H.
    
    For spectrograms, X should be #time bins x # frequency bins. This makes H
    a dictionary of spectral features and W their activations over time.
    H is normalized by its matrix norm to avoid arbitrary scaling.
    """
    X = X + abs(X.min())        # make sure data is nonnegative
        
    nmf_model = NMF(n_components, solver='mu', beta_loss='kullback-leibler', max_iter=400,
                    alpha=alpha, l1_ratio=l1_ratio)
    W = nmf_model.fit_transform(X)
    H = nmf_model.components_
    
    # W2 = transform(X2)
    hnorm = np.linalg.norm(H)
    W = W * hnorm
    H = H / hnorm
    
    return W, H

def create_groupdict(group_info, ncomp = 8, frange = (0,6000), trim=None, 
                     alpha=0.0, l1_ratio=0.0):
    """Create groups of speakers, each defining a household audio device.
    
    Arguments: 'group_info' gives instructions for grouping in terms of gender
    and dialect region; 'ncomp' is number of components for NMF; 'frange' is
    the low and high frequency content (up to Nyquist rate) in Hz; 'trim'
    is a scaling factor for removing silent periods from the audio (value
    of 1-100 often works, with higher=more aggressive; default is None)"""
    
    nspeaker = len(group_info['speakers'])

    spkrDict = []
    spkrID = []
    
    for j in range(nspeaker):
        for wfile in group_info['train'][j]:
            # Calculate spectrogram from audio file; reject quiet parts #
            wav, srate = sf.read(wfile)
            freqs, times, SS = \
                log_spectrogram(wav, srate, freq_lim=frange)
            SS = SS + abs(SS.min())
            
            if trim:  # optionally remove quiet portions (little low-freq energy)
                SSavg = SS[2:102,:].mean(axis=0)
                cutoff = (SSavg[4:].max()/SS[:2].max()) * trim
                SS_trimmed = SS[:,SSavg > cutoff*SSavg[:2].mean()]
                if SS_trimmed.shape[1] >= 0.3*SS.shape[1]:
                    SS = SS_trimmed
#            SSavg = SS[:40,:].sum(axis=0)   # low-freq power vs time
#            cutoff = (SSavg[4:].mean()/SS[:2].max()) * 0.66  # self-scale
#            SSon = SS[:,SSavg > cutoff*SSavg[:2].mean()]

            # Perform nonnegative matrix decomp and concat dictionaries #
            W, H = nmf_decomp(SS.T, ncomp, alpha=alpha, l1_ratio=l1_ratio)
        
            spkrDict.append(H.T)  # transpose to match Zegers+vH paper
            spkrID.append(j)      # each wav file has a speaker label
    
    # Convert output to arrays #
    spkrDict = np.hstack(spkrDict)  # #freq bins x (NCOMP*nspkr*nwav)
    spkrID = np.array(spkrID, ndmin=2)
    spkrID = spkrID.repeat(ncomp, axis=0).flatten(order='F')

    return spkrDict, spkrID