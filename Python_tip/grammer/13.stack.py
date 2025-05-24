class Stack:
    def __init__(self):
        self.stack = []
        
    def push(self,element):
        self.stack.append(element)
        
    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
myStack = Stack()
myStack.push(3)
myStack.push(1)
myStack.push(4) # myStack = [3, 1, 4]

myStack.pop() # return 4 and myStack = [3, 1]

myStack.isEmpty() # False