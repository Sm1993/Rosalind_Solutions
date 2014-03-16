from math import factorial

def binomial(n, m):  # This is nCm
        return factorial(n) / (factorial(m) * factorial(n - m))

def main():
        # open the file
        f = open('rosalind_lia.txt', 'r')

        [k, n] = map(int, f.readline().split('\n')[0].split(' '))

        # close the file
        f.close()

        K = pow(2, k)

        s = 0
        for i in range(n, K+1):
                s += binomial(K,i) * pow(1./4, i) * pow(3./4, K - i)

        print s

        return

if __name__ == '__main__':
        main()
