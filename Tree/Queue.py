from QNode import QNode

class Queue:
    def __init__ (self, front = None, last = None):
        self.front = front
        self.last = last
        
    def isEmpty(self):
        return (self.front is None)
    def visit (self, x):
        print (x.data, end="")
    
    def display (self):
        if self.isEmpty:
            print ("404 not found")
        
        else:
            cur = self.front
            while cur is not None:
                self.visit(cur)
                cur = cur.next
    
    def enqueue(self, x):
        node = Node(x)
        if self.isEmpty() == True:
            self.front = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        
    def dequeue(self):
        if self.isEmpty() == True:
            print ("Queue is Empty")
        else:
            tmp = self.front
            self.front = self.front.next
            self.front.next = None
            if tmp == self.last:
                self.last = None            
            return tmp 
    
        
        
            
            