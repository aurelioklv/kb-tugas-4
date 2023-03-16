#Analisis Masalah

#1. Bikin undirected weighted graph
#2. Setiap verteks ada nilai heuristic
#3. Algo A*

##Kode

import sys
from typing_extensions import Self
from copy import deepcopy #Help asign list value to variables without passing only the reference

#CLASS : MinHeap
    #https://www.geeksforgeeks.org/min-heap-in-python/
    #MODIFICATION : Stores pairs of a number and a string (g/h value + node name)
class MinHeap:
  
    def __init__(self, max):
        self.size = 0
        self.maxsize = int(max)
        self.Heap = []
        for i in range(self.maxsize+1):
            self.Heap.append([int(sys.maxsize), "TEST"])
        self.Heap[0][0] = -1 * sys.maxsize
        self.FRONT = 1
  
    # Function to return the position of
    # parent for the node currently
    # at pos
    def parent(self, pos):
        return pos//2
  
    # Function to return the position of
    # the left child for the node currently
    # at pos
    def leftChild(self, pos):
        return 2 * pos
  
    # Function to return the position of
    # the right child for the node currently
    # at pos
    def rightChild(self, pos):
        return (2 * pos) + 1
  
    # Function that returns true if the passed
    # node is a leaf node
    def isLeaf(self, pos):
        return pos*2 > self.size
  
    # Function to swap two nodes of the heap
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]
  
    # Function to heapify the node at pos
    def minHeapify(self, pos):
  
        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.Heap[pos][0] > self.Heap[self.leftChild(pos)][0] or 
               self.Heap[pos][0] > self.Heap[self.rightChild(pos)][0]):
  
                # Swap with the left child and heapify
                # the left child
                if self.Heap[self.leftChild(pos)][0] < self.Heap[self.rightChild(pos)][0]:
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))
  
                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))
  
    # Function to insert a node into the heap
    def insert(self, value, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size][0] = int(value)
        self.Heap[self.size][1] = element

        current = self.size
  
        while self.Heap[current][0] < self.Heap[self.parent(current)][0]:
            self.swap(current, self.parent(current))
            current = self.parent(current)
  
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+ 
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))

    # Function to get number value
    def getFirstValue(self, secondValue):
        for pair in self.Heap:
            if pair[1] == secondValue:
                return int(pair[0])
  
    # Function to change number value
    def modFirstValue(self, secondValue, newValue):
        for pair in self.Heap:
            if pair[1] == secondValue:
                pair[0] = int(newValue)

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):
  
        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)
  
    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
  
        popped = self.Heap[self.FRONT]
        self.Heap[self.FRONT] = deepcopy(self.Heap[self.size])
        self.size-= 1
        self.minHeapify(self.FRONT)
        return deepcopy(popped)
  
###INIT : DATA STRUCTURES
#1. graph = Stores graph in adjacency list (key : [val1, val2] || nodeA : [cost, nodeB])
#2. hValues : Stores heuristic values (key : val || node : hValue)
#3. gValues : Stores g value of nodes
#4. fValues : Stores f value of nodes
#5. cameFrom : Untuk node "A", mencatat node yang sebelumnya didatangi sebelum ke "A"
graph = dict()
hValues = dict()
gValues = dict()
fValues = dict()
cameFrom = dict()

def addEdge(node1, node2, cost):
    if node1 not in graph:
        graph[node1] = []
    if node2 not in graph:
        graph[node2] = []
    temp = [int(cost), node2]
    graph[node1].append(temp)
    temp = [int(cost), node1]
    graph[node2].append(temp)

#FUNCTION getCost
#Node1 : origin node
#Node2 : destination node

#Desc :
##Returns cost going from node1 to node2
def getCost(node1, node2):
    if node1 in graph:
        for node in graph[node1]:
            if node[1] == node2:
                return int(node[0])

