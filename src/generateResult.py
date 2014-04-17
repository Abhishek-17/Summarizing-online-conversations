import pickle

with open('testdataset.pickle', 'rb') as handle:
  test = pickle.load(handle)

with open('sentenceids.pickle', 'rb') as handle:
  sids = pickle.load(handle)

#print test

