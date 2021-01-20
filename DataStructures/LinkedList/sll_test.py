'''
    create a singly linked list.
'''


class Node():
    def __init__(self, data):
        self.data = data
        self.next = None


class s_linked_list():
    def __init__(self):
        self.head = None

    def print_llist(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head

        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node


llist = s_linked_list()

llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
print('Append')
llist.print_llist()

llist.prepend('Start')
print('Prepend')
llist.print_llist()


