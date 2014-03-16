import time
# This program has a time complexity of O((k*k)), assuming factorial alone takes O(k)
# where k = length of the num from m to n

from math import factorial
n=int(raw_input("Enter n\n"))

m=int(raw_input("Enter k\n"))

i=0
sum=0
run_time=time.time()
for i in range(m,n+1):
    comb= factorial(n)/(factorial(i) * factorial(n-i))
    sum=sum+comb


print (sum % 1000000)

print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
