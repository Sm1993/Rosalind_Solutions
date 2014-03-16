str1=raw_input("Enter Dna seq1\n")
str2=raw_input("Enter Dna_seq 2\n")

i=0
transition=0
transversion=0
for i in range(len(str1)):
	#print str1[i] ,str2[i]
	if str1[i] == str2[i]:
		pass
	if str1[i]=='A':
		if str2[i]=='G':
			transition +=1
		elif str2[i]=='C' or str2[i]=='T':
			transversion +=1
	if str1[i]=='G':
		if str2[i]=='A':
			transition +=1
		elif str2[i]=='C' or str2[i]=='T':
			transversion +=1
			
	if str1[i]=='C':
		if str2[i]=='T':
			transition +=1
		elif str2[i]=='A' or str2[i]=='G':
			transversion +=1		
	if str1[i]=='T':
		if str2[i]=='C':
			transition +=1
		elif str2[i]=='A' or str2[i]=='G':
			transversion +=1


print transition/float(transversion)
