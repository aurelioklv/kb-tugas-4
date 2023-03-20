import networkx as nx
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
                visited[v] = True
                c = h[v]
                pq.put((c, v))

    full_path = " -> ".join(path)
    # print(full_path)
    return full_path

def a_star(Graph: nx.Graph, start_node, goal_node, heuristics: dict):
    open_list = set([start_node])
    closed_list = set([])

    h = heuristics
    g = {}
    g[start_node] = 0
    parents = {}
    parents[start_node] = start_node

    while len(open_list) > 0:
        n = None

        for v in open_list:
            if n == None or g[v] + h[v] < g[n] + h[n]:
                n = v
        
        if n == None:
            # print("Path does not exist")
            return None
        
        if n == goal_node:
            path = []
            while parents[n] != n:
                path.append(n)
                n = parents[n]
            
            path.append(start_node)
            path.reverse()

            full_path = " -> ".join(path)
            # print(full_path)
            return full_path
        
        for m in Graph.neighbors(n):
            if m not in open_list and m not in closed_list:
                open_list.add(m)
                parents[m] = n
                g[m] = g[n] + h[m]
            else:
                if g[m] > g[n] + h[m]:
                    g[m] = g[n] + h[m]
                    parents[m] = n

                    if m in closed_list:
                        closed_list.remove(m)
                        open_list.add(m)
        
        open_list.remove(n)
        closed_list.add(n)

    # print("Path does not exist")
    return None



def main():
    G = nx.Graph()

    # graph_add_node() is optional
    # graph_add_node(G, "cities.txt")
    graph_add_edge(G, "edges.txt")

    heuristic = get_heuristic("heuristics.txt")
    goal_node = get_goal_from_heuristic(heuristic)

    print("Goal Node: " + goal_node + "\n")

    start_nodes = G.nodes()
    for start_node in start_nodes:
        gbfs_path = gbfs(G, start_node, goal_node, heuristic)
        a_star_path = a_star(G, start_node, goal_node, heuristic)
        print("Start Node: {}\nGBFS: {}\nA*  : {}\n".format(start_node, gbfs_path, a_star_path))

if __name__ == "__main__":
    main()