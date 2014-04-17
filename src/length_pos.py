import xml.etree.ElementTree as ET
import decimal



def sentence_length_position(root): 
	#instead of passing root we can use "global root" here
	#returns list of dictionaries that have (sentenceid,normalized length) key-val pair
	#and list of dictionaries that have (sentenceid,normalized position) key-val pair
	len_lst=[] #length
	pos_lst=[] #position

	len_dict={} #length
	pos_dict={} #position
	lmax=1;

	for doc in root.iter('DOC'):
		len_d={}
		pos_d={}
		for text in doc.iter('Text'):
			pos=0
			for sentence in text.iter('Sent'):
				l=len(sentence.text.split())
				id=sentence.attrib['id']
				len_d[id]=l
				pos+=1
				pos_d[id]=pos
				lmax=max(lmax,l)
		for key in len_d.iterkeys():
			len_d[key]=round(decimal.Decimal(len_d[key]*1.0/lmax),4)
		for key in pos_d.iterkeys():
			if pos!=0:
				pos_d[key]=round(decimal.Decimal(pos_d[key]/(1.0*pos)),4)

		len_lst.append(len_d)
		pos_lst.append(pos_d)
		len_dict=dict(len_dict.items()+ len_d.items())
		pos_dict=dict(pos_dict.items()+ pos_d.items())
	#return len_lst,pos_lst
	return len_dict,pos_dict







