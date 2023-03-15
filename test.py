import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

cities = ["Bangkalan", "Sampang", "Pamekasan", "Sumenep", "Surabaya", "Sidoarjo", "Probolinggo", "Situbondo", "Gresik", "Lamongan", "Jombang", "Nganjuk", "Bojonegoro", "Madiun", "Ngawi", "Ponorogo", "Magetan"]
for city in cities:
    G.add_node(city)

G.add_edge("Pamekasan", "Sumenep", weight=54)
G.add_edge("Pamekasan", "Sampang", weight=31)
G.add_edge("Bangkalan", "Sampang", weight=52)
G.add_edge("Surabaya", "Bangkalan", weight=44)
G.add_edge("Surabaya", "Sidoarjo", weight=25)
G.add_edge("Surabaya", "Gresik", weight=12)
G.add_edge("Surabaya", "Jombang", weight=72)
G.add_edge("Sidoarjo", "Probolinggo", weight=78)    
G.add_edge("Probolinggo", "Situbondo", weight=99)
G.add_edge("Gresik", "Lamongan", weight=14)
G.add_edge("Lamongan", "Bojonegoro", weight=42)
G.add_edge("Jombang", "Bojonegoro", weight=70)
G.add_edge("Nganjuk", "Jombang", weight=40)
G.add_edge("Nganjuk", "Bojonegoro", weight=33)
G.add_edge("Ngawi", "Bojonegoro", weight=44)
G.add_edge("Ngawi", "Magetan", weight=32)
G.add_edge("Madiun", "Ngawi", weight=30)
G.add_edge("Madiun", "Nganjuk", weight=48)
G.add_edge("Madiun", "Magetan", weight=22)
G.add_edge("Madiun", "Ponorogo", weight=29)
G.add_edge("Magetan", "Ponorogo", weight=34)

node_list = G.nodes()
print("List:", node_list)

n = G.number_of_nodes()
print("Number of nodes:", n)

m = G.number_of_edges()
print("Number of edges:", m)

for city in cities:
    neighboring_cities = G.neighbors(city)
    print("The neighbor(s) of {}:".format(city))
    for neighbor in neighboring_cities:
        distance = G.get_edge_data(city, neighbor)['weight']
        print("{} ({})".format(neighbor, distance))
    print()