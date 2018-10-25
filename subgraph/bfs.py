from collections import deque

import graph_parse
import sys
import numpy as np


def bfs_subgraph(G, source,max_depth,fout_name):
	"""Produce edges in a breadth-first-search starting at source.

	Parameters
	----------
	G : NetworkX graph

	source : node
	Specify starting node for breadth-first search and return edges in
	the component reachable from source.

	Returns
	-------
	edges: generator
	A generator of edges in the breadth-first-search.

	Examples
	--------
	>>> G = nx.Graph()
	>>> G.add_path([0,1,2])
	>>> print(list(nx.bfs_edges(G,0)))
	[(0, 1), (1, 2)]

	Notes
	-----
	Based on http://www.ics.uci.edu/~eppstein/PADS/BFS.py
	by D. Eppstein, July 2004.
	"""

	neighbors = iter(G[source])
	visited = set([source])
	queue = deque([(source, 0, neighbors)])


	while queue:
		parent, height,children = queue[0]

		if int(height)==int(max_depth):
			break
		print(height,max_depth)
		try:
			child = next(children)
			if child not in visited:
				visited.add(child)
				print(parent,visited)
				queue.append((child, height+1,iter(G[child])))

		    
		    
		except StopIteration:
			queue.popleft()


	#print("visted:",visited)
	sub_edges=set([])
	for i in visited:
		for j in visited:
			if j in G[i]:
				sub_edges.add((i,j))

	with open(fout_name,"w") as f:
		for i in visited:
			f.write("node("+str(i)+").\n")
		for i in sub_edges:
			m,n=i
			f.write("link("+str(m)+","+str(n)+").\n")

def go():
	program,fname,numberofsample,depth=sys.argv
	#G={1:[2,4],2:[1,3],3:[1,2],4:[1]}
	G=graph_parse.read_ham_graph(fname)
	nodes=[i for i in G]
	sample=np.random.choice(nodes, int(numberofsample))
	sample=set(sample)
	print(nodes,sample)
	for i in sample:
		fout_name=fname+"0"+i
		bfs_subgraph(G,numberofsample,depth,fout_name)

go()
