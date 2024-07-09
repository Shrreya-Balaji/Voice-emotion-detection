import numpy as np
import os
from os.path import dirname, join

import _multiprocessing
_multiprocessing.sem_unlink = None

import librosa
from keras.models import load_model


def test(path):
    model_path = os.path.join(dirname(__file__), '5c_model_60.h5')
    model = load_model(model_path)
    local_results = []

    _min, _max = float('inf'), -float('inf')
    _min,_max

    class Config:
        def __init__(self, n_mfcc = 26, n_feat = 13, n_fft = 552, sr = 22050, window = 0.4, test_shift = 0.1):
            self.n_mfcc = n_mfcc
            self.n_feat = n_feat
            self.n_fft = n_fft
            self.sr = sr
            self.window = window
            self.step = int(sr * window)
            self.test_shift = test_shift
            self.shift = int(sr * test_shift)

    config = Config()

    wav, sr = librosa.load(path)

    X = []


    for i in range(int((wav.shape[0]/sr-config.window)/config.test_shift)):
        X_sample = wav[i*config.shift: i*config.shift + config.step]
        X_mfccs = librosa.feature.mfcc(X_sample, sr, n_mfcc = config.n_mfcc, n_fft = config.n_fft,hop_length = config.n_fft)[1:config.n_feat + 1]

        _min = min(np.amin(X_mfccs), _min)
        _max = max(np.amax(X_mfccs), _max)
        X.append(X_mfccs)


    X = np.array(X)
    X = (X - _min) / (_max - _min)
    X = X.reshape(X.shape[0], X.shape[1], X.shape[2], 1)


    for i in range(X.shape[0]):
        window = X[i].reshape(1, X.shape[1], X.shape[2], 1)
        local_results.append(model.predict(window))


    local_results = (np.sum(np.array(local_results), axis = 0)/len(local_results))[0]
    local_results = list(local_results)

    prediction = np.argmax(local_results)

    return prediction