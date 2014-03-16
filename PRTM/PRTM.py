s=raw_input()
y=''.join(s.split())
f=open('weight.txt','r')
r=f.readlines()
#print r
sum1=0
k={}


for line in r:
    l=line.split()
    k[l[0]]=l[1]
    
f.close()
for i in y:    
    sum1=sum1+ float (k[i])
print sum1





