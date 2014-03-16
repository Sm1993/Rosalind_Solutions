import time
# This program has a time complexity of O((k)) where k is length of the larger of the input sets
with open("rosalind_seto.txt",'r') as r:
    raw_set=r.read()
    r.close()
run_time=time.time()
setA=[]
setB=[]

start1=raw_set.find("{")
end1=raw_set.find("}")
n=int(raw_set[0:start1])

setA=[int(k) for k in raw_set[start1+1:end1].split(", ")]

start2=raw_set.find("{",start1+1)
end2=raw_set.find("}",end1+1)

setB=[int(k) for k in raw_set[start2+1:end2].split(", ")]


setA =set(setA)
setB=set(setB)

union=setA|setB
intersect=setA&setB
subAB=setA-setB
subBA=setB-setA


compA=set(range(1,n+1))-setA
compB=set(range(1,n+1))-setB


with open("rosalind_seto_output.txt",'a') as r:
    r.write("{" + str(union)[5:-2] + "}" + "\n")
    r.write("{" + str(intersect)[5:-2] + "}" + "\n")
    r.write("{" + str(subAB)[5:-2] + "}" + "\n")
    r.write("{" + str(subBA)[5:-2] + "}" + "\n")
    r.write("{" + str(compA)[5:-2] + "}" + "\n")
    r.write("{" + str(compB)[5:-2] + "}" + "\n")

r.close()
print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"

