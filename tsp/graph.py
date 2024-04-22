class Node:
    def __init__(self, val, lat=0, long=0):
        self.val = val
        self.lat = lat
        self.long = long
        self.nbs = []

class Graph:
    def __init__(self):
        self.nodes = []
    
    def getDistance(node1: Node, node2: Node):
        lat_diff = node1.lat - node2.lat
        long_diff = node1.long - node2.long

        return (lat_diff ** 2 + long_diff ** 2) ** 0.5
    
    def addNode(self, node: Node):
        self.nodes.append(node)
    
    def removeNode(self, node: Node):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes[i].nbs)):
                if self.nodes[i].nbs[j][0] == node:
                    self.nodes[i].nbs.pop(j)
        
        self.nodes.remove(node)

    def addEdge(self, source: Node, destination: Node, cost: int):
        found_source = False
        found_destination = False
        for i in range(len(self.nodes)):
            if not found_source and self.nodes[i].val == source.val:
                found_source = self.nodes[i]
            
            if not found_destination and self.nodes[i].val == destination.val:
                found_destination = self.nodes[i]
                
        if not found_source:
            self.nodes.append(source)
            found_source = self.nodes[-1]
        
        if not found_destination:
            self.nodes.append(destination)
            found_destination = self.nodes[-1]
        
        found_source.nbs.append((found_destination, cost))
    

    def removeEdge(self, source: Node, destination: Node, cost: int):
        found = False
        for i in range(len(self.nodes)):
            if self.nodes[i].val == source.val:
                found = self.nodes[i]
                break
        
        if not found:
            return

        for j in range(len(found.nbs)):
            if found.nbs[j] == (destination, cost):
                return found.nbs.pop(j)

    def __str__(self):
        s = "\n"
        for n in self.nodes:
            s += f"{n.val} : ({n.lat}, {n.long})\n"

        return s
