import sys

s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Downloads\\11CO83_02\\HAMM\\" + s + ".txt"

f=open(s,'r')
temp=f.readlines()
f.close()

s1=temp[0]
s1=s1[0:len(s1)-1]
s2=temp[1]
s2=s2[0:len(s2)-1]

count=0

#print s1 ,len(s1),s2, len(s2)

if len(s1)!=len(s2):
    print "length not equal"
    sys.exit(1)

else:
    for i in range(0,len(s1)):
        if s1[i]!=s2[i]:
            count=count + 1

print count
