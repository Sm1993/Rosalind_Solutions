probs = [2., 2., 2., 1.5, 1, 0]

with open('C:\\Users\\Sampat\\Downloads\\11CO83_02\\IEV\\rosalind_iev.txt', 'r') as f:
    couples = map(int, f.readline().split())

print sum([a*b for a, b in zip(probs, couples)])
