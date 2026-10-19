from Node import Node

class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
    
    def isEmpty (self):
        return (self.head is None)
    
    def visit(self, x, end=" "):
        print(x.data, end=" ")
    
    
    def travel(self):
        cur = self.head
        while (cur is not None):
            self.visit(cur, end=" ")
            
    def addLast (self, x):  
        new = Node (x)
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            self.tail = new    
        return    
        
    def addFirst (self, x):
        new = Node(x)
        if self.isEmpty():
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head = new
        return
        
    def addAt(self, x, i):
        new = Node(x)
        if self.isEmpty():
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
                par = cur
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
        elif self.head == self.tail:
            self.head = None
            self.tail = None
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
                par = cur
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
                    temp = i.data
                    i.data = j.data
                    j.data = temp
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
                    temp = i.data
                    i.data = j.data
                    j.data = temp
                j = j.next
            i = i.next               
        return 
    
    def sort_by_n (self , n):
        i = self.head
        while i is not None:
            if i.data.Price < n:           # so sanh voi dieu kien < n cua i
                j = i.next 
                while j is not None:
                    if j.data.Price < n:   # so sanh voi dieu kien < n cho j
                        if i.data.Price >= j.data.Price:  # loc dieu kien dau tien la Price
                            if i.data.Price > j.data.Price: # neu Price thoa ma thi chay
                                temp = i.data
                                i.data = j.data
                                j.data = temp
                            elif i.data.Brand > j.data.Brand: # vi da loc tu truoc nen neu no sai cai dau thi dieu kien la bang nhau van co san
                                temp = i.data
                                i.data = j.data
                                j.data = temp
                            elif i.data.Brand == j.data.Brand and i.data.Code < j.data.Code: #loc dieu kien lan 3
                                temp = i.data
                                i.data = j.data
                                j.data = temp
                                
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

    def find_minimum (self):
        cur = self.head
        mini = 9999999
        index = 0
        tmp = 0
        while cur is not None:
            if mini >= cur.data.Price:
                mini = cur.data.Price
                tmp = index
            cur = cur.next
            index = index + 1
        return tmp