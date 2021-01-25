'''
Lab 5
'''

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
    
    def Count(self):
        return self.top

    def Print(self):
        print(self.data)



# MyStack = Stack(4)
# MyStack.Push(5)
# MyStack.Push(3)
# MyStack.Push(1)
# MyStack.Push(7)
# print(MyStack.Peek())
# print(MyStack.Peek())
# print(MyStack.Peek())
# print(MyStack.Peek())
# # print(MyStack.Pop())
# # print(MyStack.Pop())
# # print(MyStack.Pop())
# # print(MyStack.Pop())
# # print(MyStack.Pop())
# print(MyStack.Count())
# MyStack.Print()


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
    
    def Print(self):
        print("Number of Elements = ", self.Count())
        
    def StringExp(self, s):
        
        for i in range(len(s)):
            self.Enqueue(s[i])
            
        op_brackets = ['[', '{', '(']
        cl_brackets = [']', '}', ')']
        op = 0
        cl = 0
        
        for i in self.data:
            if i in op_brackets:
                op += 1
                
            elif i in cl_brackets:
                cl += 1
        
        if op == cl:
            return True
        
        else:
            return False
        
MyQueue = Queue(10)

# MyQueue.Enqueue(3)
# MyQueue.Enqueue(7)
# MyQueue.Enqueue(2)
# MyQueue.Enqueue(9)
# MyQueue.Enqueue(2)
# # MyQueue.Enqueue(9)
# MyQueue.Dequeue()
# MyQueue.Dequeue()
# MyQueue.Print()


print(MyQueue.StringExp('[][][][]{}(())'))
MyQueue.Print()









