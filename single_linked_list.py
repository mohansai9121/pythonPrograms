class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Single_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def display(self):
        if self.head:
            new_list = self.head
            print("Displaying list elements:", end=" ")
            while new_list:
                print(f'{new_list.data}', end=",")
                new_list = new_list.next
            print()
        else:
            print("There is no list to display...!")

    def insert_at_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1
        self.display()

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.count += 1
        self.display()

    def delete_at_front(self):
        if not self.head:
            print("Nothing to delete")
        else:
            self.head = self.head.next
        self.count -= 1
        self.display()

    def delete_at_end(self):
        self.tail = self.head
        if self.count == 0:
            print("Nothing to delete")
        elif self.count == 1:
            self. head = self.tail = None
        else:
            for _ in range(self.count - 2):
                self.tail = self.tail.next
            self.tail.next = None
        self.count -= 1
        self.display()

    def search(self, val):
        new_list = self.head
        z = 0
        for p in range(self.count):
            if new_list.data == val:
                print(f'{val} found at position:{p+1}')
                z = 1
                break
            new_list = new_list.next
        if z == 0:
            print(f'{val} not found in the list')
        self.display()

    def insert_at_index(self, val, indx):
        new_node = Node(val)
        if indx > self.count+1:
            print(f"Insertion of {val} not poosible(index out of bounds)")
        elif indx == 1:
            self.insert_at_front(val)
        elif indx == self.count+1:
            self.insert_at_end(val)
        else:
            new_head = self.head
            for _ in range(indx-2):
                self.head = self.head.next
            new_list2 = self.head.next
            self.head.next = new_node
            new_node.next = new_list2
            self.head = new_head
            self.count += 1
        self.display()

    def delete_at_index(self, indx):
        new_head = self.head
        if indx > self.count:
            print("Can't delete (Array index out of bounds)")
        elif indx == 1:
            self.delete_at_front()
        elif indx == self.count:
            self.delete_at_end()
        else:
            for _ in range(indx-2):
                self.head = self.head.next
            self.head.next = self.head.next.next
            self.head = new_head
            self.count -= 1
            self.display()


sll = Single_linked_list()
n = int(input("Enter the number of initial nodes in linked list:"))
for i in range(n):
    k = input(f'Enter value ({i + 1}):')
    sll.insert_at_end(k)
while True:
    print("Enter \'1\' to insert at front\nEnter \'2\' to insert at end\nEnter \'3\' to display the list\nEnter \'4\' "
          "to delete node at front\nEnter \'5\' to delete node at end\nEnter \'6\' to find count nodes\nEnter \'7\' "
          "to search a value\nEnter \'8\' to insert at an index\nEnter \'9\' to delete a node at an index\nEnter "
          "\'0\' to Exit")
    m = int(input("Enter a number related to operation:"))
    if (m != 1) and (m != 2) and (m != 3) and (m != 0) and (m != 4) and (m != 5) and (m != 6) and (m != 7) and (m != 8) and (m != 9):
        m = int(input("Enter a number(0,1,2,3) only:"))
    if m == 1:
        a = input("Enter value to insert at front:")
        sll.insert_at_front(a)
    if m == 2:
        a = input("Enter value to insert at end:")
        sll.insert_at_end(a)
    if m == 3:
        sll.display()
    if m == 4:
        sll.delete_at_front()
    if m == 5:
        sll.delete_at_end()
    if m == 6:
        print(f'Number of node in the list are:{sll.count}')
    if m == 7:
        search_element = input("Enter the value to search in the list:")
        sll.search(search_element)
    if m == 8:
        value = input("Enter the value to be inserted:")
        index = int(input("Enter at which position to insert:"))
        sll.insert_at_index(value, index)
    if m == 9:
        index = int(input("Enter the position of the node to be deleted:"))
        sll.delete_at_index(index)
    if m == 0:
        sll.display()
        break
