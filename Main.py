import os
class Stack:
    def __init__(self, size):
        self.top = 
        self.items = []
        self.size = size

    def is_empty(self):
         if self.top == -1 :
            return 1
        else :
            return 0
        
    def is_full(self):
        if self.top = self.size - 1

    def push(self, data):
        if not self.is_full():
            # Write code here

    def pop(self):
        if not self.is_empty():
            # Write code here

    def status(self):
        # Write code here

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
