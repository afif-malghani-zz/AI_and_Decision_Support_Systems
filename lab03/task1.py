# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


# Import networkx to create graphs
# Graphs can be creted from scaratch using classes
# Using networkx helps draw the graphs and makes the process more visual
import networkx as nx

# create list of edges
edges = [(1, 5), (1, 2), (2, 5), (2, 3), (3, 4),
         (4, 5), (4, 6)]

# Initialize graph
graph = nx.Graph()

# add edges from the list
graph.add_edges_from(edges)

# draw graph
# import error on my own env
nx.draw(graph, with_labels=True, font_weight='bold')

# get and print number of nodes
print("number of nodes: ")
print(int(graph.number_of_nodes()))

# get and print number of edges
print("number of edges: ")
print(int(graph.number_of_edges()))

# list of nodes
print("all nodes: ")
print(list(graph.nodes()))

# lsit of edges
print("all edges: ")
print(list(graph.edges()))

# print degree of each node:
print("Degree for all nodes: ")
print(dict(graph.degree()))


# Task c
print("One of the paths From node 6 to node 1: ")
print(nx.bidirectional_dijkstra(graph,6,1))


# Task e
print("All possible paths from node 6 to 1: ")

# iterate and print all paths
for path in nx.all_simple_paths(graph, source=6, target=1):
    print(path)

# Task g
nx.write_adjlist(graph, "Graph01_AL.adjlist")