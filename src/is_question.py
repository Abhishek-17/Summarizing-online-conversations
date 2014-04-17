import xml.etree.ElementTree as ET
import sets

def is_question(root):
	ques = []
	doc_ques = {}
	q = ['What', 'When', 'How', 'Where', 'Can', 'Do', 'Will', 'Is', 'Could', 'Was', 'Would', 'May','?']
	for doc in root.iter('DOC'):
		
		for text in doc.iter('Text'):
			for sentence in text.iter('Sent'):
				flag=0
				l = sentence.text.split()
				n=len(l)
				last=l[n-1]
				if last[-1:]=='?':
					flag=1
				id = sentence.attrib['id']
				l = set(l)
#				words = [x.lower for x in l]
				qwords = set(q) & l
				if (len(qwords)!=0):
					flag=1
				doc_ques[id]=flag
#				print id, flag, qwords
		#ques.append(doc_ques)
	return doc_ques

if __name__=='__main__':
	filepath="splitted/chunk1.xml"
	tree = ET.parse(filepath)
	root=tree.getroot()
	is_Q = is_question(root)
	print is_Q
