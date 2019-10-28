class Node(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_start(self,data):
        self.size +=1
        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
        else:
            NewNode.next_node = self.head
            self.head = NewNode


    def insert_end(self,data):
        self.size +=1
        NewNode = Node(data)

        if self.head is None:
            self.head = NewNode
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = NewNode



    def remove(self, data):
        if self.head is None:
            return
        self.size -=1

        current_node = self.head
        previous_node = None

        while current_node.data != data:
            previous_node = current_node
            current_node = current_node.next_node

        if previous_node is None:
            self.head = current_node.next_node
        else:
            previous_node.next_node = current_node.next_node

    def traverse_list(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    # def reverse_traverse_list(self):





linklist = LinkedList()

linklist.insert_start(12)
linklist.insert_end(11)
linklist.insert_start(14)
linklist.remove(14)
linklist.traverse_list()
