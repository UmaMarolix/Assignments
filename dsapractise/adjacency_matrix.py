
class Graph:
    def __init__(self, numOfNodes):
        self.numOfNodes = numOfNodes
        self.adjMatrix = []
        for i in range(numOfNodes):
            
            row = [0]*numOfNodes
            self.adjMatrix.append(row)

    def addEdge(self, value1,value2):
        self.adjMatrix[value1][value2] = 1
        self.adjMatrix[value2][value1] = 1

    def display(self):
        for row in self.adjMatrix:
            print(row)

g = Graph(5)
g.addEdge(0,1)
g.addEdge(0,2)
g.addEdge(1,2)
g.addEdge(2,0)
g.addEdge(2,3)

g.display()

