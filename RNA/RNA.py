
s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Desktop\\11CO83---Assignment-1\\RNA\\" + s
dic={}
res=""
count=1
f=open(s,'r')
str1=f.read()
if len(s)<=1000:
    alpha=list(str1)
    for ele in alpha:
        if ele == 'T':
            ele='U'
        res=res + ele

print res

