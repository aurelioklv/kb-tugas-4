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

def get_goal_from_heuristic(heuristic: dict):
    for node, cost in heuristic.items():
        if cost == 0:
            return node

def gbfs(Graph: nx.Graph, start_node, goal_node, heuristics: dict):
    h = heuristics
    path = []
    visited = {}
    for node in Graph.nodes():
        visited[node] = False

    pq = PriorityQueue()
    pq.put((0, start_node))
    visited[start_node] = True

    while not pq.empty():
        u = pq.get()[1]
        path.append(u)

        if u == goal_node:
            break

        for v in Graph.neighbors(u):
            if visited[v] == False:
                visited[v] == True
                c = h[v]
                pq.put((c, v))

    full_path = " -> ".join(path)
    print(full_path)

def main():
    G = nx.Graph()

    # graph_add_node(G, "cities.txt")
    graph_add_edge(G, "edges.txt")
    heuristic = get_heuristic("heuristics.txt")
    goal_node = get_goal_from_heuristic(heuristic)

    print("Goal Node: " + goal_node)

    gbfs(G, "Magetan", goal_node, heuristic)
    gbfs(G, "Ngawi", goal_node, heuristic)
    gbfs(G, "Pamekasan", goal_node, heuristic)
    gbfs(G, "Sampang", goal_node, heuristic)
    # gbfs(G, "Sumenep", goal_node, heuristic) !!!loop

if __name__ == "__main__":
    main()