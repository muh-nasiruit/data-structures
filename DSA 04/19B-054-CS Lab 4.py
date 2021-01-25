
import random

class Sorting:
    
    data = []
    
    def __init__(self):
        pass
    
    def GenerateRandom(self, n):
        self.data = random.sample(range(1,100),n)
        return self.data
    
    def BubbleSort(self):
        flag = False # To Modify the code
        # which will check and break if list sorted.
        
        n = len(self.data)
        for i in range(n):
            for j in range(n-1):
                if self.data[i] > self.data[j]: 
                    temp = self.data[i]
                    self.data[i] = self.data[j]
                    self.data[j] = temp
                    flag = True
            if flag == False:
                break
        return self.data
    
    def Print(self):
        print("List = ", self.data)

    def InsertionSort(self):
        for i in range(1, len(self.data)):
            key = self.data[i]
            j = i - 1
            
            while j >= 0 and self.data[j] > key:
                self.data[j+1] = self.data[j]
                j = j - 1
            self.data[j+1] = key
            
        return self.data
    
    def SelectionSort(self):
        n = len(self.data)
        
        for i in range(n):
            min_i = i
            
            for j in range(i+1, n):
                if self.data[j] < self.data[min_i]:
                    min_i = j
                    
            self.data[i], self.data[min_i] = self.data[min_i], self.data[i]
    
        return self.data
    
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

    def Search(self, v):
        x = self.data[:]
        x.sort()
        if self.data == x:
            print("Sorted List Already = ", self.data)
            return f"Location = {self.BinarySearch(len(self.data), v)}"
        
        else:
            print("List = ", self.data)
            self.data = self.SelectionSort()
            print("Sorted List = ", self.data)
            return f"Location = {self.BinarySearch(len(self.data), v)}"
            
   

        
'''
Time Complexity of BubbleSort = O(n^2)
Time Complexity of InsertionSort = O(n)
InsertionSort is better than BubblesSort
'''

obj = Sorting()
obj.GenerateRandom(10)

# print("Bubble Sorted = ", obj.BubbleSort())
# print("Insertion Sorted = ", obj.InsertionSort())
# print("Selection Sorted = ", obj.SelectionSort())
print(obj.Search(32))




