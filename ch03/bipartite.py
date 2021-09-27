# vertices = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'}
adjMat1 = [
    [0, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0],
    [0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 1],
    [0, 0, 1, 0, 1, 0, 1, 0]
]

# vertices = {'A', 'B', 'C', 'D'}
adjMat2 = [
    [0, 1, 1, 1],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [1, 0, 1, 0]
]

class Graph:
    def __init__(self, G):
        self.graph = G
        self.colorArr = [-1] * len(G)
        self.queue = []
        
    def visited(self, vertex):
        if self.colorArr[vertex] == -1:
            return False
        else:
            return True
    
    def isGroup(self, vertex, c):
        if self.colorArr[vertex] == c:
            return True
        else : 
            return False
        
    def isSameGroup(self, v, u):
        if self.colorArr[v] == self.colorArr[u]:
            return True
        else:
            return False
        
    def isAdjacent(self, u, v):
        if self.graph[u][v] == 1 :
            return True
        else: 
            return False
        
    def isSelfLoop(self, u):
        if self.graph[u][u] == 1:
            return True
        else:
            return False
        
    def isBipartite_DFS(self, vtx, color):
        anotherColor = 1 - color
        
        if self.visited(vtx) and not self.isGroup(vtx, color):
            return False
        
        self.colorArr[vtx] = color
        ans = True
        
        for i in range(0, len(self.graph)):
            if self.isAdjacent(vtx, i):
                if not self.visited(i):
                    ans &= self.isBipartite_DFS(i, anotherColor)
                
                elif self.isSameGroup(vtx, i):
                    return False
        
            if not ans:
                return False
        
        return True
    
    def isBipartite_BFS(self, start):
        self.queue.append(start)
        
        while self.queue:
            u = self.queue.pop()
            
            anotherColor = 1 - self.colorArr[u]
            
            if self.isSelfLoop(u):
                return False
            
            for v in range(len(self.graph)):
                if self.isAdjacent(u, v):
                    if not self.visited(v):
                        self.colorArr[v] = anotherColor
                        self.queue.append(v)
                    
                    elif self.isSameGroup(v, u):
                        return False
    
        return True
    
g1 = Graph(adjMat1)
g2 = Graph(adjMat2)

print("g1 is", end = ' ')
print("Bipartite Graph." if g1.isBipartite_DFS(0,1) else "not Bipartite Graph.")

print("g1 is", end = ' ')
print("Bipartite Graph." if g1.isBipartite_BFS(0) else "not Bipartite Graph.")

print("g2 is", end = ' ')
print("Bipartite Graph." if g2.isBipartite_DFS(0,1) else "not Bipartite Graph.")

print("g2 is", end = ' ')
print("Bipartite Graph." if g2.isBipartite_BFS(0) else "not Bipartite Graph.")