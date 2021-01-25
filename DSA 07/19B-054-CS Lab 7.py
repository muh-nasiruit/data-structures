
# Task 1:

def Write(n):    
    if n == 1:
        print(n)
    else:
        print(n)
        Write(n-1)
# Write(5)

# Task 2:

def Factorial(n):
    if n == 1:
        return n
    else:
        return n * Factorial(n-1)

# Factorial(5)

# Task 3:
        
def GCD(a, b): 
    if b == 0: 
        return a 
    else: 
        return GCD(b, a%b)

# GCD(8,12)

# Task 4:

def Binary_Search(List ,low ,high, value):
    
    if high >= low:
        mid = (high + low) // 2
        
        if List[mid] == value:
            return mid
        
        elif List[mid] > value:
            return Binary_Search(List, low, mid - 1, value)
        
        else:
            return Binary_Search(List, mid + 1, high, value)
    else:
        return -1
    
# Binary_Search([3,5,7,9,11,13,15,57],0, 6, 9)

# Task 5:

def partition(arr, f, r):
    pivot = arr[f]
    low = f + 1
    high = r

    while True:
        while low <= high and arr[high] >= pivot:
            high = high - 1
        while low <= high and arr[low] <= pivot:
            low = low + 1
        if low <= high:
            arr[low], arr[high] = arr[high], arr[low]
        else:
            break
    arr[f], arr[high] = arr[high], arr[f]

    return high


def QuickSort(arr, f, r):
    if f >= r:
        return

    p = partition(arr, f, r)
    QuickSort(arr, f, p - 1)
    QuickSort(arr, p + 1, r)
    return arr

# QuickSort([22,21,1,9,10,11], 0, 5)

