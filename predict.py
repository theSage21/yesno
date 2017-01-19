import os
import sys
import pickle
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile as wav

##########################################################
# Read classifier
##########################################################
if not os.path.exists('Classifier.pickle'):
    print('Please put a Classifier.pickle file in the current directory')
    sys.exit(-1)
else:
    with open('Classifier.pickle', 'rb') as file:
        estimator = pickle.load(file)

if not os.path.exists('LabelEncoder.pickle'):
    print('Please put a LabelEncoder.pickle file in the current directory')
    sys.exit(-1)
else:
    with open('LabelEncoder.pickle', 'rb') as file:
        le = pickle.load(file)


##########################################################
# Predict
##########################################################

try:
    recording = sys.argv[1]
except IndexError:
    print('No recording given')
    print('Usage: python predict.py <recording.wav>')
    sys.exit(-1)
else:
    # Get recording
    rate, data = wav.read(sys.argv[1])
    data = data[:, 0] if len(data.shape) > 1 else data
    data = fft(data)[:20000]
    data = np.sqrt(np.power(data.real, 2) + np.power(data.imag, 2))

    # Predict
    label = estimator.predict([data])
    print(le.inverse_transform(label)[0].strip())
