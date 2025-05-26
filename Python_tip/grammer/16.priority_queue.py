import heapq

# Default : Min heap(smallest one)
h1 = [10, 20, 15, 30, 40]

heapq.heapify(h1)

min = heapq.heapreplace(h1, 5)

print(min)

h2 = [2, 4, 6, 8]

h3 = list(heapq.merge(h1, h2))

# Push(heappush) : Adds an element to the heap while maintaining the heap property
# Pop(heappop) : Removes and returns the smallest element in the heap, agin maintaining the heap property
# Peek : View the smallest element without removing it
# Heapify: Convert a regular list into a valid heap in-place


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
            return
        
        queue = [self.root]
        while queue:
            current = queue.pop(0)
            
            if current.left is None:
                current.left = Node(data)
                return
            else:
                queue.append(current.left)
                
            if current.right is None:
                current.right = Node(data)
                return
            else:
                queue.append(current.right)
                
    def heapify(start_node):
        large = start_node.data
        