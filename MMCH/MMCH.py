import time
# This program has a time complexity of O((k+l)), assuming factorial alone takes O(k)
# where l = length of string

from math import factorial
with open("rosalind_mmch.txt",'r') as r:
    raw_str=r.read()

r.close()

run_time=time.time()
rna_str=raw_str[13:-1]

#print rna_str,len(rna_str)

dict={'A':0,'U':0,'G':0,'C':0}
for char in rna_str:
    if char == 'A':
        dict[char] += 1
    elif char == 'U':
        dict[char] += 1
    elif char == 'G':
        dict[char] += 1
    elif char == 'C':
        dict[char] += 1
        
possibility=1

#print dict['A'],dict['G'],dict['U'],dict['C']

possibility *= (factorial(max(dict['A'],dict['U']))/factorial(max(dict['A'],dict['U'])-min(dict['A'],dict['U']))) * (factorial(max(dict['G'],dict['C']))/factorial(max(dict['G'],dict['C'])-min(dict['G'],dict['C'])))  
print possibility

print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
