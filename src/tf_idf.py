import xml.etree.ElementTree as ET
import re
import math
import decimal

def tf_idf(root): 
	tfList = []
	df_dictionary = {}
	idf_dictionary = {}
	doc_count = 0
	for doc in root.iter('DOC'):
		doc_count = doc_count + 1
		tf_dictionary = {}
		for text in doc.iter('Text'):
			for sentence in text.iter('Sent'):
				sentence.text = sentence.text.lower()
				words = sentence.text.split(' ')
				for i in words:
					m = re.search("[a-z]+",i)
					if m != None:
						keyword = m.group()
						if keyword in tf_dictionary:
							tf_dictionary[keyword] = tf_dictionary[keyword] + 1
						else:
							tf_dictionary.update({keyword:1})
						
		tfList.append(tf_dictionary)	
	
	for dct in tfList:
		maxtf = 0
		for word in dct:
			if dct[word] > maxtf:
				maxtf = dct[word]
		for word in dct:
			dct[word] = dct[word] / float(maxtf)		
	
	#print tfList
	
	for dict1 in tfList:
		for j in dict1:
			if j in df_dictionary:
				df_dictionary[j] = df_dictionary[j] + 1
			else:
				df_dictionary.update({j:1})
	
	#print df_dictionary
	#print "========================"
	
	#print doc_count
	for word in df_dictionary:
		idf_score = 0
		val1 = (doc_count / (1 + df_dictionary[word]))
		if val1 > 0:
			idf_score = math.log(val1 , 10)
				
		idf_dictionary.update({word:idf_score})			
	
	#print idf_dictionary				
	
	for dict1 in tfList:
		for word in dict1:
			idf_score = idf_dictionary[word]
			val1 = dict1[word]
			val1 = val1 * idf_score
			dict1.update({word:val1})
	#return tfList
	#------------------------ tf-idf score for sentence
	#tfList	 : [{},{},{}..] each dictionary is for a doc and has (word:tf_idf)
	doc_ct=0
	ans={}
	for doc in root.iter('DOC'):
		for text in doc.iter('Text'):
			for sentence in text.iter('Sent'):
				id=sentence.attrib['id']
				score=0 #total tf-idf score of sentence
				sentence.text = sentence.text.lower()
				words = sentence.text.split(' ')
				length=1+len(words) # sentence length
				for i in words:
					m = re.search("[a-z]+",i)
					if m != None:
						keyword = m.group()
						if tfList[doc_ct].has_key(keyword):
							score+=tfList[doc_ct][keyword]#add tf-idf of words of sentence
				score=score*1.0/length #normalized
				ans[id]	=round(decimal.Decimal(score),4)
						
		doc_ct+=1
	return ans #has sentId:totalTF-idfScore key-val pair

	
	
		







