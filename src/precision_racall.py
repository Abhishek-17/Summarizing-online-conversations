import re
fi_res = open("resultids","rb")
fi_sum = open("givenids","rb")

total_res = 0
total_summ = 0

givenids = {}
resids = {}
st = fi_sum.readline()
while st:
	total_summ = total_summ + 1
	st = re.sub('\n', '', st)
	if st[-1]=='\r': st=st[:-1]
	givenids[st] = 1

	st = fi_sum.readline()


st = fi_res.readline()
while st:
	total_res = total_res + 1
	st = re.sub('\n', '', st)
	resids[st] = 1
	st = fi_res.readline()

found = 0
#print givenids
#print resids
for sid in resids:
	if sid in givenids:
#		print sid
		resids[sid] = 2
		found = found + 1
#print "found="+str(found)
precision = float(found )/ float(total_res)
print "precision :"+str(precision)

matched = 0

for sid in givenids:
	if sid in resids:
		matched = matched + 1

recall = float(matched) / float(total_summ)

print "recall :"+str(recall)

