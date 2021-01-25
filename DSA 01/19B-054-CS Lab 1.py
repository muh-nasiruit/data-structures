'''
Muhammad Nasir
19B-054-CS
Section: B

P.S: Kindly uncomment the driver code
to begin execution of the function.
'''

'''
Question 1
'''

def EvenList(n):
    even = []
    for i in range(n):
        y = int(input("Enter the numbers: "))
        if y%2 == 0:
            even.append(y)
    return even

# n1 = int(input("Enter the range: "))
# x1 = EvenList(n1)
# print(x1)

'''
Question 2
'''

def Max(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0, n- 1):
            if l[j] > l[j+ 1] : 
                l[j], l[j+ 1] = l[j+ 1], l[j]
    return l[-1]

# x2 = Max([3,5,21,1,9,4])
# print(x2)    

'''
Question 3
'''
def Min(l):
    n = len(l)
    for i in range(n-1):
        for j in range(0, n- 1):
            if l[j] > l[j+ 1] : 
                l[j], l[j+ 1] = l[j+ 1], l[j]
    return l[0]

# x3 = Min([3,5,21,1,9,4])
# print(x3)
    
'''
Question 4
'''
def Last(l):
    return l[-1]

# x4 = Last([2,4,6])
# print(x4)
    
'''
Question 5
'''

def KElement(l, k):
    if (k+1)>(len(l)):
        return "Range exceeds limit."
    
    else:
        return l[k]
    
# x5 = KElement([5,8,3,12,9], 2)
# print(x5)
        
'''
Question 6
''' 

def SecondLast(l):
    return l[-2]

# x6 = SecondLast([5,8,3,12,9])
# print(x6)
    
'''
Question 7
'''

def Reverse(l):
    rev = []
    for i in range(len(l)):
        rev.append(l[-i])
    rev.pop(0)
    rev.append(l[0])
    return rev

# x7 = Reverse([5,8,3,12,9])
# print(x7)
    
'''
Question 8
'''

def Unique(l):
    u = []
    for i in l:
        if i not in u:
            u.append(i)
    return u

# x8 = Unique([5,4,7,8,8,9,4,2])
# print(x8)
    
'''
Question 9
'''

def UserNumber(n):   

    c = 0
    while c<10:
        i = int(input("Enter a number: "))
        if i%2 == 0:
        
            n.append(i)
        c+=1
    return n

# x9 = UserNumber(n=[])
# print("Even List: {}\nMin Value: {}\nMax Value: {}\nLast Element: {}\nSecond Last Element: {}"
#       .format(x9,  Min(x9), Max(x9), Last(x9), SecondLast(x9)))


'''
Question 10
'''

def ShowExcitement():
    s = "A quick brown fox jumps over the lazy dog"
    return (s+" " )* 5

# x10 = ShowExcitement()
# print(x10)

'''
Question 11
'''

def Greater(n1, n2, n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    else: 
        return n3
    
# x11 = Greater(8,20,3)
# print(x11)

'''
Question 12
'''    

def Divide(dividend, divisor):
    p = dividend%divisor
    q = dividend//divisor
    return q, p

# x12 = Divide(8, 4)
# print(x12)

'''
Question 13
''' 

class Person:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def birthday(self):
        self.age = self.age + 1
        return f"Happy Birthday {self.name}!\nYou are now: {self.age}"

# x13 = Person("Zain", 19)
# print(x13.birthday())


'''
HOME TASK
'''

from cmath import sqrt,phase

def PolarCoordinates(z):
    print("r = ", round(sqrt(pow(z.real,2)+pow(z.imag,2)).real, 3))
    print("φ = ", round(phase(complex(z.real,z.imag)),3))

# z = 1+2j
# PolarCoordinates(z)



























