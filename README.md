YesNo
=====

May be used to recognize spoken words. Three files are available.

1. `record.py`: Records multiple samples ofaudio using `arecord` in the current directory.
2. `train.py`: Trains a classifier and label encoder to recognize the words stored in the `data` directory..
3. `predict.py`: Given a recording as argument predict's what it is saying

Usage
-----

To set up the data you may perform the following

```bash
mkdir data && cd data
mkdir yes && cd yes

# Record 100 samples of you saying yes
python ../../record.py 100
```

To build the classifier you may do the following

```bash
python train.py
```

To predict the label of a given recording we can:

`python predict.py recording.wav`

All audio files in use must be having a sampling rate of 44000 Hz.


Train Metrics
-------------

```
2017-01-19 10:36:30.388405

Confusion matrix
   no[ 0.98461538  0.01538462]
  yes[ 0.03076923  0.96923077]
```


```
2017-01-19 11:16:40.886842
{'n_jobs': -1, 'n_estimators': 30}

Confusion matrix
   no[ 0.98461538  0.01538462]
  yes[ 0.01538462  0.98461538]
```


```
2017-01-19 11:17:52.066204
RF{'n_estimators': 30, 'n_jobs': -1}

Confusion matrix
   no[ 0.98461538  0.01538462]
  yes[ 0.03076923  0.96923077]
```


```
2017-01-19 11:17:57.416147
RF{'n_estimators': 30, 'n_jobs': -1}

Confusion matrix
   no[ 0.98461538  0.01538462]
  yes[ 0.01538462  0.98461538]
```


