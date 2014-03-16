import time
# This program has a time complexity of O((k)),where k is constant,assuming power computation in python takes almost constant time.
n=int(raw_input("Enter val\n"))
run_time=time.time()
print (2**n)%1000000
print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
