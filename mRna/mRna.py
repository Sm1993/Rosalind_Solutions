dict = {'A':4,'R':6,'N':2,'D':2,'C':2,'Q':2,'E':2,'G':4,'H':2,'I':3,'L':6,'K':2,'M':1,'F':2,'P':4,'S':6,'T':4,'W':1,'Y':2,'V':4,'Stop':3}
s= raw_input("Enter the string\n")
y=''.join(s.split())

pr=1
for i in y:
    pr=pr*dict[i]


pr=pr*3
pr=pr%1000000
print pr
    
