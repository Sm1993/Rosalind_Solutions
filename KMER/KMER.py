import time
# This program has a time complexity of O((k*k)), assuming hashimgs are done in constant time
from itertools import product
with open("rosalind_kmer.txt",'r') as r:
    raw_str=r.read()

r.close()
run_time=time.time()
raw_dna_list=[k for k in raw_str if k.isupper()==True and k!='R']

dna_str=''
for ele in raw_dna_list:
    dna_str += ele

#print dna_str

cart_prod=list(product('ACGT',repeat=4))
temp_str=''
kmer={}
for ele in cart_prod:
    for val in ele:
        temp_str += val
    kmer[temp_str]=0
    temp_str=''

#print kmer
kmer_list = sorted(kmer)

start=0

for key in kmer.keys():

    while start!=-1:
        start=dna_str.find(key,start)
        if start !=-1:
            kmer[key] += 1
            #print kmer[key]
            start += 1
    start=0

result=[]
res=''
for ele in kmer_list:
        ele=str(kmer[ele])
        result.append(ele)
#print result
res= " ".join(result)
with open("rosalind_kmer_output.txt",'w') as w:
    w.write(res)
w.close()

print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
