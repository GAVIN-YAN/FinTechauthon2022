import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
# nodes=['A','B','C','D','E','F','1']


dataset = pd.read_csv("./topology.csv", header=None)
lenth = dataset.shape[0]
G=nx.Graph()
edges=[]
for i in range(lenth):
    edges.append((dataset.values[i, 0], dataset.values[i, 1]))


r=G.add_edges_from(edges)

# shortest_way=nx.shortest_path(G,"F","D")
# print(shortest_way)
#
# nx.draw(G, with_labels=True,node_color='r', node_size=50,)
# plt.show()

options = {"node_color": "red", "node_size": 300, "linewidths": 0, "width": 0.1, "with_labels": True}
pos = nx.spring_layout(G, random_state=1969)  # Seed for reproducible layout
nx.draw(G, pos, **options)
plt.show()