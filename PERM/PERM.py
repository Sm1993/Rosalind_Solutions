from math import factorial
n=int(raw_input())
print factorial(n)
listt=[]
for i in range(1,n+1):
    listt.append(str(i))
#print listt

def permute(LIST):
    length=len(LIST)
    if length <= 1:
        yield LIST
    else:
        for k in range(0,length):
             for end in permute( LIST[:k] + LIST[k+1:] ):
                 yield [ LIST[k] ] + end

#print permute(["3","3","4"])
strr=""
for x in permute(listt):
    for i in x:
        strr=strr+str(i)
        strr=strr+" "
    print strr
    strr=""
