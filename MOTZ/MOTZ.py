import time
# This program has a time complexity of O((k)),where k is constant 
# where k = length of the str


pair = {('A','U'), ('U','A'), ('C','G'), ('G','C')}
memos = {}
fin = open('rosalind_motz.txt', 'r')
fout = open('rosalind_motz_output.txt', 'w')
_INF = 1000000L
 
def count(s):
    if s in memos:
        return memos[s]
    c = 1L
    if len(s) == 2 and (s[0],s[1]) in pair:
        c = 2L
    elif len(s) > 2:
        c = count(s[1:]) + sum([count(s[1:k])*count(s[k+1:]) for k in range(1,len(s)) if (s[0],s[k]) in pair])
    c %= _INF
    memos[s] = c
    return c
     
     
if __name__ == '__main__':
    RNA = fin.read()
    run_time=time.time()
    fout.write(str(count(RNA)))
    fin.close()
    fout.close()
    print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"

