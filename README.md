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

# Passively record 5 second samples
python record.py
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
2017-01-19 13:55:47.147176
RF{'class_weight': 'balanced', 'n_jobs': -1, 'n_estimators': 30}

Confusion matrix
__silence      |[ 0.84  0.16  0.  ]
no             |[ 0.03  0.97  0.  ]
yes            |[ 0.02  0.03  0.95]
```

```
2017-01-19 14:38:39.780316
OvR-RF{'class_weight': 'balanced', 'n_jobs': -1, 'n_estimators': 30}


DataCount
{'yes': 65, 'no': 65, '__silence': 174}

Confusion matrix
__silence      |[ 0.99  0.01  0.  ]
no             |[ 0.02  0.98  0.  ]
yes            |[ 0.03  0.02  0.95]
```


```
2017-01-19 15:28:42.902340
OvR-RF{'n_estimators': 30, 'n_jobs': -1, 'class_weight': 'balanced'}


DataCount
{'__silence': 484, 'yes': 65, 'no': 65}

Confusion matrix
__silence      |[ 1.  0.  0.]
no             |[ 0.03  0.97  0.  ]
yes            |[ 0.06  0.02  0.92]
```


```
2017-01-19 21:59:13.946171
OvR-RF{'n_estimators': 30, 'n_jobs': -1, 'class_weight': 'balanced'}


DataCount
{'no': 65, 'movies': 100, '__silence': 484, 'yes': 65}

Confusion matrix
__silence      |[ 1.  0.  0.  0.]
movies         |[ 0.02  0.86  0.03  0.09]
no             |[ 0.02  0.02  0.97  0.  ]
yes            |[ 0.03  0.22  0.02  0.74]
```


```
2017-01-19 22:03:59.392004
OvR-RF{'n_estimators': 30, 'class_weight': 'balanced', 'n_jobs': -1}


DataCount
{'__silence': 484, 'movies': 100, 'yes': 100, 'no': 65}

Confusion matrix
__silence      |[ 1.  0.  0.  0.]
movies         |[ 0.03  0.85  0.02  0.1 ]
no             |[ 0.03  0.03  0.94  0.  ]
yes            |[ 0.03  0.14  0.03  0.8 ]
```


```
2017-01-19 22:06:52.359614
OvR-RF{'n_jobs': -1, 'n_estimators': 50, 'class_weight': 'balanced'}


DataCount
{'no': 65, '__silence': 484, 'yes': 100, 'movies': 100}

Confusion matrix
__silence      |[ 1.  0.  0.  0.]
movies         |[ 0.06  0.82  0.02  0.1 ]
no             |[ 0.03  0.02  0.95  0.  ]
yes            |[ 0.03  0.16  0.02  0.79]
```


```
2017-01-19 22:07:49.821013
OvR-RF{'n_estimators': 100, 'class_weight': 'balanced', 'n_jobs': -1}


DataCount
{'__silence': 484, 'movies': 100, 'no': 65, 'yes': 100}

Confusion matrix
__silence      |[ 1.  0.  0.  0.]
movies         |[ 0.03  0.85  0.02  0.1 ]
no             |[ 0.02  0.02  0.97  0.  ]
yes            |[ 0.03  0.16  0.03  0.78]
```


```
2017-01-19 22:09:33.344876
OvR-RF{'n_estimators': 100, 'n_jobs': -1, 'class_weight': 'balanced'}


DataCount
{'no': 65, 'movies': 100, 'yes': 100, '__silence': 484}

Confusion matrix
__silence      |[ 1.  0.  0.  0.]
movies         |[ 0.03  0.87  0.02  0.08]
no             |[ 0.03  0.02  0.95  0.  ]
yes            |[ 0.02  0.14  0.04  0.8 ]
```


```
2017-01-20 17:08:10.982897
OvR-RF{'class_weight': 'balanced', 'n_jobs': -1, 'n_estimators': 100}


DataCount
{'yes': 100, 'no': 65, 'movies': 100, '__silence': 725}

Confusion matrix
__silence      |[ 1.  0.  0.  0.]
movies         |[ 0.05  0.84  0.02  0.09]
no             |[ 0.03  0.02  0.95  0.  ]
yes            |[ 0.03  0.14  0.02  0.81]
```


```
2017-01-20 17:09:44.718766
OvR-RF{'class_weight': 'balanced', 'n_estimators': 100, 'n_jobs': -1}


DataCount
{'movies': 100, 'yes': 100, 'no': 65}

Confusion matrix
movies         |[ 0.84  0.02  0.14]
no             |[ 0.02  0.97  0.02]
yes            |[ 0.13  0.04  0.83]
```


```
2017-01-20 17:10:43.239006
OvR-RF{'class_weight': 'balanced', 'n_estimators': 40, 'n_jobs': -1}


DataCount
{'no': 65, 'movies': 100, 'yes': 100}

Confusion matrix
movies         |[ 0.85  0.02  0.13]
no             |[ 0.02  0.97  0.02]
yes            |[ 0.13  0.03  0.84]
```


