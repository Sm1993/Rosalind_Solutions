import time
# This program has a time complexity of O((k)), assuming hashings are done in constant time.

import sys
from collections import Counter
from numpy import log, exp


if __name__ == '__main__':
    with open('rosalind_eval.txt','r') as r:
        N,s,cg=r.readlines()
        r.close()
    run_time=time.time()
    N = int(N)
    s = s[:-1]
    cg=cg[:-1]
    cgs = [float(x) for x in cg.split()]#lines[2].split()]
    c = Counter(s)
    with open('rosalind_eval_output.txt','w') as w: 
        for cg in cgs:
            log_p = (c['A'] + c['T']) * log((1 - cg)/2) + (c['C'] + c['G']) * log(cg/2)
            w.write(str(round(exp(log_p) * (N-1),3)) + ' ')
    print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
