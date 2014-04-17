import xml.etree.ElementTree as ET
import re
import math
from tf_isf_old import *

tf_isf_sentence = []
title_simm_dict = {}
def title_simm(root, tf_isf_sentence):
	#return a list of lists of cosine simmilarity of title with sentences of the doc
	
	tf_isf_list = [] 
	sub_count = 0
	
	for sub in root.iter('Subject'):
		sub_count = sub_count + 1
		tf_isf_dict = {}
		sub.text = sub.text.lower()
		words = sub.text.split(' ')
		for w in words:
			m = re.search("[a-z]+",w)
			if m != None:
				keyword = m.group()
				if keyword in tf_isf_dict:
					tf_isf_dict[keyword] = tf_isf_dict[keyword] + 1
				else:
					tf_isf_dict[keyword] = 1	
		tf_isf_list.append(tf_isf_dict)
	
	isf_dict = {}
	for sub in tf_isf_list:
		for w in sub:
			if w in isf_dict:
				isf_dict[w] = isf_dict[w] + 1
			else:
				isf_dict[w] = 1
	
	for w in isf_dict:
		score = 0
		val1 = 0
		if 1 + isf_dict[w] < sub_count:
			val1 = sub_count / float(1 + isf_dict[w])
		else:
			val1 = sub_count / float(isf_dict[w])	
		if val1 > 0:
			score = math.log(val1,10)
		isf_dict[w] = score
	
	for sub in tf_isf_list:
		max1 = 0
		for w in sub:
			if sub[w] > max1:
				max1 = sub[w]
		for w in sub:
			sub[w] = sub[w] / float(max1)	
	
	for sub in tf_isf_list:
		for w in sub:
			sub[w] = sub[w] * isf_dict[w]
		#print sub
				
	docid = -1
	dot_prod = []
			
	for d in tf_isf_sentence:
		docid = docid + 1
		sum1 = 0
		dot_per_sent = []
		for s in d:
			for w in s:
				val = 0
				if w in tf_isf_list[docid]:
					val = s[w] * tf_isf_list[docid][w]
					sum1 = sum1 + val
			dot_per_sent.append(sum1)
		dot_prod.append(dot_per_sent)

	mag_title = []
	

	for i in range(0,docid+1):
		sum1 = 0
		for w in tf_isf_list[i]:
			val = tf_isf_list[i][w] * tf_isf_list[i][w]
			sum1 = sum1 + val
		mag_title.append(math.sqrt(sum1))
	

	mag_doc = []
	docid = -1;
	for d in tf_isf_sentence:
		docid = docid + 1
		mag_per_sent = []
		for s in d:
			sum1 = 0
			for w in s:
				val = s[w]*s[w]
				sum1 = sum1 + val
			sum1 = math.sqrt(sum1)
			sum1 = sum1 * mag_title[docid]	
			mag_per_sent.append(sum1)
		mag_doc.append(mag_per_sent)
		
	#print ""
	docid = -1
	for d in dot_prod:
		docid = docid + 1
		sentid = -1
		for s in d:
			sentid = sentid + 1
			if s < mag_doc[docid][sentid]:
				s = s /float( mag_doc[docid][sentid] )
			
	cosine = []
	for d in dot_prod:
		cosine.append(d)		

	#print cosine
	
	did = 1
	sid = 1
	for l in cosine:
		for c in l:
			val = str(did) +"." + str(sid)
			title_simm_dict.update({val:c})
			sid = sid + 1
		did = did + 1
		sid = 1	
	return title_simm_dict
	

def title_simm_main1(filename):
	#print filename	
	filepath=filename
	tree = ET.parse(filepath)
	root = tree.getroot()

	tf_isf_sentence = tf_isf_old(filepath)
	tree = ET.parse(filepath)
	root = tree.getroot()
	
	final_dict = title_simm(root , tf_isf_sentence)
	#print final_dict
	return final_dict
#title_simm_main1("splitted/007-7484738")
