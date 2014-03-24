import xml.etree.ElementTree as ET

def sentence_length_position(root): 
	#instead of passing root we can use "global root" here
	#returns list of dictionaries that have (sentenceid,normalized length) key-val pair
	#and list of dictionaries that have (sentenceid,normalized position) key-val pair
	len_lst=[] #length
	pos_lst=[] #position
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
			len_d[key]=len_d[key]*1.0/lmax
		for key in pos_d.iterkeys():
			if pos!=0: pos_d[key]/=(1.0*pos)
		len_lst.append(len_d)
		pos_lst.append(pos_d)
	return len_lst,pos_lst

filepath="splitted/chunk0.xml"
tree = ET.parse(filepath)
root = tree.getroot()
length,position=sentence_length_position(root)

print length
print"\n\n-----------------\n\n"
print position






