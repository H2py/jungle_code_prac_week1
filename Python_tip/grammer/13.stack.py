class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack.pop()
    
    def peak(self):
        if self.isEmpty():
            return 'Stack is Empty'
        return self.stack[-1]
    
    
list(map(lambda x: x**2, range(10)))
list(map(lambda x : x + 2 , range(10)))