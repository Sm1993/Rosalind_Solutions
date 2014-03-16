from __future__ import division
import time
# This program has a time complexity of O((k*k))

def strip_fasta(dna_seq):
    with open("rosalind_pdst.txt",'r') as r:
        raw_str=r.read()
    r.close()

    raw_fasta = [k for k in raw_str if k=='>' or k.isupper()==True and k!='R']

    s="".join(raw_fasta)
    dna_seq=s.split('>')
    del(dna_seq[0])
    return dna_seq


def compare(ele1,ele2):
    count=0
    for i in range(0,len(ele1)):
        if ord(ele1[i])^ord(ele2[i])!=0:
            count += 1

    return count/(len(ele1))



dna_seq=[]
dna_seq=strip_fasta(dna_seq)
run_time=time.time()
count=0
d_matrix_val=[]
d_matrix=[]
for i in dna_seq:
    for j in dna_seq:
        #print i,j
        count=compare(i,j)
        d_matrix_val.append(count)
    d_matrix.append(d_matrix_val)
    d_matrix_val=[]
    count=0
with open("rosalind_pdst_output.txt",'w') as w:
    for ele in d_matrix:
        for val in ele:
            w.write(str(val) + ' ')
        w.write('\n')
w.close()
print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
      
