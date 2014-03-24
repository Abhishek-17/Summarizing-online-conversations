fi = open("corpus.xml","r")
i=0
chunkname = "splitted/chunk"+str(i)+".xml"
fo = open(chunkname,"w")

while 1:
	str1 = fi.readline()
	fo.write(str1)
	if str1.find("/thread") > 0:
		i = i + 1
		chunkname = "splitted/chunk"+str(i)+".xml"
		fo = open(chunkname,"w")

