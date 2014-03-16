import time
# This program has a time complexity of O((k^3))or O((k^3)),dpending on the input size 
# where k = input size

from itertools import product
fin =open('rosalind_lexv.txt','r')
val,n=fin.readlines()
fin.close()
run_time=time.time()
val=val[:-1].split()
val=''.join(val)
n=int(n[:-1])

fout=open("rosalind_lexv_output.txt",'w')
raw_str=val

cart_prod1=list(product(raw_str,repeat=1))

cart_prod2=list(product(raw_str,repeat=2))

cart_prod3=list(product(raw_str,repeat=3))
if(n==4):
    cart_prod4=list(product(raw_str,repeat=4))

l=len(cart_prod1)

for i in range(l):
    fout.write(''.join(cart_prod1[i]) + '\n')
    for j in range(l):
        fout.write(''.join(cart_prod2[l*i+j])+ '\n')
        for k in range(l):
            fout.write(''.join(cart_prod3[l*l*i+l*j+k]) + '\n')
            if(n==4):
                for z in range(l):
                    fout.write(''.join(cart_prod4[l*l*l*i+l*l*j+l*k+z])+ '\n')

fout.close()
print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
