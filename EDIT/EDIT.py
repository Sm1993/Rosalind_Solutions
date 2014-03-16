import time
# This program has a time complexity of O((k*k))


raw_str1=raw_input('Enter String 1\n')
raw_str2=raw_input('Enter String 2\n')


def min_val(a,b,c):
    if a<=b and a<=c:
        return a
    elif b<=c:
        return b
    else:
        return c



def edit(raw_str1,raw_str2):
    edit_matrix=[]
    edit_matrix_val=[]
    edit_matrix=[[k for k in range(0,len(raw_str1)+1)]]

    for i in range(0,(len(raw_str2))):
        edit_matrix.append(edit_matrix_val)
        edit_matrix_val=[]
    for i in range(1,len(raw_str2)+1):
        if edit_matrix[i]==[]:
            edit_matrix[i].append(i)
        for j in range(1,len(raw_str1)+1):
            if raw_str1[j-1] == raw_str2[i-1]:
                edit_matrix[i].append(min_val(edit_matrix[i][j-1]+1,edit_matrix[i-1][j]+1,edit_matrix[i-1][j-1]))
            else:
                edit_matrix[i].append(min_val(edit_matrix[i][j-1]+1,edit_matrix[i-1][j]+1,edit_matrix[i-1][j-1]+1))

    #print len(edit_matrix),len(edit_matrix[0]),len(raw_str2),
    return edit_matrix[len(edit_matrix)-1][len(edit_matrix[0])-1]

run_time=time.time()
distance=edit(raw_str1,raw_str2)
print distance

print "\n\nThe time of execution of the above program is",time.time()-run_time,"seconds"

            
