

class Node:
    def __init__(self, e):
        self.value = e
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        
    def Insert(self, value):
        #wrapper function encapsulates the implementation technique
        self.root = self.__Insert(self.root, value)
        
    def __Insert(self, root, value):
        #if tree is empty
        if root is None:
            root = Node(value)
            
        else:
            if value > root.value:
                root.right = self.__Insert(root.right, value)
            
            else:
                root.left = self.__Insert(root.left, value)
        
        return root
    
    def InOrder(self):
        return self.__InOrder(self.root)
    
    def __InOrder(self, root):
        if root:
            self.__InOrder(root.left)
            print(root.value)
            self.__InOrder(root.right)

    def PreOrder(self):
        #wrapper function encapsulates the implementation technique
        return self.__PreOrder(self.root)

    def __PreOrder(self, root):
        if root:
            print(root.value)
            self.__PreOrder(root.left)
            self.__PreOrder(root.right)
            
    def PostOrder(self):
        #wrapper function encapsulates the implementation technique
        return self.__PostOrder(self.root)
    
    def __PostOrder(self, root):
        if root:
            self.__PostOrder(root.left)
            self.__PostOrder(root.right)
            print(root.value)
        
    def Height(self, root):
        return self.__Height(self.root)

    def __Height(self, root):
        if root is None:
            return -1
        
        h = 1 + max(self.__Height(root.left), self.__Height(root.right))
        return h

    def FindMin(self):
        x = self.__FindMin(self.root)
        return x.value

    
    def __FindMind(self, root):
        while root.left is not None:
            if root.left is None:
                break
            root = root.left
        
        return root
        
    def FindMax(self, root):
        x = self.__FindMax(self.root)
        return x.value
    
    def __FindMax(self, root):
        if root.right is None:
            return root
        
        return self.__FindMax(root.right)

    def Delete(self, value):
        return self.__Delete(self.root, value)

    def __Delete(self, root, value):
        if root is None:
            return root

        if value < root.value:
            root.left = self.__Delete(root.left, value)

        elif value > root.value:
            root.right = self.__Delete(root.right, value)

        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.__FindMin(root.right)
            root.value = temp.value
            root.right = self.__Delete(root.right, temp.value)
        return root

#Succssor: Minimum element in right subtree        
#Drive Code
            
obj = BST()
obj.Insert(2)
obj.Insert(3)
obj.Insert(4)
obj.Insert(10)
obj.Insert(9)
obj.Insert(1)

# print("PreOrder:")
# obj.PreOrder()

print("\nInOrder:")
obj.InOrder()
print()

obj.Delete(4)

print("\nInOrder:")
obj.InOrder()
print()
# print("\nPostOrder:")
# obj.PostOrder()

print(obj.Height(2)) 


