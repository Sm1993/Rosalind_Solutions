
s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Desktop\\11CO83---Assignment-1\\DNA\\" + s
dic={}
count=1
f=open(s,'r')
str1=f.read()
if len(s)<=1000:
    alpha=list(str1)
    for ele in alpha:
        if ele not in dic:
            dic[ele]=count
        else:
            dic[ele]=dic[ele]+1


temp= str(dic['A']) + " " + str(dic['C']) + " " + str(dic['G']) + " " + str(dic['T'])
print temp

