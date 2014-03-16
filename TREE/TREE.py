# Number of edges in a tree is equal to total_nodes-1
with open("test.txt",'r') as r:
    data=r.readlines()

nodes=int(data[0][:-1])                                 

min_edges=0                                             
curr_edge_count=0                                                   
del(data[0])                                                  
                                                    

for ele in data:
    ele=ele[:-1]
    curr_edge_count += 1

#current_edges + req_edges = total_nodes-1

edges_req=nodes-curr_edge_count-1

print edges_req
