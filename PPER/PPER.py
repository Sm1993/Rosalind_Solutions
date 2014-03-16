from math import factorial

n=int(raw_input("Enter n\n"))
k=int(raw_input("Enter k\n"))

# This is Like nCr * k! i.e. equal to nPr only

print (factorial(n)/factorial(n-k))%(1000000)