def addHeuristic(node, hVal):
    if node not in hValues:
        hValues[node] = []
        #gValues[node] = []
        fValues[node] = []
        cameFrom[node] = []

    hValues[node].append(int(hVal))
    #Step 0 : Starts with value "infinity"
    gValues.update({node : int(sys.maxsize)})
    fValues[node].append(int(sys.maxsize))
    cameFrom[node].append("NULL")


#Fungsi A*
def a_Star(start, goal, max):
###Variabel Penting
    #1. Closed set : Node yang sudah diexpand/didatangi dan nilai Fnya
    #2. Open set : Queue yang berisi node yang siap diperiksa dan nilai Fnya
        #NOTE : Untuk Closed/Open List menggunakan priority queue/min heap, supaya prioritas memeriksa node yang Fnya kecil
    #3. 2 Data Structure untuk menyimpan nilai G dan F setiap node (berubah selama proses)
    #4. cameFrom : Untuk node "A", mencatat node yang sebelumnya didatangi sebelum ke "A"
    #closedSet = MinHeap()
    openSet = MinHeap(max)

###Steps
        #0. Inisialisasi :
            #Nilai G dan F setiap node = Infinitely large
            #Open list : Diisi node awal dengan nilai F = H node awal dan nilai G = 0
    #print(hValues[start])
    fValues[start] = hValues[start]
    gValues[start] = 0
    openSet.insert(fValues[start][0], start)
    #WHILE (OPEN LIST TIDAK KOSONG)
    while (openSet.size > 0):
        print("Min Heap STATUS:")
        openSet.Print()
        print("--------------------------")
        #1. Ambil node yang ingin dicek dari open list (save)
        curr = openSet.remove()
        currF = deepcopy(curr[0])
        currName = deepcopy(curr[1])
        print("Visiting node : ", currName)

        if currName == goal:
            return 1 #Goal is found
   #3.  FOR (SETIAP CHILD/NEIGHBOUR DARI NODE TSB)
        for neighbour in graph[currName]:
            #print("++++++++++++++++++++++++++++++++++++++")
            tempGValue = 0
            tempGValue = int(deepcopy(gValues[currName])) + int(deepcopy(neighbour[0]))

            if tempGValue < gValues[neighbour[1]]:            
                gValues[neighbour[1]] = tempGValue
                fValues[neighbour[1]] = tempGValue + hValues[neighbour[1]][0]
                cameFrom[neighbour[1]] = currName
                if neighbour[1] not in openSet.Heap:
                    openSet.insert(deepcopy(fValues[neighbour[1]]), deepcopy(neighbour[1]))
                    #openSet.Print()
                    #print("-----------------------")

def printResult(goal):
    current = goal
    parent = cameFrom[current]
    total = 0
    print(goal)
    while parent != ['NULL']:
        total += getCost(current, parent)
        print("^\n|", "cost :", getCost(current, parent))
        print(parent)
        current = parent
        parent = cameFrom[current]
    print("TOTAL COST : ", total)
def main():
#BUILDS GRAPH
    with open("graph.txt") as graphInput:
        for idx, line in enumerate(graphInput):
            if idx < 1:
                nodes, edges = line.split()
                #print(idx, line)
            elif idx <= int(edges) and idx > 0:
                node1, node2, cost = line.split()
                addEdge(node1, node2, cost)
                #print(idx, line)
            elif idx > int(edges):
                node, hVal = line.split()
                addHeuristic(node, hVal)
                #print(node, " + ",  hVal)
#DRIVER CODE
    origin = "Magetan"
    destination = "Surabaya"

    if a_Star(origin, destination, int(nodes)):
        printResult(destination)

#TESTING CODE
    # print("HEURISTICS/n")
    # for key, val in hValues.items():
    #     print(f"{key} = {val}")
    # print("INIT F VALUE/n")
    # for key, val in fValues.items():
    #     print(f"{key} = {val}")


    # for key, val in graph.items(): #Usual way to access key value pairs
    #     for x in val:
    #         print(f"{key} = ", x[0], "+", x[1])

#Lets interpreter know that it's running the main program
if __name__=="__main__": 
    main()