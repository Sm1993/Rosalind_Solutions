import time
# This program has a time complexity of O((k)) where k is the length of the input
ref_table={ round(71.03711,4) : 'A',
            round(103.00919,4) : 'C',
            round(115.02694,4) : 'D',
            round(129.04259,4) : 'E',
            round(147.06841,4) : 'F',
            round(57.02146,4)  : 'G',
            round(137.05891,4) : 'H',
            round(113.08406,4) : 'I',
            round(128.09496,4) : 'K',
            round(113.08406,4) : 'L',
            round(131.04049,4) : 'M',
            round(114.04293,4) : 'N',
            round(97.05276,4)  : 'P',
            round(128.05858,4) : 'Q',
            round(156.10111,4) : 'R',
            round(87.03203,4)  : 'S',
            round(101.04768,4) : 'T',
            round(99.06841,4)  : 'V',
            round(186.07931,4) : 'W',
            round(163.06333,4) : 'Y'}

with open("rosalind_spec.txt",'r') as r:
    values=r.read().split('\n')
    r.close()
run_time=time.time()
del(values[len(values)-1])
val_table=[float(k) for k in values]
result_table=[]
for i in range(1,len(val_table)):
    result_table.append((round(val_table[i]-val_table[i-1],4)))
res=''

for ele in result_table:
    res += ref_table[ele]
print res
    
print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
