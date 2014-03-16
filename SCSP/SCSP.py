import time
# This program has a time complexity of O((k*k)), assuming LCS takes O(k^2) and problem takes O(k)
# where k = length of input str

def LCS(X, Y):
    m = len(X)
    n = len(Y)
    # An (m+1) times (n+1) matrix
    C = [[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]: 
                C[i][j] = C[i-1][j-1] + 1
            else:
                C[i][j] = max(C[i][j-1], C[i-1][j])
    return C

def backTrack(C, X, Y, i, j):
    if i == 0 or j == 0:
        return ""
    elif X[i-1] == Y[j-1]:
        return backTrack(C, X, Y, i-1, j-1) + X[i-1]
    else:
        if C[i][j-1] > C[i-1][j]:
            return backTrack(C, X, Y, i, j-1)
        else:
            return backTrack(C, X, Y, i-1, j)


def problem(z,s,t):
    u = ""
    i = 0
    j = 0
    for c in z:
        if i < len(s):
            while s[i] != c:
                u += s[i]
                i += 1
            i += 1
        if j < len(t):
            while t[j] != c:
                u += t[j]
                j += 1
            j += 1
        u += c
    if i < len(s):
        u += s[i:]
    if j < len(t):
        u += t[j:]
    return u



with open('rosalind_scsp.txt','r') as r:
    X,Y=r.readlines()
    r.close()
X = X[:-1]
Y = Y[:-1]
m = len(X)
n = len(Y)
C = LCS(X, Y)
with open('rosalind_scsp_output.txt','w') as w:
    run_time=time.time()
    w.write(problem(backTrack(C, X, Y, m, n),X,Y))
print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"
