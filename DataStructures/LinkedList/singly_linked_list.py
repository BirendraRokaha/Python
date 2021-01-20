'''
Singly Linked list implementation with insertion methods
'''

class Node:
    '''
    A class to represent a Node.

    Attributes
    data = data of the node
    next = pointer to the next node

    '''
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    '''
    A class to represent a LinkedList DataStructure.

    Attributes
    head = Head/First element of the linked list

    '''

    def __init__(self):
        self.head = None

    def print_list(self):
        ''' Prints the linked list '''
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        ''' Append into a Linked list '''
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        # This is same
        # while last_node.next is not None:
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        ''' Prepend data at the begining '''
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_between(self, prev_node, data):
        ''' Insert node in between '''
        if not prev_node:
            print("Node not found")
            return

        new_node = Node(data)

        new_node.next = prev_node.next

        prev_node.next = new_node


llist = LinkedList()


llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
print("Append")
llist.print_list()

llist.prepend("E")
print("Prepend")
llist.print_list()

llist.insert_between(llist.head.next, "F")
print("Insert between")
llist.print_list()
