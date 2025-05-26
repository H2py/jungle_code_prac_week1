# Linked List definition : 각각의 노드가 사슬처럼 연결되어 있는 자료구조
# 노드란? 노드는 2가지 정보를 저장하고 있는데, 첫 번째는 데이터이고 두 번째는 연결되어 있는 노드를 가리키고 있다
# 첫번째 노드를 가리키는 head 포인터도 존재한다. 우리는 head 포인터를 이용해서 모든 요소에 접근이 가능하다

# SinglyLinkedList 구현하기
# 앞에 삽입할때는 head가 들어오는 요소를 가리켜야한다 

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class DoublyNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
        

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        
    def insertAtBegin(self, data):
        new_node = Node(data) #새 노드를 생성한다
        if self.head is None: #노드가 없으면, head 포인터는 새 노드를 가리킨다
            self.head = new_node
            return
        else:
            new_node.next = self.head  #새로운 노드의 포인터는 기존, head 포인터가 가리키던 곳을 가리키고,
            self.head = new_node #head 포인터는 새 노드를 가리킨다
        
    def insertAtIndex(self, data, index):
        if (index == 0) :
            self.insertAtBegin(data)
            return
        
        position = 0
        current_node = self.head
        
        while(current_node != None and position+1 != index):
            position += 1
            current_node = current_node.next
            
        if current_node != None:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
        else:
            print("Index not present")
        
    def delete(self, key):
        temp = self.head
        
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
            
        while temp is not None:
            if temp.data == key:
                break
            
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_front(self,data):
        new_node = DoublyNode(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        
    def insert_end(self, data):
        new_node = DoublyNode(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node