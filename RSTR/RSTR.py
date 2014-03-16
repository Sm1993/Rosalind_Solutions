import time
# This program has a time complexity of O((k))
# where k = length of input

import math

def main():

	# import the string from file
	f = open('c:\\Python27\\rosalind_rstr.txt', 'r')

	lines = f.read().split('\n')[:2]
	f.close()
	run_time=time.time()

	N = int(lines[0].split(' ')[0])
	x = float(lines[0].split(' ')[1])
	s = lines[1]

	# get the GC-content of the string s
	GC_count = 0
	for i in s:
		if i == 'G' or i == 'C':
			GC_count += 1

	AC_count = len(s) - GC_count

	P = 1-pow(1-pow(x/2, GC_count)*pow((1-x)/2,AC_count), N)

	print '%.3f' % P
	print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"


	return


if __name__ == '__main__':
	main()


