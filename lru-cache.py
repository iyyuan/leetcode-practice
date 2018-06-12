class Node(object):
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.mem = dict()
        self.head = None
        self.tail = None

    def add_node(self, node):
        """
        Add a node to the head of the DLL
        """
        # Always make the node the head and update it's
        # next ptr to point to the head
        node.next = self.head
        if self.head:
            # If the head is not None, need to
            # update the head's prev ptr to be the node's address
            self.head.prev = node
        self.head = node

        # If the tail is None, then the node
        # being added is also the tail
        if self.tail is None:
            self.tail = node


    def remove_node(self, node):
        """
        Remove a node in the DLL
        """
        if node == self.head and node == self.tail:
            # Edge case where DLL only has one node
            # Remove it and update head and tail ptrs
            self.head = None
            self.tail = None
        elif node == self.head:
            # Edge case where node is the head
            # Update the head to be the next node
            self.head = node.next
        elif node == self.tail:
            # Edge case where node is the tail
            # Update the tail to be the previous node
            self.tail = node.prev
        else:
            # Make the previous node's next ptr equal to the node's next ptr
            # Make the next node's prev ptr equal to the node's prev ptr
            node.prev.next = node.next
            node.next.prev = node.prev


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.mem:
            node = self.mem[key]
            # Remove the node and add it to the front
            self.remove_node(node)
            self.add_node(node)
            return node.value
        return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.mem:
            # Updating existing key
            node = self.mem[key]
            node.value = value
            # Remove the node and add it to the front
            self.remove_node(node)
            self.add_node(node)
        else:
            # Adding a new key
            if self.size == self.capacity:
                # Delete the tail node if full
                del self.mem[self.tail.key]
                self.remove_node(self.tail)
                self.size -= 1

            # Add a new node to the head of the DLL
            node = Node(key, value)
            self.mem[key] = node
            self.add_node(node)
            self.size += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
