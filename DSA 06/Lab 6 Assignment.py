

class DNode:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None
        
class DoublyLinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.data = []
        
    def InsertAtFirst(self, value):
        newnode = DNode(value)
        newnode.next = self.head
        self.head = newnode
        if self.tail == None and self.head != None:
            self.tail = newnode
            
    def InsertAtEnd(self, value):
        newnode = DNode(value)
        if self.head is None:
            self.head = newnode
            self.tail = self.head
        else:
            newnode.prev = self.tail
            self.tail.next = newnode
            self.tail = newnode
        
    def InsertAfter(self, item, val):
        x = self.head
        while x != None:
            if x.value == item:
                break
            x = x.next
        if x is None:
            print("item not in list.")
        
        else:
            newnode = DNode(val)
            newnode.next = x.next
            x.next = newnode
                  
    def DeleteAtFirst(self):
        x = self.head
        if x is None:
            raise Exception("Empty List")
        
        x = x.next
        self.head = x
            
    def DeleteAtEnd(self):
        
        x = self.tail
        if x is None:
            raise Exception("List is Empty")
            
        x = x.prev
        self.tail = x

    
    def DeleteByValue(self, e):
        x = self.head
        while x != None:
            if x.next.value == e:
                y = x.next
                x.next = x.next.next
                y = None
                break
            x = x.next

    def Sort(self, data):
        
        # must call GetAll() before Sorting
        if len(data) > 1:
     
            # Finding the mid of the array
            mid = len(data)//2
     
            # Dividing the array elements
            L = data[:mid]
     
            # into 2 halves
            R = data[mid:]
     
            # Sorting the first half
            
            self.Sort(L)
     
            # Sorting the second half
            self.Sort(R)
     
            i = j = k = 0
 
            # Copy data to temp arrays L[] and R[]
            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    data[k] = L[i]
                    i += 1
                else:
                    data[k] = R[j]
                    j += 1
                k += 1
     
            # Checking if any element was left
            while i < len(L):
                data[k] = L[i]
                i += 1
                k += 1
     
            while j < len(R):
                data[k] = R[j]
                j += 1
                k += 1
            
            return data
        
    def Head(self):
        return self.head.value
    
    def Tail(self):
        return self.tail.value

    def Print(self):
        x = self.head
        while x != None:
            print(x.value)
            x = x.next
    
    def GetAll(self):
        x = self.head
        while x != None:
            self.data.append(x.value)
            x = x.next

            
            
obj = DoublyLinkedList()




obj.InsertAtFirst(5)
obj.InsertAtFirst(7)
obj.InsertAtFirst(10)

# obj.InsertAtEnd(200)
# obj.InsertAtEnd(30)
obj.DeleteAtEnd()
# obj.InsertAtEnd(40)
# obj.InsertAtEnd(50)
obj.DeleteAtEnd()
# obj.InsertAtEnd(60)



# obj.GetAll()
# print("Sorted = ", obj.Sort(obj.data))




obj.Print()
