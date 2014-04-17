from tf_isf import tf_isf
import xml.etree.ElementTree as ET
import re
from math import sqrt
import decimal

def centroid_coherence(root):#path of chunk.xml
	#return a list of list which contains the centroid-coherence of each sentence. Each sublist represents a doc in the chunk

	#tree = ET.parse(filepath)
	#root = tree.getroot()
	tf_isf_feature,sent_ids = tf_isf(root)

		#tf_isf_feature
		#[[{},{},{}..],[],[],..]
		#list which contains list of dictionaries.
		# the list represents a whole chunk
		# the sublist represent a doc
		# the dictionaries have (word:tf-isf) key-pair

		#sent_ids
		#list of list conatining sentence ids

	#print tf_isf_feature
	centroid=[] # contains centroid(a dictionary of word - meanTf-isf) of each doc of the chunk  [{},{},{}..]

	for doc in tf_isf_feature:
		centroid_tmp={}
		for sent in doc:#a dict
			for word in sent.iterkeys():
				if centroid_tmp.has_key(word):
					centroid_tmp[word]+=sent[word] #summing tf-isf
				else: centroid_tmp[word]=sent[word]
		l=len(doc)# total no of sentences
		if l==0:l=1.0
		for key in centroid_tmp.iterkeys():
			centroid_tmp[key]/=(l*1.0)
		centroid.append(centroid_tmp)

	coherence=[] 
	for i,doc in enumerate(tf_isf_feature):
		coherence_temp=[]
		val=0
		for key in centroid[i].iterkeys():# magnitude of vector
			val+=(centroid[i][key]*centroid[i][key])
		val=sqrt(val)
		for sent in doc:
			#now find similarity b/w sent and the centrod[i]
			val_sent=0.0
			similarity=0.0
			for key in sent.iterkeys():# magnitude of vector
				val_sent+=(sent[key]*sent[key])
				if centroid[i].has_key(key):
					similarity+=(sent[key]*centroid[i][key])
			val_sent=sqrt(val_sent)
			deno=val*val_sent
			if deno==0:deno=1
			similarity/=(deno*1.0)
			coherence_temp.append(similarity)
		coherence.append(coherence_temp)
	#print coherence
	#print sent_ids

	#-----------------------------------------add id
	ans={}

	for i,sublist in enumerate(coherence):#doc
		for j,score in enumerate(sublist):#sentence
			ans[sent_ids[i][j]]=round(decimal.Decimal(score),4)
	return ans #dictionary of sent-id: coherence














