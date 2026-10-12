from Node import Node

class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    
    def isEmpty (self):
        return (self.head is None)
    
    def visit (self, x):
        print (x.data)
    
    
    def travel(self):
        cur = self.head
        while (cur is not None):
            self.visit(cur, end=" ")
            
    def addLast (self, x):  
        new = Node (x)
        if self.isEmpty:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new    
        return    
        
    def addFirst (self, x):
        new = Node(x)
        if self.isEmpty:
            self.head = new
            self.tail = new
        else:
            tmp = self.head
            self.head = x
            self.head.next = tmp
        return
        
    def addAt(self, x, i):
        new = Node(x)
        if self.isEmpty:
            self.head = new
            self.tail = new
        elif i == 0:
            self.addFirst (x)
        else:
            cur = self.head.next
            count = 1
            par = self.head
            while cur is not None:
                if count == i:
                    par.next = new
                    new.next = cur
                    return
                cur = cur.next 
                count = count + 1
        return
    
    def delLast (self):
        if self.isEmpty():
            print("List is Empty")
        else:
            cur = self.head
            par = self.head
            while cur is not None:
                if cur == cur.tail:
                    par.next = None
                    self.tail = par
                    return
                cur = cur.next
        return

    def delFirst(self):
        if self.isEmpty():
            print("List is Empty")
        else:
            tmp = self.head.next
            self.head.next = None
            self.head = tmp
        
    def delAt (self, i):
        if self.isEmpty():
            print("List is Empty")
        
        elif i == 0:
            self.delFirst()
        
        else:
            cur = self.head.next
            par = self.head
            count = 1
            while cur is not None:
                if count == i:
                    par.next = cur.next
                    cur.next = None
                    return
                count = count + 1
                cur = cur.next
        return

    def count (self):
        cur = self.head
        count = 0
        while (cur is not None):
            count = count + 1
            cur = cur.next 
        return count
    
    def getVal (self, index):
        cur = self.head
        count = 0
        if self.isEmpty():
            return 0
        while cur is not None:
            if count == index:
                return cur
            count = count + 1
            cur = cur.next
        return 0
    
    def getIndex(self, x):
        cur = self.head
        count = 0
        while cur is not None:
            if cur.data == x:
                return count
            count = count + 1
            cur = cur.next
        return 0
    
    def sort(self):
        i = self.head
        while i.next is not None:
            j = i.next 
            while j is not None:
                if i.data > j.data:
                    temp = i.info
                    i.info = j.info
                    j.info = temp
                j = j.next
            i = i.next
        return
                    
    def SortFrom (self, x, y):
        cur = self.head
        count = 0
        head = 0
        tail = 0
        while cur is not None:
            if count == x:
                head = cur
            if count == y:
                tail = cur
            cur = cur.next
            count = count + 1
            
        i = head
        while i != self.tail:
            j = i.next
            while j is not None:
                if i.data > j.data:
                    temp = i.info
                    i.info = j.info
                    j.info = temp
                j = j.next
            i = i.next               
        return 
    
    def reverse (self):
        cur = self.head
        pre = None
        while cur is not None:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        self.tail = self.head
        self.head = pre
            