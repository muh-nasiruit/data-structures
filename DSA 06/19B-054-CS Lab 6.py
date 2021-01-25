


class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        
        
    def InsertAtFirst(self, value):
        newnode = Node(value)
        newnode.next = self.head
        self.head = newnode
            
    def InsertAtEnd(self, value):
        newnode = Node(value)
        x = self.tail
        # check if list is empty
        if x is None:
            self.tail = newnode
        
        n = self.head
        while n.next is not None:
            n = n.next
        n.next = newnode

    def InsertAfter(self, item, val):
        x = self.head
        while x != None:
            if x.value == item:
                break
            x = x.next
        if x is None:
            print("item not in list.")
        
        else:
            newnode = Node(val)
            newnode.next = x.next
            x.next = newnode
                  
    def DeleteAtFirst(self):
        x = self.head
        if x is None:
            raise Exception("Empty List")
        
        x = x.next
        self.head = x
            
    def DeleteAtEnd(self):
        x = self.head
        if x is None:
            raise Exception("List is Empty")
        
        while x.next.next is not None:
            x = x.next
        self.tail = x
        x.next = None
    
    def DeleteByValue(self, e):
        x = self.head
        while x != None:
            if x.next.value == e:
                y = x.next
                x.next = x.next.next
                y = None
                break
            x = x.next
        
    def Head(self):
        return self.head.value
    
    def Tail(self):
        return self.tail.value

    def Print(self):
        x = self.head
        while x != None:
            print(x.value)
            x = x.next

# obj = LinkedList()

# obj.InsertAtFirst(2)
# obj.InsertAtFirst(3)
# # obj.InsertAtFirst(5)
# obj.InsertAtFirst(9)
# obj.InsertAtFirst(11)
# obj.InsertAtFirst(15)
# obj.InsertAtFirst(18)

# # obj.InsertAtEnd(10)

# obj.InsertAfter(9, 5)
# obj.DeleteByValue(11)
# # will not delete the end element

# # obj.DeleteByValue(18)
# # obj.InsertAtFirst(20)
# # obj.DeleteAtFirst()
# # obj.DeleteAtEnd()

# obj.Print()

class Stack:
    def __init__(self, size):
        self.size = size
        self.top = 0
        self.obj = LinkedList()
        
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
            self.obj.InsertAtFirst(e)
            self.top += 1
            
    def Pop(self):
        if self.IsEmpty() == True:
            return "Underflow detected."
        
        else:
            self.obj.DeleteAtFirst()
            self.top -= 1

    def Peek(self):
        return self.obj.Head()
    
    def Count(self):
        return self.top

    def Print(self):
        self.obj.Print()
        

# y = Stack(5)
# y.Push(9)
# y.Push(11)
# y.Push(15)
# y.Push(20)
# y.Push(24)
# # y.Pop()
# y.Print()
# print("Peek = ", y.Peek())
# print("Count = ", y.Count())


class Queue:
    def __init__(self):
        self.head = None
        self.last = None

 
    def Enqueue(self, value):
        if self.last == None:
            self.head = Node(value)
            self.last = self.head
        else:
            self.last.next = Node(value)
            self.last = self.last.next
 
    def Dequeue(self):
        if self.head == None:
            return None
        else:
            to_return = self.head.value
            self.head = self.head.next
            return to_return


    def Print(self):
        x = self.head
        while x != None:
            print(x.value)
            x = x.next

# z = Queue()
# z.Enqueue(3)
# z.Enqueue(5)
# z.Enqueue(7)
# z.Enqueue(10)
# z.Dequeue()
# z.Dequeue()
# z.Enqueue(20)
# z.Print()
        








