f=raw_input("Enter the string\n")

z=''.join(f.split())


s=z[14:]
l=len(s)



for i in range(len(s)):
    
    
    
    j=4
    while j<13:
       
        if i+j<l+1:
            s1=s[i:(i+j)]
            s2=s1[::-1]
            m=[]
            for k1 in s2:
                if k1=='A':
                    m.append("T")
                elif k1=='T':
                    m.append("A")
                elif k1=='C':
                    m.append("G")
                elif k1=="G":
                    m.append("C")
                
              
            y=''.join(m)
           
            if s1==y:
                
                print i+1,j
        j=j+1
    
        

