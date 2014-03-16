import re, urllib2





def get_uniprot_IDs(f):
	# read in the database IDs
	f = open(f, 'r')

	uniprot_IDs = []
	for line in f.readlines():
		uniprot_IDs.append(line.split('\n')[0])

	f.close()

	return uniprot_IDs

def get_fasta(ID):
	# generate the ID
	ID_html = 'http://www.uniprot.org/uniprot/' + ID + '.fasta'

	f = urllib2.urlopen(ID_html)

	return ''.join(f.read().split('\n')[1:-1])

def find_motif(s):
	indices = []
	for m in re.finditer('(?=(N[^P][ST][^P]))', s):
		indices.append(m.start() + 1)

	return indices

def main():
	# get the uniprot IDs
	#t=open('/home/sampat/Downloads/vikas123/11CO55_03/MPRT/output.txt','w')
	uniprot_IDs = get_uniprot_IDs('C:\\Users\\Sampat\\Downloads\\Programs\\11CO83_03\\MPRT\\rosalind_mprt.txt')

	# download the fasta string
	for ID in uniprot_IDs:
		indices = find_motif(get_fasta(ID))
		if indices != []:
			print ID
			#t.write(ID + '\n')
			print ' '.join(map(str,indices))
			#t.write(' '.join(map(str,indices) + '\n')
			
	

	# print get_fasta(uniprot_IDs[2])


if __name__ == '__main__':
	main()
