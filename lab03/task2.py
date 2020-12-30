# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import networkx
import networkx as nx

# create list of edges
edges = [('A', 'B'), ('B', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'E'),
         ('D', 'E'), ('E', 'F'), ('G', 'D')]

# create graph
graph=nx.DiGraph()

# Add edges from list
graph.add_edges_from(edges)

# Draw graph
nx.draw(graph, with_labels=True, font_weight='bold')

# get and print number of nodes
print("number of nodes: " )
print(int(graph.number_of_nodes()))

# get nad print number of edges
print("number of edges: ")
print(int(graph.number_of_edges()))

# Print list of nodes
print("List of all nodes: ")
print(list(graph.nodes()))

# Print list of all edges
print("List of all edges: ")
print(list(graph.edges()))

# Indegree of all nodes
print("Indegree for all nodes: ")
print(dict(graph.in_degree()))

# Outdegree for all nodes
print("Outdegree for all nodes: ")
print(dict(graph.out_degree()))

# Get and prinmt a path from source to destination
print("One of the paths from node A to node F: ")
print(nx.bidirectional_dijkstra(graph,'A','F'))

print("All possible paths from node A to F: ")

# get and print all paths from source to destination
for path in nx.all_simple_paths(graph, source='A', target='F'):
    print(path)

# get and print adjacency list for teh graph
nx.write_adjlist(graph, "Graph02_AL.adjlist")