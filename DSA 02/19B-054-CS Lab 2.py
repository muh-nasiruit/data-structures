
''' Lab 2 '''

'''
Question 1
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
            
    def RightDiagonal(self):
        for i in range(3):
            for j in range(1):
                print(self.GetValue(i, -i), end = " ")
            



    
    def SubValue(self, a1, a2):
        x = a1.data
        y = a2.data
        result = [x[i] - y[i] for i in range(len(x))]

        for i in range(self.row):
            for j in range(self.col):
                print(result[self.Location(i, j)], end =" ")
            print('\n')
        
        
    
    def MultValue(self, a1, a2):
        a1 = a1.data
        a2 = a2.data
        
        res = []
        for i in range(len(a1)):
            res.append(a1[i]*a2[i])
        
        for i in range(self.row):
            for j in range(self.col):
                print(res[self.Location(i, j)], end =" ")
            print('\n')        
            

        
    def Transpose(self):
        for i in range(self.row):
            for j in range(self.col):
                print(self.GetValue(j, i), end =" ")
            print('\n')


row = 3 
col = 3

row2 = 3
col2 = 3

arr1 = Array(row, col)
arr2 = Array(row, col)

for i in range(row):
    for j in range(col):
        arr2.SetValue(i, j, i-j)

print(arr1.data)
arr1.RightDiagonal()



# # For Subtraction
# arr1.SubValue(arr1, arr2)
# print("")
        
# # For Multiplicaiton
# arr1.MultValue(arr1, arr2)
# print("")

# # For Transpose
# arr1.Print()
# arr1.Transpose()
# print("")
# arr2.Print()
# arr2.Transpose()


'''
Question 2


import numpy as np

array1 = np.array([[1,2,3,4], [5,6,7,8,]], dtype=np.int64)
print(array1)
print("")

x = np.ones((3,3), dtype=np.int64)
print(x)
print("")

y = np.zeros((1,3,3), dtype=np.int16)
print(y)
print("")

array2 = np.random.random((2,2))
print(array2)
print("")

array3 = np.full((3,3),7)
print(array3)
print("")

array4 = np.identity(3, dtype = np.int64)
print(array4)
print("")


# Sum of Two matrices
add = np.add(x, y)
print(add)
print("")

# Difference of Two matrices
diff = np.subtract(x, y)
print(diff)
print("")

# Multplication of Two matrices
mult = np.multiply(x,y)
print(mult)

# Division of Two matricies
div = np.divide(y,x)
print(div)

# Remainder of Two matrices
rem = np.remainder(y, x)
print(rem)

# Checking if both arrays are equal
result = np.array_equal(x, y)
print(result)

'''


































