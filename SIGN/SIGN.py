import itertools

num=int(raw_input("Enter the Number\n"))
element=[]
ele2=[]
i=0
for i in range (-num,num+1):
	if(i==0):
		pass
	else:
		element.append(i)
count=0
res=""
with open("result.txt",'w') as f:
        ele2=list(itertools.permutations(element,num))

        for ele5 in ele2:
                        if abs(ele5[0])!=abs(ele5[1]):
                                count=count+1
        count=str(count)
        f.write(count + "\n")

        for ele5 in ele2:
                        if abs(ele5[0])!=abs(ele5[1]):
                                for key in ele5:
                                        res =res +  str(key) + " " 
                                f.write(res+"\n")
                                res=""
f.close()
