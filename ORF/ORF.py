str=raw_input()

str=str.split('\n')
str="".join(str)
str=str[15:len(str)]
s=str
listt=[]
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
i=0
str2=""
k=0
while i<len(str):
    a=str[i:i+3]
   # print i
    if a=="ATG":
           k=i
           while k<(len(str)-2):
              #print "hi",k
               str2=str2+dict[a]
               
               k=k+3
               a=str[k:k+3]
               if a=="TAA" or a=="TAG" or a=="TGA":
                   listt.append(str2)
                   #print str2
                   break
    
    str2=""
               
    i=i+1


s=s[::-1]
b=len(s)
s=list(s)
for i in range(0,b):
    if(s[i]=='A'):
        s[i]='T'
    elif(s[i]=='C'):
        s[i]='G'
    elif(s[i]=='G'):
        s[i]='C'
    elif(s[i]=='T'):
        s[i]='A'
        
s="".join(s)
str=s

i=0
str2=""
k=0
while i<len(str):
    a=str[i:i+3]
   # print i
    if a=="ATG":
           k=i
           while k<(len(str)-2):
               #print "hi",k
               str2=str2+dict[a]
               #a=str[k:k+3]
               k=k+3
               a=str[k:k+3]
               if a=="TAA" or a=="TAG" or a=="TGA":
                   listt.append(str2)
                   #print str2
                   break
    
    str2=""
               
    i=i+1
listt=list(set(listt))

for i in listt:
   print i
