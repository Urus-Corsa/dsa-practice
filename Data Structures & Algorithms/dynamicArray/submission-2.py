class DynamicArray:
    
    # def __init__(self, capacity: int):


    # def get(self, i: int) -> int:


    # def set(self, i: int, n: int) -> None:


    # def pushback(self, n: int) -> None:


    # def popback(self) -> int:
 

    # def resize(self) -> None:


    # def getSize(self) -> int:
        
    
    # def getCapacity(self) -> int:

    def __init__(self, capacity: int = 1):
        self.capacity =capacity
        self.arr = self.capacity * [None]
    def get(self, i: int) -> int:
        return self.arr[i]
    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
    def pushback(self, n: int) -> None:
        if self.getSize() == self.capacity:
            print('resized for push')
            self.resize()
            self.capacity = self.getCapacity()
        self.arr[self.getSize()] = n
    def popback(self) -> int:
        # return self.arr.pop()
        last_elem = self.arr[self.getSize()-1]
        self.arr[self.getSize()-1] = None
        return last_elem
    def resize(self) -> None:
        new_arr = self.capacity*2 * [None]
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
    def getSize(self) -> int:
        elem_counter = 0
        for elem in self.arr:
            if elem != None:
                elem_counter+=1
        return elem_counter
    def getCapacity(self) -> int:
        return len(self.arr)