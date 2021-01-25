import mystack, myqueue

class Graph:
    def __init__(self, vertex):
        self.vertex = vertex
        self.adj = [[0 for i in range(vertex)] for j in range(vertex)]
        self.r = 0
        self.neigh = []
        self.visited = []
        
    def IsEmpty(self):
        if self.r == 0 :
            return True
        return False
    
    def Push(self, item):
        self.data[self.r] = item
        self.r += 1
    
    def Pop(self):
        self.r -= 1
        x = self.data[self.r]
        return x
    
    def AddEdge(self, src, dest):
        self.adj[src][dest] = 1
        self.adj[dest][src] = 1
    
    def GetNeighbors(self,v):
        for i in range(len(self.adj[v])):
            if self.adj[v][i] == 1:
                self.neigh.append(i)
        
        return self.neigh

    def PrintMatrix(self):
        for i in range(self.vertex):
            for j in range(self.vertex):
                print(self.adj[i][j], end=' ')
            print()

    def DFS(self, source):
        
        s = mystack.Stack(self.vertex)
        s.Push(source)
        self.visited.append(source)
        
        while not s.IsEmpty():
            x = s.Pop()
            print('Visited {}'.format(x))
            neighbors = self.GetNeighbors(x)
            
            for i in neighbors:
                if i not in self.visited:
                    s.Push(i)
                    self.visited.append(i)
                    
    def BFS(self, source):
        
        q = myqueue.Queue(self.vertex)
        q.Enqueue(source)
        self.visited.append(source)
        
        while not q.IsEmpty():
            x = q.Dequeue()
            print('Visited {}'.format(x))
            neighbors = self.GetNeighbors(x)
            
            for i in neighbors:
                if i not in self.visited:
                    q.Enqueue(i)
                    self.visited.append(i)
            


#DFS implemented with stack.
#BFS implement with queue
# g = Graph(5)
# g.AddEdge(0,1)
# g.AddEdge(0,2)
# g.AddEdge(1,3)
# g.AddEdge(3,4)
# g.AddEdge(1, 4)

# g.GetNeighbors(0)
# g.BFS(0)
# g.DFS(0)
# g.PrintMatrix()




