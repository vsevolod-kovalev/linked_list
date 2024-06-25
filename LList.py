class Node:
    def __init__(self, data=0):
        self.data = data
        self.next = None
class LList:
    def __init__(self):
        self.head = None
    def append(self, data):
        newNode = Node(data)
        if self.head == None:
            self.head = newNode
            return
        t_head = self.head
        while (t_head.next != None):
            t_head = t_head.next
        t_head.next = newNode
    def prepend(self, data):
        newNode = Node(data)
        if (self.head != None):
            newNode.next = self.head
        self.head = newNode
    def insert_after_node(self, prev_node, data):
        if (prev_node == None):
            raise Exception("Cannot insert after None")
        newNode = Node(data)
        t_head = self.head
        while (t_head != prev_node):
            t_head = t_head.next
        newNode.next = prev_node.next
        prev_node.next = newNode
    def delete_node(self, key):
        if (key == None):
            raise ValueError("Cannot delete a node with None data")
        t_head = self.head
        if (t_head == None):
            raise Exception("List is empty")
        if (t_head.data == key):
            self.head = self.head.next
            return
        while (t_head.next != None):
            if (t_head.next.data == key):
                t_head.next = t_head.next.next
                return
            t_head = t_head.next
        raise Exception("Node with the specified key does not exist")

    def delete_node_at_pos(self, pos):
        if not isinstance(pos, int):
            raise ValueError("Position must be an integer")
        if pos < 0:
            raise ValueError("Position must be a non-negative integer")
        if (self.head == None):
            raise Exception("List is empty")
        if (pos == 0):
            self.head = self.head.next
            return
        t_head = self.head
        current_index = 0
        while current_index != pos-1 and t_head.next != None:
            t_head = t_head.next
            current_index += 1
        if (t_head.next != None):
            t_head.next = t_head.next.next
            return
        raise Exception("Position is out of bounds")

    def search(self, key):
        t_head = self.head
        while (t_head is not None):
            if (t_head.data == key):
                return t_head
            t_head = t_head.next
        raise Exception("Node with the specified key does not exist")

    def get_length(self):
        length = 0
        t_head = self.head
        while (t_head != None):
             t_head = t_head.next
             length += 1
        return length

    def reverse_recursively(self):
        def reverseHelper(node):
            if (node.next is None):
                self.head = node
                return node
            reverseHelper(node.next).next = node
            return node
            
        if self.head is not None:
            reverseHelper(self.head).next = None
    def reverse(self):
        t_head = self.head
        next = None
        prev = None
        while (t_head is not None):
            next = t_head.next
            t_head.next = prev
            prev = t_head
            t_head = next
        self.head = prev

    def middle(self):
        if (self.head == None):
            raise Exception("List is empty")
        slow = self.head
        fast = self.head
        while not (fast is None or fast.next is None):
            slow = slow.next
            fast = fast.next.next

        return slow

    def has_cycle(self):
        pass
    def print(self):
        t_head = self.head
        while (t_head != None):
            print(t_head.data)
            t_head = t_head.next
    def print_reverse(self):
        def print_reverse_helper(node):
            if (node is None):
                return
            print_reverse_helper(node.next)
            print(node.data)
        print_reverse_helper(self.head)
            
    

l = LList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.append(5)
# l.prepend(10)
# l.insert_after_node(l.head, 99)
# l.insert_after_node(l.search(3), 100)
l.print()
print("\n")
l.reverse()
l.print()
print()
print(l.middle().data)

# print(l.get_length())

