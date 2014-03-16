s=raw_input("Enter filename\n")
s="C:\\Users\\Sampat\\Downloads\\11CO83_02\\PROT\\" + s + ".txt"

f=open(s,'r')
temp=f.read()
f.close()

str1=temp[0:len(temp)-1]

i=0
t=[]

k=len(str1)/3
for i in range (0,k+1):
    l=str1[3*(i-1) :3*i]
    t.append(l)

res=''
#print t
for ele in t :
    if ele == 'UUU' or ele =='UUC':
        res=res + 'F'

    elif ele == 'UUA' or ele =='UUG' or ele=='CUU' or ele=='CUC' or ele=='CUA' or ele=='CUG':
        res=res + 'L'

    elif ele == 'UCU' or ele =='UCC' or ele == 'UCA' or ele =='UCG' or ele == 'AGU' or ele == 'AGC':
        res=res+'S'

    elif ele == 'UAU' or ele =='UAC':
        res=res+'Y'
        
    elif ele == 'UGU' or ele =='UGC':
        res=res+'C'

    elif ele == 'UGG':
        res=res+'W'

    elif ele == 'CCU' or ele =='CCC' or ele=='CCA' or ele=='CCG':
        res=res + 'P'

    elif ele == 'CAU' or ele =='CAC':
        res=res + 'H'

    elif ele == 'CAA' or ele =='CAG' :
        res=res + 'Q'


    elif ele == 'CGU' or ele =='CGC' or ele=='CGA' or ele=='CGG' or ele =='AGA' or ele =='AGG':
        res=res + 'R'

    elif ele == 'AUU' or ele =='AUC' or ele=='AUA':
        res=res + 'I'

    elif ele == 'AUG':
        res=res + 'M'

    elif ele == 'ACU' or ele =='ACC' or ele=='ACA' or ele=='ACG':
        res=res + 'T'

    elif ele == 'AAU' or ele =='AAC':
        res=res + 'N'

    elif ele == 'AAA' or ele =='AAG' :
        res=res + 'K'

    elif ele == 'GUU' or ele =='GUC' or ele=='GUA' or ele=='GUG':
        res=res + 'V'


    elif ele == 'GCA' or ele =='GCC' or ele=='GCU' or ele =='GCG':
        res=res + 'A'

    elif ele == 'GAU' or ele =='GAC':
        res=res + 'D'

    elif ele == 'GAA' or ele =='GAG':
        res=res + 'E'

    elif ele == 'GGU' or ele =='GGC' or ele=='GGA' or ele=='GGG' :
        res=res + 'G'


#print res



w=open("C:\\Users\\Sampat\\Downloads\\11CO83_02\\PROT\\Output.txt",'w')
w.write(res)
w.close()


        





