from Node import Node

class Node:
    def __init__ (self, root = None):
        self.root = root
        
    def isEmpty(self):
        return self.head is None
    
    def visit (self):
        print (self.data)
    
    def insert(self):
        y = input("Enter your node: ")
        x = Node(x)
        if self.isEmpty() == True:
            self.root = x
        else:
            cur = self.root
            par = self.root
            while cur is not None:
                if cur.data == y:
                    print ("it is exist")
                elif cur > y:
                    par = cur
                    cur = cur.left
                else:
                    par = cur
                    cur = cur.right
            if par > y:
                par.left = x
            else:
                par.right = x
    
    def findNode(self):
        x = input("Enter your Node: ")
        if self.isEmpty() == True:
            print ("is empty")
        else:
            cur = self.root
            par = self.root
            while cur is not None:
                if cur.data == x:
                    return (cur, par)
                elif cur.data > x:
                    par = cur
                    cur = cur.left
                else:
                    par = cur
                    cur = cur.right
            return 0
    
    def delete(self):
        x = input("Enter your Node: ")
        if self.isEmpty() == True:
            print("Tree is Empty")
        else:
            
                    