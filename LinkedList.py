
class Node:
    def __init__(self, data=None):
        self.val = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, val):
        new_Node = Node(val)
        if (self.head == None):
            self.head = new_Node
            return
        cur = self.head
        while(cur.next != None):
            cur = cur.next

        cur.next = new_Node

    def display(self):
        cur = self.head
        while(cur != None):
            print(cur.val, end = ' ')
            cur = cur.next


my_list = LinkedList()
my_list.insert(10)
my_list.insert(11)
my_list.insert(12)
my_list.display()

