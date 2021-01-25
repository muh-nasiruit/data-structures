

class Stack:
    def __init__(self, size):
        self.size = size
        self.data = [0 for i in range(size)]
        self.top = 0
        
    def IsEmpty(self):
        # to check for Underflow
        
        if self.top == 0:
            return True
        else:
            return False
    
    def IsFull(self):
        #to check for Overflow
        
        if self.top == self.size:
            return True
        else:
            return False
        
    def Push(self, e):
        if self.IsFull() == True:
            return "Overflow detected."
        
        else:
            self.data[self.top] = e
            self.top += 1
            
    def Pop(self):
        if self.IsEmpty() == True:
            return "Underflow detected."
        
        else:
            x = self.data[self.top -1]
            self.top -= 1
            return x

    def Peek(self):
        x = self.data[self.top-1]
        return x

    # def Print(self):
    #     for i in range(self.top):
    #         print(self.data[i], end = ' ')
        
    #     print()
    
# s = Stack(5)
# s.Push(1)
# s.Push(2)
# s.Push(3)
# s.Push(4)
# s.Push(5)
# s.Print()
# print("--After Pop--")
# print(s.Count())
# s.Pop()
# s.Pop()
#s.Print()
# s.Pop()
# s.Print()
#print(s.Count())    
    
    
    
    
    
    
    
    
    
    
    
    