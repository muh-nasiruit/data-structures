




# Question 1



def BrainSearch(arr, start, e):
    

    if start >= len(arr):
        return -1
    elif arr[start] == e:
        return start
    return BrainSearch(arr, start + 1, e)

# print(BrainSearch([11,32,13,41,51], 0, 13))



# Question 2




def RotateRight(d, arr):

    arr = [arr[(i + d) % len(arr)] 
           for i, x in enumerate(arr)]
    
    return arr

# print(RotateRight(3 ,[1,2,3,4,5]))




# Question 3
    
class DoubleStack():

    def _init_(self ,size):
        self.size = size
        self.data = []
        self.current = 0

    def IsEmpty(self):
        if self.size == 0:
            return True
        else:
            return False

    def Push(self ,s):
        self.data.append(s)
        self.current =1
        if len(self.data) > self.size:
            raise Exception('Size overflow')
        return self.data

    def Pop(self):
        x = self.data[self.current -1]
        self.current -= 1
        if self.current == -1:
            raise Exception('Size underflow')
        return x

    def Peek(self):
        return self.data[self.current - 1]

    def Count(self):
        l = len(list(range(self.current))) + 1
        return l



# ds = DoubleStack(5)
# ds.IsEmpty()
# ds.Push(5)
# ds.Push(4)
# ds.Push(3)
# ds.Push(6)
# ds.Push(7)






#Question 4
class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class Deque:
    def __init__(self, size):
        self.head = None
        self.last = None
        self.data = []
        self.size = size

 
    def InsertRear(self, value):
        if self.last == None:
            self.head = Node(value)
            self.last = self.head
        else:
            self.last.next = Node(value)
            self.last = self.last.next

    def GetRear(self):
        self.Print()
        return self.data[-1]
    
    def Print(self):
        x = self.head
        while x != None:
            self.data.append(x.value)
            x = x.next   
        
        return self.data
    
# obj = Deque(5)
# obj.InsertRear(5)
# obj.InsertRear(3)
# obj.InsertRear(2)
# obj.InsertRear(1)
# obj.GetRear()

# print(obj.GetRear())








# Question 5

class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self):
          self.head = None
          self.tail = None

    def Insert(self,x,j):
        
        if j == 1:
            newnode = Node(x)
            newnode.next = self.head
            self.head = newnode
            
        i = 1
        n = self.head
        while i < j-1 and n is not None:
            n = n.next
            i = i+1
        if n is None:
            return -1
        else: 
            newnode = Node(x)
            newnode.next = n.next
            n.next = newnode
        

    def SearchByValue(self,x):
        if self.head is None:
            return -1
        
        n = self.head
        i = 0
        while n is not None:
            if n.value == x:
                return i
            n = n.next
            i += 1

        return -1
    
    def DeleteDuplicates(self):
        # // your code goes here
        pass
    
    def Print(self):
        x = self.head
        while x != None:
            print(x.value)
            x = x.next

# obj = LinkedList()
# obj.Insert(5, 1)
# obj.Insert(10, 2)
# obj.Insert(15, 3)



# print(obj.SearchByValue(10))
# obj.DeleteDuplicates()

# obj.Print()












