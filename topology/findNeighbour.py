import random

import networkx as nx
import pandas as pd


def kTHNeighbour(lenth, G, node):
    kth_neighbour = {"0-order": [node]}
    for i in range(lenth):
        kth_neighbour[str(i + 1) + "-order"] = []

    for FNs in list(nx.neighbors(G, node)):  # find 1_th neighbors
        kth_neighbour["1-order"].append(FNs)

    for i in range(1, lenth):
        for FNs in kth_neighbour[str(i) + "-order"]:
            for SNs in list(nx.neighbors(G, FNs)):  # find 2_th neighbors
                kth_neighbour[str(i + 1) + "-order"].append(SNs)
        # print("mid-results:", (i+1), kth_neighbour[str(i+1) + "-order"])
        for j in range(1, i + 1):
            kth_neighbour[str(i + 1) + "-order"] = list(
                set(kth_neighbour[str(i + 1) + "-order"]) - set(kth_neighbour[str(j) + "-order"]))
        if i == 2:
            kth_neighbour["2-order"].remove(node)
        # if node in kth_neighbour[str(i+1) + "-order"]:
        #     kth_neighbour[str(i+1) + "-order"].remove(node)
    return kth_neighbour


def iNkthNeighbour(kmatrix, genself):
    # kmatrix["1-order"] = kmatrix["1-order"] + [genself]
    for i in range(1, len(kmatrix)):
        kmatrix[str(i) + "-order"] = kmatrix[str(i) + "-order"] + kmatrix[str(i - 1) + "-order"]
    return kmatrix


def gensID():
    random.seed(401)
    generatorsID = random.sample(range(2, 119), 20)
    generatorsID.sort()
    return generatorsID


def findNeighbour(federated):
    dataset = pd.read_csv("C:/Users/icome/PycharmProjects/pythonProject_try1/topology/topology.csv", header=None)
    lenth = dataset.shape[0]
    G = nx.Graph()
    edges = []
    for i in range(lenth):
        edges.append((dataset.values[i, 0], dataset.values[i, 1]))
    G.add_edges_from(edges)

    generatorsID = gensID()

    # generatorsID = [1]+ generatorsID

    generator_neighbourGenerators = {}
    # a, b = [],[]
    for i in range(len(generatorsID)):
        neighbors = kTHNeighbour(lenth, G, generatorsID[i])
        for k in list(neighbors.keys()):
            if not neighbors[k]:
                del neighbors[k]
        bbb = iNkthNeighbour(neighbors, generatorsID[i])

        # for k in list(neighbors.values()):
        #     a.append(len(k))
        # print(a)

        for j in range(len(neighbors)):
            neighbors[str(j) + "-order"] = list(set(generatorsID) & set(bbb[str(j) + "-order"]))

        # for k in list(neighbors.values()):
        #     b.append(len(k))
        # print(b)
        # print(operator.eq(a, b))

        generator_neighbourGenerators["G" + str(generatorsID[i])] = neighbors

    if federated == 'federated':
        for k in list(generator_neighbourGenerators.keys()):
            temp = []
            res = dict()
            for key, val in generator_neighbourGenerators[k].items():
                if val not in temp:
                    temp.append(val)
                    res[key] = val
            generator_neighbourGenerators[k] = res

    return generator_neighbourGenerators


#
#
generator_neighbourGenerators = findNeighbour('federated')
