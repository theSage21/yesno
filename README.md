YesNo
=====

Records samples of your voice and stores them.
Then runs a classifier on it and shows you the prediction metrics


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
