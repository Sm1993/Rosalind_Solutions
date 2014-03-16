dna_seq=[]
id=[]

def extract_fasta(List):
    temp1=''
    count1=1
    i=0
    for ele in List:
        #ele=ele[0:len(ele)-1]
        if ele[0]=='>':
            if count1==1:
                count1=count1+1
            
            else:
                dna_seq.append(temp1)
                temp1=''
            id.append(ele[0:len(ele)-1])
        else:
            #dna_seq.append(ele)
            temp1=temp1+ele[0:len(ele)-1]
        i=i+1

    dna_seq.append(temp1)


def get_protein(str1):
    i=0
    dict={
    "TTT":"F",      "CTT": "L" ,     "ATT": "I",      "GTT": "V",
    "TTC" :"F" ,     "CTC": "L" ,     "ATC": "I" ,     "GTC" :"V",
    "TTA" :"L" ,     "CTA": "L" ,     "ATA": "I" ,     "GTA" :"V",  
    "TTG" :"L",       "CTG" :"L",      "ATG": "M" ,     "GTG" :"V",
    "TCT" :"S",      "CCT" :"P",      "ACT": "T",      "GCT": "A",
    "TCC" :"S",      "CCC" :"P",      "ACC": "T",      "GCC": "A",
    "TCA" :"S",      "CCA" :"P",      "ACA": "T",      "GCA":"A",
    "TCG" :"S",      "CCG" :"P",      "ACG": "T" ,     "GCG":"A",
    "TAT" :"Y",      "CAT" :"H" ,     "AAT": "N",      "GAT":"D",
    "TAC" :"Y",      "CAC" :"H",      "AAC": "N",      "GAC":"D",
    "TAA" :"Stop" ,  "CAA" :"Q",      "AAA": "K",      "GAA":"E",
    "TAG" :"Stop",   "CAG" :"Q",      "AAG": "K",      "GAG":"E",
    "TGT" :"C" ,     "CGT" :"R",      "AGT": "S" ,     "GGT":"G",
    "TGC" :"C",      "CGC" :"R"  ,    "AGC": "S",      "GGC":"G",
    "TGA" :"Stop",   "CGA" :"R",      "AGA": "R"  ,    "GGA" :"G",
    "TGG" :"W"   ,   "CGG" :"R",      "AGG": "R"   ,   "GGG": "G"}
    t=[]
    print str1
    k=len(str1)/3
    print k
    for i in range (0,k+1):
        l=str1[3*(i-1) :3*i]
        t.append(l)

    res=''
    print t
    
    for i in range(1,len(t)):
        if(dict[t[i]] == "Stop"):
            pass
        else:
            res = res + dict[t[i]]
    return res



with open("rosalind_splc.txt") as r:
        sequence = r.readlines()
r.close()
extract_fasta(sequence)
root_dna=dna_seq[0]
j=0
print root_dna
for j in range(1,len(dna_seq)):
    print dna_seq[j]
    intron_index = root_dna.find(dna_seq[j])

    root_dna = root_dna[0:intron_index] + root_dna[intron_index+len(dna_seq[j]):len(root_dna)]
    print root_dna

result = get_protein(root_dna)

print result
    
