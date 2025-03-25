class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}  # key => Node

        self.dummy_head = Node(0, 0)
        self.dummy_tail = Node(0, 0)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def _insert_at_front(self, node):
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        self.dummy_head.next.prev = node
        self.dummy_head.next = node

    def _move_to_front(self, node):
        self._remove(node)
        self._insert_at_front(node)

    def get(self, key: int) -> int:
        if key in self.hash:
            node = self.hash[key]
            self._move_to_front(node)
            return node.value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            node = self.hash[key]
            node.value = value
            self._move_to_front(node)
        else:
            if len(self.hash) == self.capacity:
                # Remove LRU
                lru_node = self.dummy_tail.prev
                self._remove(lru_node)
                del self.hash[lru_node.key]
            new_node = Node(key, value)
            self._insert_at_front(new_node)
            self.hash[key] = new_node
