'''
Lab 3
'''

def LinearSearch(lst, v):
    for i in range(len(lst)):
        if lst[i] == v:
            return i
    else:
        return -1
    
# print(LinearSearch([2,3,4,5,6], 5))


# Data must be sorted

def BinarySearch(data, n, v):
    l = 0
    r = n-1
    while l <= r:
        m = (l+r)//2
        if data[m] < v:
            l = m + 1
        elif data[m] > v:
            r = m -1
        else:
            return m
    return -1

# print(BinarySearch([2,3,4,5,6,7,8], 7, 7))


class List:
    
    def __init__(self, data=[]):
        self.data = data

    
    def InsertAtFirst(self, v):
        self.data.insert(0, v)
        return self.data
    
    def InsertAtEnd(self, v):
        self.data.insert(len(self.data), value)
        return self.data
    
    def DeleteFromFirst(self):
        x = self.data[0]
        self.data = self.data[1:]
        return x
    
    def DeleteFromEnd(self):
        x = self.data[-1]
        self.data = self.data[-2:]
        return x
    def Print(self):
        return self.data
    
    def LinearSearch(self, v):
        
        for i in range(len(self.data)):
            if self.data[i] == v:
                return i
        else:
            return -1

    def BinarySearch(self, n, v):
        l = 0
        r = n-1
        while l <= r:
            m = (l+r)//2
            if self.data[m] < v:
                l = m + 1
            elif self.data[m] > v:
                r = m -1
            else:
                return m
        return -1
    
    def IsSorted(self):
        x = self.data[:]
        x.sort()
        if self.data == x:
            return True
        else:
            return False
    
    def Search(self, v):
        x = self.data[:]
        x.sort()
        if self.data == x:
            return self.BinarySearch(len(self.data), v)
        else:
            return self.LinearSearch( v)

        
        
    
# l1 = List([3,5,6,21,32,1,9])
# print(l1.Print())
# print(l1.Search(32))    
# print(l1.Print())




















