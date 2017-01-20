import os
import pickle
import pandas as pd
import numpy as np
from scipy.fftpack import fft
from datetime import datetime 
from scipy.io import wavfile as wav
from tqdm import tqdm
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_predict, cross_val_score


data_dir = 'data'

##########################################################
# Create dataframe
print('Create dataframe')
##########################################################

labels = list(os.listdir(data_dir))
x, y = [], []
datacount = {}
for label in tqdm(labels, ncols=80, desc='Labels'):
    files = os.listdir(os.path.join(data_dir, label))
    datacount[label] = len(files)
    for f_name in tqdm(files, ncols=80, desc='Recordings'):
        path = os.path.join(data_dir, label, f_name)
        try:
            rate, data = wav.read(path)
        except:
            print('\n Error while reading file: ', path)
            continue
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
kwargs = dict(n_jobs=-1, n_estimators=40, class_weight='balanced')
y, estimator = le.fit_transform(y), OneVsRestClassifier(RandomForestClassifier(**kwargs))
print('X: {}, Y: {}\n'.format(x.shape, y.shape))

print('-'*5, 'Confusion Matrix', '-'*5)
lines = ['```',str(datetime.now()), 'OvR-RF'+str(kwargs), '', '', 'DataCount',  str(datacount), '', 'Confusion matrix']

cm = confusion_matrix(y, cross_val_predict(estimator, x, y))
for label, row in zip(le.classes_, cm):
    linestring = '{:15}|{}'.format(label, np.round(row / row.sum(), 2))
    lines.append(linestring)
lines.append('```'); lines.extend(['']*3)
# Save performance to README file
with open('README.md', 'a') as fl:
    fl.write('\n'.join(lines))
print('\n'.join(lines))

print('Fitting and saving to file')
estimator.fit(x, y)
with open('Classifier.pickle', 'wb') as file:
    pickle.dump(estimator, file)
with open('LabelEncoder.pickle', 'wb') as file:
    pickle.dump(le, file)
