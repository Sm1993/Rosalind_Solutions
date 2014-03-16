import time
from itertools import product,compress
# This program has a time complexity of O((n^2)), assuming that each of the index finding operations takes constant time using suitable datastructure
# where n = length of thepermutaion pair, here 10

def bpfind(x,y):
    return abs(x-y)!=1
def reversal(perm,start,stop):
    return perm[:start]+perm[start:stop+1][::-1]+perm[stop+1:]
def bpc(permutation): #counting breakpoints using the concept of shift mapping
    permutation = [0] + list(permutation) + [len(permutation)+1] 
    return sum(map(bpfind, permutation[1:], permutation[:-1]))
def bpi(permutation): # counting number of breakpoints
    permutation = [0] + list(permutation) + [len(permutation)+1]
    return compress(range(len(permutation)-1), map(bpfind, permutation[1:], permutation[:-1]))
    

def bfs_min(perm1, perm2):
    linear = {value: i + 1 for i, value in enumerate(perm2)} # 
    indices = [linear[value] for value in perm1]
    indices = tuple(indices)
    current_perms = {indices:[]}
    min_breaks = bpc(indices)
    dist = 0

    # Run the greedy BFS breakpoint reduction sorting.
    while True:
        new_perms = {}
        dist+=1
        # Iterate over all combinations of breakpoint indices for all  current minimal permutations.
        for perm in current_perms.keys():
            for ri in product(bpi(perm), repeat=2): # start adn end 
                # Store some temporary variables for the given iteration.
                start = ri[0]
                stop = ri[1]-1
                temp_perm = tuple(reversal(perm, start,stop))
                temp_breaks = bpc(temp_perm)
                temp_transformation = current_perms[perm] + [str(start+1) + ' ' + str(stop)]
                # Done we have no breakpoints.
                if temp_breaks == 0:
                    return temp_transformation # the final set of sort orders

                # Create a new dictionary and update the minimum number of breakpoints if we've found a reduction.
                elif temp_breaks < min_breaks:
                    min_breaks = temp_breaks
                    new_perms = {temp_perm:temp_transformation}

                # Add to the dictionary if the current breakpoints match the minimum number.
                elif temp_breaks == min_breaks:
                    new_perms[temp_perm]=temp_transformation

        current_perms = new_perms
k=0
source=[] # set of all source permutations
destination=[] # set of all destination permutations

with open("rosalind_sort.txt","r") as ip:
    src=ip.readline().strip().split()
    destn=ip.readline().strip().split()
ip.close()
with open("rosalind_sort_output.txt","w") as op:
    tim=time.time()
    ans=bfs_min(src,destn)
    ans=[str(len(ans))]+ans
    for i in range(1,len(ans)):
        m=ans[i].split()
        m[0]=int(m[0])
        m[1]=int(m[1])+1
        ans[i]=' '.join(map(str,m))
    op.write('\n'.join(ans))
    print '\n'.join(ans),"\n\nThe time of execution of the above program is",time.time()-tim,"seconds"
op.close()
