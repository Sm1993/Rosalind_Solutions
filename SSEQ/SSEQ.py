input_str = raw_input("Enter Dna String\n")

sub_seq = raw_input ("Enter the subseq\n")
end_res=""
i=0
for index in sub_seq:
	#print index
	start_index = input_str.find(index,i)

	#print start_index 
	if start_index==-1:
		print "String Not found"
	else:
		end_res += str(start_index+1) + " "
		i=start_index+1
print end_res
