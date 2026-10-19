from Node import Node
from Queue import Queue

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
                elif cur.data > y:
                    par = cur
                    cur = cur.left
                else:
                    par = cur
                    cur = cur.right
            if par.data > y:
                par.left = x
            else:
                par.right = x
        return
    
    def findNode(self, x):
        if self.isEmpty() == True:
            print ("is empty")
            return
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
        
    def inOrder (self, x):
        self.inOrder
        self.visit(x.left)
        self.inOrder(x.right)
        
    def preOrder(self, x):
        self.visit(x)
        self.preOrder(x.left)
        self.preOrder(x.right)
    
    def lastOrder(self, x):
        self.lastOrder(x)
        self.lastOrder(x)
        self.visit(x)
        
    def breadth (self):
        if  self.isEmpty() == True:
            print ("404 Not found")
        else:
            queue = Queue()
            queue.enqueue(self.root)
            while queue.isEmpty() == False:
                tmp = queue.dequeue()
                if tmp.left is not None:
                    queue.enqueue(tmp.left)
                if tmp.right is not None:
                    queue.enqueue(tmp.right)
                print (tmp.data, end=" -> ")
                
    def dfs (self):
        if self.isEmpty() == True:
            print ("404 Not Found")
        else:
            return
        pass
        
                
    # def delete(self):
    #     x = input("Enter your Node: ")
    #     if self.isEmpty() == True:
    #         print("Tree is Empty")
    #     else:
    #         cur, par = self.findNode(x)
    #         if (cur == 0):
    #             print ("404 not found")
    #         else:
                            
                    