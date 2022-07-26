class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.items = [None] * size
       
    def is_empty(self):
         if self.top == -1 :
            return 1
         else:
            return 0
        
    def is_full(self):
        if self.top == (self.size - 1):
            return 1
        else:
            return 0

    def push(self, data):
        if not self.is_full():
            self.top = self.top + 1
            self.list[self.top] = data
   
               
    def pop(self):
        if not self.is_empty():
            v = self.list[self.top]
            del self.list[self.top]
            self.top = self.top - 1
            
    def status(self):
         if self.isEmpty() != 1:
            for i in range (0,self.top+1):
                print(self.list[i])
        
# Do not change the following code
size, queries = map(int, input().rstrip().split())
stack = Stack(size)
for line in range(queries):
    values = list(map(int, input().rstrip().split()))
    if values[0] == 1:
        stack.push(values[1])
    elif values[0] == 2:
        stack.pop()
stack.status()
