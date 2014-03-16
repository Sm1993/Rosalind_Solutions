from math import factorial

def main():
	# load data from file
	f = open('C:\\Users\\Sampat\\Downloads\\rosalind_pmch.txt', 'r')

	s = ''.join(f.read().split('\n')[1:])

	f.close()

	# print s
	# return

	# length of the string (should be even)
	n = len(s) / 2

	# count the GC pairs
	GCcount = s.count('G')
	print GCcount

	# count the AT pairs
	ATcount = s.count('A')
	print ATcount

	print factorial(GCcount) * factorial(ATcount)

	return

if __name__ == '__main__':
	main()
