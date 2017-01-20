import os
import sys
import pickle
import subprocess
import numpy as np
from tqdm import tqdm
from scipy.fftpack import fft
from datetime import datetime 
from scipy.io import wavfile as wav
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import cross_val_predict

__version__ = (0, 1, 0, 0) # Breaking release, Release, update, misc

def predict_label(filename, estimator, label_encoder):
    "Predict class for a given filename"
    rate, data = wav.read(filename)
    data = data[:, 0] if len(data.shape) > 1 else data
    data = fft(data)[:20000]
    data = np.sqrt(np.power(data.real, 2) + np.power(data.imag, 2))

    # Predict
    label = estimator.predict([data])
    return label_encoder.inverse_transform(label)[0].strip()

def get_classifier_and_label_encoder():
    "Read the classifier and label encoder from file"
    # ----------estimator
    estimator = None
    if not os.path.exists('Classifier.pickle'):
        print('Please put a Classifier.pickle file in the current directory')
        sys.exit(-1)
    else:
        with open('Classifier.pickle', 'rb') as file:
            estimator = pickle.load(file)
    # ----------label encoder
    le = None
    if not os.path.exists('LabelEncoder.pickle'):
        print('Please put a LabelEncoder.pickle file in the current directory')
        sys.exit(-1)
    else:
        with open('LabelEncoder.pickle', 'rb') as file:
            le = pickle.load(file)
    return estimator, le

def record_data(filename, timelimit=None):
    "Record audio using aplay"
    command = 'arecord -r 44000 {}.wav'
    if timelimit is None:
        os.system(command.format(filename))
    else:
        with subprocess.Popen(command.format(filename), shell=True) as process:
            try:
                process.wait(timeout=timelimit)
            except subprocess.TimeoutExpired:
                print('timeout')
                process.send_signal(2)  # Ctrl+C

def listen():
    "Infinite loop to listen and predict"
    estimator, le = get_classifier_and_label_encoder()
    while True:
        input('Press enter to start recording and press Ctrl+C to stop. ::>')
        os.system('arecord -r 44000 temp.wav')
        label = predict_label('temp.wav', estimator, le)
        print(label)

def handle_recording(target_file_count=None):
    ##########################################################
    # RECORD DATA
    ##########################################################
    limit = list(filter(lambda x: 'wav' in x, os.listdir('.')))
    limit = len(list(sorted(limit)))
    if target_file_count is None:
        i = limit
        print('starting count at ', i)
        while True:
            i += 1
            record_data(i, 5)
    else:
        for i in range(limit, int(target_file_count)):
            quit = input('Press q to quit. Press Ctrl+c to stop recording. Press Enter to start recording: ')
            if quit.strip() == 'q':
                print('Quitting')
                sys.exit(0)
            record_data(i)

def handle_training(data_dir):
    "Train the classifier"
    ##########################################################
    print('Create dataframe')
    ##########################################################
    labels, datacount = list(os.listdir(data_dir)), {}
    x, y = [], []
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
            x.append(data); y.append(label)
    ##########################################################
    # Run classifier
    print('\nRun classifier')
    ##########################################################

    x, le = np.array(x), LabelEncoder()
    kwargs = dict(n_jobs=-1, n_estimators=40, class_weight='balanced')
    y, estimator = le.fit_transform(y), OneVsRestClassifier(RandomForestClassifier(**kwargs))
    print('Generating Confusion Matrix')

    lines = [str(datetime.now()), 'OvR-RF'+str(kwargs), '', '', 'DataCount',  str(datacount), '', 'Confusion matrix']

    cm = confusion_matrix(y, cross_val_predict(estimator, x, y))
    for label, row in zip(le.classes_, cm):
        linestring = '{:15}|{}'.format(label, np.round(row / row.sum(), 2))
        lines.append(linestring)
    print('\n'.join(lines))

    print('Completing fitting and saving to file')
    estimator.fit(x, y)
    with open('Classifier.pickle', 'wb') as file:
        pickle.dump(estimator, file)
    with open('LabelEncoder.pickle', 'wb') as file:
        pickle.dump(le, file)
##########################################################
# MAIN STUFF
##########################################################
def main():
    try:
        sys.argv[1]
    except IndexError:
        listen()
    else:
        need = sys.argv[1]
        if need == 'record':
            try:
                target_file_count = int(sys.argv[2])
            except IndexError:  # Infinite samples of 5 seconds
                target_file_count = None
            handle_recording(target_file_count)
        elif need == 'train':
            try:
                data_dir = sys.argv[2]
            except IndexError:
                data_dir = 'data'
            handle_training(data_dir)
if __name__ == '__main__':
    main()
