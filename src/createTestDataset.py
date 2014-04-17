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
from merge import *



	


def getTestdata(filepath=""):#chunk to be tagged

	# Location of test data file	
	#filepath="testSplitted/107-16164699"
	test_data = []
	sent_ids = []

	res = merge(filepath)# get fvs for bayse
	for w in res:
		test_data.append((res[w]))
		sent_ids.append(w)
	#test data is the list to feed into the classifier
	#sentence ids are the corresponding sids for the test data 
	return sent_ids,test_data
