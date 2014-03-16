import time
# This program has a time complexity of O((k*k*k))
# where k = length of strings
import sys
def get_string():
	with open("rosalind_kmp.txt",'r') as r:
		raw_str=r.read()
	r.close()
	run_time=time.time()
	raw_str=raw_str.split('\n')
	#print raw_str
	dna_str=""
	i=0
	for ele in raw_str:

		i +=1
		if ele=='':
			pass
			
		else:
			if ele[0]=='>' :
				pass
			else:
				dna_str +=ele
	print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"


	return dna_str		


s = get_string()
p = [0] * len(s)

for j in xrange(1, len(s)):
	for k in xrange(len(s) - j):
		if s[j + k] != s[k]:
			break
		p[j + k] = max(p[j + k], k + 1)
with open("rosalind_kmp_output.txt",'w') as w:
	w.write( ' '.join(map(str, p)))
w.close()

