import os
import pickle
import pandas as pd
import numpy as np
from scipy.fftpack import fft
from scipy.io import wavfile as wav
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_predict, cross_val_score


data_dir = 'data'

##########################################################
# Create dataframe
print('Create dataframe')
##########################################################

if not os.path.exists('dataframe.csv'):
    labels = list(os.listdir(data_dir))
    x, y = [], []
    for label in tqdm(labels, ncols=80, desc='Labels'):
        files = os.listdir(os.path.join(data_dir, label))
        for f_name in tqdm(files, ncols=80, desc='Recordings'):
            path = os.path.join(data_dir, label, f_name)
            rate, data = wav.read(path)
            if len(data.shape) > 1:
                data = data[:, 0]  # Only one channel
            # FFT
            data = fft(data)[:20000]  # First 20k freq
            # Just the magnitude of complex number
            data = np.sqrt(np.power(data.real, 2) + np.power(data.imag, 2))
            x.append(data)
            y.append(label)
##########################################################
# Run classifier
print('\nRun classifier')
##########################################################

x, le = np.array(x), LabelEncoder()
y, estimator = le.fit_transform(y), RandomForestClassifier(n_jobs=-1, n_estimators=20)
print('X: {}, Y: {}\n'.format(x.shape, y.shape))

print('-'*5, 'Confusion Matrix', '-'*5)
cm = confusion_matrix(y, cross_val_predict(estimator, x, y))
for label, row in zip(le.classes_, cm):
    print(label.zfill(5).replace('0', ' '), row / row.sum())

print('Fitting and saving to file')
estimator.fit(x, y)
with open('Classifier.pickle', 'wb') as file:
    pickle.dump(estimator, file)
with open('LabelEncoder.pickle', 'wb') as file:
    pickle.dump(le, file)
