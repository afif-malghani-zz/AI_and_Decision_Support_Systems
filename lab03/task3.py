# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                        Coded by:                                        #
#                                Muhammad Afif Ul Hasnain                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

# import numpy and networkx
import numpy as np
import networkx as nx

# define a function to extract edges
def Extract_edges(img):
  # individual edge
  edge = ()

  # list of edges
  edges = []

  # rows in image
  row = img.shape[0]

  # columns in image
  col = img.shape[1]
  for i in range(0, row):
    for j in range(0, col):
      if i < row-1 and j < col-1:

        # define edge
        edge = (img[i, j], img[i, j+1])

        # append to lsit of edges
        edges.append(edge)

        # define edge
        edge = (img[i, j], img[i+1, j])

        # append to list of edges
        edges.append(edge)

      # pixels at the border from left
      elif i == row-1 and j != col-1:
        edge = (img[i, j], img[i, j+1])
        edges.append(edge)

      # pixels at the bottom border
      elif i != row-1 and j == col-1:
        edge = (img[i, j], img[i+1, j])
        edges.append(edge)

  # return list of edges
  return edges

# dummy image
img = np.array([[150, 2, 5], [80, 145, 45], [74, 102, 165]])

# get edges for graph
edges = Extract_edges(img)

# create graph
G=nx.Graph()

# add egdes to graph
G.add_edges_from(edges)

# draw graph
nx.draw(G, with_labels=True, font_weight='bold')

print("\nAll possible paths from node 150 to 165: ")

# get and print all possible paths
for path in nx.all_simple_paths(G, source=150, target=165):
    print(path)

# get adjacency list
nx.write_adjlist(G, "AL.adjlist")