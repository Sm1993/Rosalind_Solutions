s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Downloads\\11CO83_02\\SUBS\\" + s + ".txt"

f=open(s,'r')
temp=f.readlines()
f.close()

s=temp[0]
s=s[0:len(s)-1]
#print s

t=temp[1]
t=t[0:len(t)-1]

#print t

res=[]
var=0
num=-1
m=''
s_temp=s

#print s_temp
while var!=-1:
    
    var=s_temp.find(t,num+1)
    if var == -1:
        break;
    else:
        
        res.append(var+1)
        num=var
        #print num
        #s_temp=s_temp[var+1::]
    #print s_temp

#print res
for ele in res:
    m=m+str(ele)+" "

print m
