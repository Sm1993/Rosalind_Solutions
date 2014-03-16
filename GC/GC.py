s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Downloads\\11CO83_02\\GC\\" + s + ".txt"

f=open(s,'r')
temp=f.readlines()
f.close()
i=0

id=[]
dna_seq=[]
















temp1=''
count1=1

for ele in temp:
    #ele=ele[0:len(ele)-1]
    if ele[0]=='>':
        if count1==1:
            count1=count1+1
            
        else:
            dna_seq.append(temp1)
            temp1=''
        id.append(ele[0:len(ele)-1])
    else:
        #dna_seq.append(ele)
        temp1=temp1+ele[0:len(ele)-1]
    i=i+1

dna_seq.append(temp1)
print id
#print id
print dna_seq

count=0
res=[]
percentage=0

if len(dna_seq)<=10:
    for dna_entry in dna_seq:
        j=0
        count=0
        var=dna_entry
        print var
        for j in range(0,len(var)):
            if var[j]=='G' or var[j]=='C':
                count=count+1

        print len(var)


        print count
        percentage=count/float(len(var))*100

        res.append(percentage)
print res
per=max(res)
k=res.index(per)

print k
print id[k]
print res[k]



'''w=open("C:\\Users\\Sampat\\Downloads\\11CO83_02\\GC\\Output.txt",'w')
#w.write(id[k])
w.write(res[k])
w.close()
'''
