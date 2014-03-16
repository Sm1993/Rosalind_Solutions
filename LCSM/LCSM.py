    

def str_sub(seq, x):
    
    list_split = []
    
    for i in range(len(seq)-x+1):
        list_split.append(seq[i:i+x])
      
    return list_split
    
def sub_str_comb(listseq):
    got_match = []
    
   
    for x in range(2,len(listseq[0])):
       
        for val in str_sub(listseq[0],x):
           
            
            if len([False for s in listseq if val not in s]) == 0:
                got_match.append(val)
                
        
        
        if len(got_match[-1]) != x:
            break
    
    
    
    return got_match[-1]

if __name__ == "__main__":
    with open("rosalind_lcsm.txt") as r:
        sequence = r.read()
       
        listseq=[]
        split_fasta = sequence.split(">")
        split_fasta.remove('')
        
        for sp in split_fasta:
           g1=''.join(sp.split())
           listseq.append(g1[14:])
        
        
        
        
       
        res = sub_str_comb(listseq)

    with open("LCSM Answer.txt","w") as a:
        a.write(res)
