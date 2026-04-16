class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def get(self, index: int) -> int: 
        cur = self.head
        counter  = -1
        while cur and counter <= index:
            counter+=1
            if counter == index:
                return cur.val 
            cur = cur.next
        return -1
    
    def insertHead(self, val: int) -> None:
        new_head = Node(val)
        new_head.next = self.head
        if self.tail == self.head == None:
            self.tail = new_head
        self.head = new_head

    def insertTail(self, val: int) -> None:
        new_tail = Node(val)
        if self.tail:
            self.tail.next = new_tail
        if not self.head:
            self.head = new_tail
        self.tail = new_tail

    def remove(self, index: int) -> bool:
        if not self.head:
            return False
        if index == 0:
            if self.tail == self.head:
              self.tail = self.head.next  
            new_head = self.head.next
            self.head.next = None 
            self.head = new_head 
            return True
        prev = self.head
        cur = self.head.next
        counter = 0
        while cur and counter <= index:
            counter+=1
            if counter == index:
                if self.tail == cur:
                    self.tail = prev
                prev.next = cur.next
                cur.next = None
                return True
            prev = cur
            cur = cur.next
        return False
    
    def getValues(self) -> List[int]:
        val_list = []
        head = self.head
        while head:
            val_list.append(head.val)
            head = head.next
        return val_list
        
    # def __init__(self):

    
    # def get(self, index: int) -> int:
        

    # def insertHead(self, val: int) -> None:
        

    # def insertTail(self, val: int) -> None:
        

    # def remove(self, index: int) -> bool:
        

    # def getValues(self) -> List[int]:
        
