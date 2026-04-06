class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}

        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        node = self.map[key]
        self.remove(node)
        self.add(node)
        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = Node(key,value)
        self.add(node)
        self.map[key] = node

        if len(list(self.map)) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.map[lru.key]


    def remove(self,node) -> None:
        prev_node = node.prev 
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def add(self,node) -> None:
        prev_node = self.tail.prev
        prev_node.next = node
        
        node.prev = prev_node
        node.next = self.tail
       
        self.tail.prev = node





        

        
