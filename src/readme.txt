//execute merge.py and createDataset.py on terminal

on python console


>>>from datasetLoader import train
>>>from generateResult import test,sids 

>>>import nltk
>>>nltk.usage(nltk.classify.ClassifierI)

>>>classifier = nltk.classify.NaiveBayesClassifier.train(train) 

>>>result = classifier.batch_classify(test)


>>>i = 0
for r in result:
	if r == 'y':
		print sids[i]    # would give corresponding sids

	i = i+1	
