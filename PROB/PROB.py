	
from math import log10

def probability(dna, probarray):

	probarray = map(float, probarray.split())

	#Calculate probability of DNA happening randomly
	randomchance = []

	for percentage in probarray:
		chancedna = 1.0
		gc = percentage*0.5
		at = (1-(gc*2))*0.5

		for char in dna:
			if char == "A":
				chancedna *= at
			if char == "T":
				chancedna *= at
			if char == "G":
				chancedna *= gc
			if char == "C":
				chancedna *= gc
		randomchance.append(log10(chancedna))
	return " ".join(map(str, randomchance))


print probability("CTTGACTGTAGGACAAGCGCCTCGAAGTAAAATCGTCTACGGCGGTATGTCGTGCACCGTAACCGACTAACTACGATCACTTTGCCCAGTCGATG", "0.100 0.114 0.183 0.255 0.300 0.317 0.393 0.440 0.509 0.546 0.614 0.679 0.727 0.745 0.804 0.877 0.943")
