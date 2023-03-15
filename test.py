import networkx as nx
import matplotlib.pyplot as plt
from queue import PriorityQueue

def graph_add_node(Graph: nx.Graph, filename = 'cities.txt'):
    with open(filename, 'r') as file:
        for city in file:
            Graph.add_node(city.rstrip('\n'))

def graph_add_edge(Graph: nx.Graph, filename = 'edges.txt'):
    with open(filename, 'r') as file:
        for row in file:
            edges_data = row.split()

            city1 = edges_data[0]
            city2 = edges_data[1]
            distance = edges_data[2]

            Graph.add_edge(city1, city2, weight=distance)

def get_heuristic(filename = 'heuristics.txt'):
    heuristics = {}
    with open(filename, 'r') as file:
        for row in file:
            node_heuristic = row.split()
            heuristics[node_heuristic[0]] = int(node_heuristic[1])
    return heuristics

G = nx.Graph()

graph_add_node(G, "cities.txt")
graph_add_edge(G, "edges.txt")

node_list = G.nodes()
print("Node:", node_list)

n = G.number_of_nodes()
print("Number of nodes:", n)

m = G.number_of_edges()
print("Number of edges:", m)

for city in G.nodes() :
    neighboring_cities = G.neighbors(city)
    print("The neighbor(s) of {}:".format(city))
    for neighbor in neighboring_cities:
        distance = G.get_edge_data(city, neighbor)['weight']
        print("{} ({})".format(neighbor, distance))
    print()