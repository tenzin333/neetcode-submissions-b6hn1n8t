class ListNode: 
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.map = {}
        self.head = ListNode(0,0)
        self.tail = ListNode(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
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
        
        node = ListNode(key,value)
        self.map[key] = node
        self.add(node)

        if len(self.map) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.map[lru.key]
        
    def remove(self,node) -> None:
        prev = node.prev
        nxt = node.next


        prev.next = node.next
        nxt.prev = prev

    def add(self,node) -> None:
        prev = self.tail.prev

        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node






