class MinStack:
    def __init__(self):
        self.arr = []
    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
       if len(self.arr) >= 1:
        minimum = self.arr[0];
        for n in self.arr:
            minimum = min(n, minimum)
        return minimum
       else:
         return 0    
        
