import xml.etree.ElementTree as ET
import re
import math


#sent_dict = {}


def dictMake(root , threadid):
	
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
		
#filepath="annotation.xml"
#tree = ET.parse(filepath)
#root = tree.getroot()
#annoteDict(root)

#for t in threads_ann:
#	filepath="splitted/"+t
#	tree = ET.parse(filepath)
#	root = tree.getroot()
#	ret = dictMake(root , t)
#	annotated_list.append(ret)

#print annotated_list
