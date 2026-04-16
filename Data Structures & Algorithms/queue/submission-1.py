class Node:
    def __init__(self,val=0):
        self.val = val
        self.next = None

class Deque:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self) -> bool:
        if not (self.head and self.tail):
            return True
        else:
            return False

    def append(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            if self.tail:
                cur = self.tail
                cur.next = new_node
                self.tail = new_node
            else:
                print("1ERROR")

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        if self.isEmpty():
            self.head = new_node
            self.tail = new_node
        else:
            if self.head:
                cur = self.head
                new_node.next = cur
                self.head = new_node
                # print(f"head: {self.head.val}")
                # print(f"tail: {self.tail.val}")
            else:
                print("2ERROR")

    def pop(self) -> int:
        if self.isEmpty():
            return -1
        if self.head:
            cur = self.head
            if cur == self.tail:
                popping_node = cur
                cur.next = None
                self.tail = None
                self.head = None
                return cur.val 
            while cur:
                if self.tail:
                    if cur.next == self.tail:
                        popping_node = cur.next
                        cur.next = None
                        self.tail = cur
                        return popping_node.val
                else:
                    print("3ERROR")
                cur = cur.next
        else:
            print("4ERROR")

    def popleft(self) -> int:
        if self.isEmpty():
            return -1
        if self.head:
            # print(f"head: {self.head}.val")
            # print(f"tail: {self.tail}.val")
            popping_node = self.head
            new_head = self.head.next
            self.head = new_head
            popping_node.next = None
            # print(f"head: {self.head.val}")
            # print(f"tail: {self.tail.val}")
            return popping_node.val
        else:
            print("5ERROR")