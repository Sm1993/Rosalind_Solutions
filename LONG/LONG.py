def Overlapping_subseq(arr, acc=''):
    if len(arr) == 0:
        return acc

    elif len(acc) == 0:
        acc = arr.pop(0)
        return Overlapping_subseq(arr, acc)

    else:

        for i in range(len(arr)):
            a = arr[i]
            l = len(a)

            for p in range(l / 2):
                q = l - p

                if acc.startswith(a[p:]):
                    arr.pop(i)
                    return Overlapping_subseq(arr, a[:p] + acc)

                if acc.endswith(a[:q]):
                    arr.pop(i)
                    return Overlapping_subseq(arr, acc + a[q:])


if __name__ == "__main__":
    s="rosalind_long.txt"

    with open(s,'r') as f:
        temp=f.readlines()
    f.close()
    i=0

    id=[]
    dna_seq=[]



    temp1=''
    count1=1

    for ele in temp:
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
    
    #print id
    #print dna_seq



    with open("output.txt",'w') as r:
        r.write(Overlapping_subseq(dna_seq))
    r.close()
    
