class Node:
    def __init__(self, val, x=0, y=0):
        self.val = val
        self.x = x
        self.y = y
        self.nbs = []
    
    # def __eq__(self, value: object) -> bool:
    #     return self.val

class Graph:
    def __init__(self):
        self.nodes = []
    
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
            nodes = "[ "
            for nb in n.nbs:
                nodes += f"({nb[0].val}, {nb[1]}) "
            nodes += "]"
            s += f"{n.val} : {nodes}\n"

        return s