
import collections 


# could be done using counting
def deg_arr(graph):

	n_vertices, n_edges = graph[0] # get #vertices, # edges
	degrees = list(0 for x in range(n_vertices)) # create 0s list
	for ind, edge in enumerate(graph[1:]):
		op_edge =  (edge[1], edge[0])
		if edge not in graph[1:ind] and op_edge not in graph[1:ind]: # check for duplicates
			degrees[edge[0]-1]+=1
			degrees[edge[1]-1]+=1
	return degrees

def read_file(file_name):
	graph_list = []
	graph_list2 = []
	f=open(file_name)

	for line in f.readlines():
		a,b = line.split()
		graph_list.append((int(a), int(b)))
		graph_list2.append(int(a))
		graph_list2.append(int(b))

	# easier counter of list of nodes that appear in the edge list
	ans2 = collections.Counter(graph_list2[2:]).values()
	f = open('rosalind_deg_ans2.txt', 'w')
	for num in ans2:
		f.write(str(num))
		f.write(' ')
	f.close()

	ans1 = deg_arr(graph_list)
	f = open('rosalind_deg_ans.txt', 'w')
	for num in ans1:
		f.write(str(num))
		f.write(' ')
 	f.close()

