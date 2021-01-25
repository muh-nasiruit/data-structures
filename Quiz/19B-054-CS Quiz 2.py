'''
Quiz 2

CS B
'''


class Array: 
    def __init__(self, row, col):
        self.row = row 
        self.col = col
        self.data = [i+j for i in range(self.row) for j in range(self.col)]
        # self.data = [0 for i in range(row*col)]
        
    def Location(self, i, j):
        l = i * self.col +j
        return l
    
    def SetValue(self, i, j, v):
        l = self.Location(i, j)
        self.data[l] = v
        
    def GetValue(self, i, j):
        l = self.Location(i, j)
        return self.data[l]
    
    def Print(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.GetValue(i, j), end =" ")
            print('\n')
            
    def SearchDiagonalValue(self, value):
        m = []
        for i in range(3):
            for j in range(1):
                m.append(self.GetValue(i, -i))
        
        if value in m:
            return True
        else: 
            return False
    
    def MaxValue(self):
        m = []
        for i in range(3):
            for j in range(1):

                m.append(self.GetValue(i, i))
        
        m.sort()
        return m[-1]



row = 3 
col = 3

arr1 = Array(row, col)
arr1.Print()

print(arr1.data)
print(arr1.SearchDiagonalValue(2))
print("Maximum Value in the Left Diagonal = ", arr1.MaxValue())









