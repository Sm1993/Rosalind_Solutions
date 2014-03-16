
s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Desktop\\11CO83---Assignment-1\\REVC\\" + s
dic={}
res=""
count=1
f=open(s,'r')
str1=f.read()
if len(s)<=1000:
    str2=str1[::-1]
    alpha=list(str2)
    for ele in alpha:
        if ele == 'A':
            ele='T'
        elif ele == 'T':
            ele='A'
        elif ele == 'G':
            ele='C'
        elif ele == 'C':
            ele='G'
        res=res + ele

print res

