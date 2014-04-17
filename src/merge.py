#Author: Abhishek

from tf_isf import tf_isf_main,tf_isf
from centroid_coherence import centroid_coherence
from length_pos import sentence_length_position
from tf_idf import tf_idf
from title_simm import *
from tf_isf_old import *
#from Annotations import annotated_list 
import xml.etree.ElementTree as ET
import pickle
from is_question import is_question

train_list = []



def dictMake(root , threadid):# sentence id: y/n tag
	
	sent_dict={}
	for doc in root.iter('DOC'):
		for text in doc.iter('Text'):
			for sent in text.iter('Sent'):
				val = sent.attrib
				#print val['id']
				sent_dict.update({val['id']:'n'})
				
	fi = "SummaryThreads/"+threadid
	tree = ET.parse(fi)
	root = tree.getroot()

	for s in root.iter('sentences'):
		for sid in s.iter('sent'):
			val = sid.attrib
			
			if val['id'] in sent_dict:
				sent_dict[val['id']] = 'y'
			
	#print sent_dict			
	return sent_dict

def annoteDict(root):
	threads_ann = []
	for lst in root.iter('listno'):
		threads_ann.append(lst.text)
	return threads_ann
	#print threads_ann


def merge(filepath=""):#path of chunk file
	#merges the feature vectors together so that they can be used in Naive bayes
	#return a dictionary ( sentenceid: featureVector)
	tree = ET.parse(filepath)
	root = tree.getroot()
	coherence_dict=centroid_coherence(root) #sentid: coherence
	tf_isf_dict=tf_isf(root,1) #sentid: total tf_isfscore
	tf_idf_dict=tf_idf(root)
	length_dict,position_dict=sentence_length_position(root)
	title_simm_dict = title_simm_main1(filepath)
	is_question_dict= is_question(root)
	#print title_simm_dict
	ans={}
	for sentid in coherence_dict.iterkeys():
		d={"coherence":coherence_dict[sentid],"tfIsf":0,"tfIdf":0,"length":0,"position":0,"titleSimm":0,"isQues":0}
		if tf_isf_dict.has_key(sentid):
			d["tfIsf"]=tf_isf_dict[sentid]
		if tf_idf_dict.has_key(sentid):
			d["tfIdf"]=tf_idf_dict[sentid]
		if length_dict.has_key(sentid):
			d["length"]=length_dict[sentid]
		if position_dict.has_key(sentid):
			d["position"]=position_dict[sentid]
		if title_simm_dict.has_key(sentid):
			d["titleSimm"]=title_simm_dict[sentid]
		if is_question_dict.has_key(sentid):
			d["isQues"]=is_question_dict[sentid]
		ans[sentid]=d


	return ans

def getTrainingData(folder=""):

	if folder=="":  folder="splitted"
	if folder[-1]!="/":folder+="/"
	#folder="splitted/"
	filepath="annotation.xml"
	tree = ET.parse(filepath)
	root = tree.getroot()
	threads_ann = annoteDict(root) #get the ids of thread

	annotated_list=[] #sentnce id: y/n  ; list of dictionaries

	for t in threads_ann:
		if t=="107-16164699":continue
		filepath=folder+t

		tree = ET.parse(filepath)
		root = tree.getroot()
		ret = dictMake(root , t)
		annotated_list.append(ret)


	i = 0
	train = []
		
	for t in threads_ann:
		if t=="107-16164699":continue
		filepath=folder+t
	
		res = merge(filepath)
		for w in res:
			val = annotated_list[i][w]
			train.append((res[w] , val))
		i = i + 1
	return train

	# train list is final list of training data. directly import merge and use the train_list as training dataset
	#train_list.append(train)





	#with open('trainingset.pickle', 'wb') as handle:
	#	pickle.dump(train, handle)

