
class Queue:
    def __init__(self, size):
        self.data = [0 for i in range(size)]        
        self.size = size
        self.r = 0
        self.f = 0
        self.count = 0
        
    def IsEmpty(self):
        if self.r == 0:
            return True
        else:
            return False
    def IsFull(self):
        if self.r == self.size:
            return True
        else:
            return False
        
    def Enqueue(self, item):
        if self.IsFull() == True:
            return "Overflow detected."
        
        else:
            self.data[self.r] = item
            self.r = (self.r+1) % self.size
            self.count += 1

    def Dequeue(self):
        if self.IsEmpty() == True:
            return "Underflow detected."
        
        else:
            x = self.data[self.f]
            self.f = (self.f+1) % self.size
            self.count -= 1
            return x
    
    def Count(self):
        return self.count

#     def Print(self):
#         for i in range(self.f, self.r):
#             print(self.data[i], end= " ")
        
#         print()
    
# q = Queue(5)
# q.Enqueue(1)
# q.Enqueue(2)
# q.Enqueue(3)
# q.Print()
# q.Dequeue()
# print("--After Dequeue--")
# q.Print()


