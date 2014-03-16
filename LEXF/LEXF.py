
'''
        This is the function implementation of cartesian product

def cross(*args):
    ans = [[]]
    for arg in args:
        ans = [x+[y] for x in ans for y in arg]
    return ans

print cross(s1,s2,s3)
'''


import itertools

str_input = raw_input("Enter the string\n")
k=int(raw_input("Enter the k value\n"))

cart_prod=[]
empty_str=''
res=[]
final_res=[]
cart_prod=list(itertools.product(str_input,repeat = k))

for ele in cart_prod:
    for val in ele:
        empty_str=empty_str + val

    res.append(empty_str)
    print empty_str
    empty_str=''

'''
        This remaining part to get all values in proper lexcographic order
        ie AA,AC,AG,AT,CA,CC,CG,CT.......TT  for input T A G C


final_res = sorted(res)

i=len(final_res)-1

while i>=0:
    print final_res[i]
    i -= 1
'''
