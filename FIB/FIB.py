n=raw_input("Enter n\n")
k=raw_input("Enter k\n")

n=int(n)
k=int(k)

a=[]
a.append(1)
a.append(1)
for i in range(2,n+1):
    temp=a[i-1]+k*a[i-2]
    a.append(temp)

print a[n-1]
