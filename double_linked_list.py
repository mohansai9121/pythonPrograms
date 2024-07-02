# Implementing double linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.pre = None


class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def insert_at_front(self, val):
        node = Node(val)
        if not self.head:
            self.head = self.tail = node
        else:
            node.next = self.head
            self.head.pre = node
            self.head = node
        self.count += 1

    def insert_at_end(self, val):
        node = Node(val)
        if not self.tail:
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node
        self.count += 1

    def forward_display(self):
        if self.head and self.tail:
            new_head = self.head
            print("Forward display of elements:", end='')
            while new_head:
                print(f'{new_head.data},', end="")
                new_head = new_head.next
        else:
            print("No elements in the list to print...!")

    def backward_display(self):
        if self.head and self.tail:
            new_tail = self.tail
            print("Backward display of elements:", end='')
            while new_tail:
                print(f'{new_tail.data},', end='')
                new_tail = new_tail.pre
        else:
            print("No elements in the list to print...!")

    def search_for(self, val):
        new_head = self.head
        if self.head:
            pos1 = 0
            while self.head:
                if self.head.data == val:
                    print(f'{val} found at position\'{pos1+1}\' in forward direction')
                    print(f'{val} found at position\'{self.count-pos1}\' in backward direction')
                    break
                else:
                    pos1 += 1
                    self.head = self.head.next
            self.head = new_head
        else:
            print("List does not exist to search")

    def insert_at_position(self, position, val):
        node = Node(val)
        new_head = self.head
        if position > self.count+1:
            print("Index range out of bounds")
        elif position == 1:
            self.insert_at_front(val)
        elif position == self.count+1:
            self.insert_at_end(val)
        else:
            for a in range(position-2):
                self.head = self.head.next
            node.next = self.head.next
            self.head.next = node
            node.pre = self.head
            self.count += 1
            self.head = new_head

    def delete_at_position(self, position):
        if position > self.count:
            print("Index range out of bounds")
        elif position == 1:
            print(f"{self.head.data} deleted")
            self.head = self.head.next
            self.count -= 1
        elif position == self.count:
            print(f'{self.tail.data} deleted')
            if self.tail.pre:
                self.tail = self.tail.pre
                self.tail.next = None
            self.count -= 1
        else:
            new_node = self.head
            for a in range(position-2):
                self.head = self.head.next
            print(f'{self.head.next.data} deleted')
            self.head.next = self.head.next.next
            self.head.next.pre = self.head
            self.head = new_node
            self.count -= 1


print("Implementing Double-Linked-List")
dll = Double_linked_list()
elements = list(map(str, input("Enter initial values in list(space separated): ").split()))
for i in elements:
    dll.insert_at_end(i)
while True:
    print("\nEnter \'1\' for inserting an element at front\nEnter \'2\' for inserting at end\nEnter \'3\' for forward "
          "display of elements\nEnter \'4\' for backward display of elements\nEnter \'5\' to search for a "
          "value\nEnter \'6\' insert after an index\nEnter \'7\' to delete a node at position\nEnter \'8\' to print "
          "number of elements in the list\nEnter \'0\' to exit")
    n = int(input("Choose operation:"))
    if n == 1:
        ele = input("Enter a value:")
        dll.insert_at_front(ele)
        dll.forward_display()
    elif n == 2:
        ele = input("Enter a value:")
        dll.insert_at_end(ele)
        dll.forward_display()
    elif n == 3:
        dll.forward_display()
    elif n == 4:
        dll.backward_display()
    elif n == 0:
        break
    elif n == 5:
        ele = input("Enter the value to search in the list:")
        dll.search_for(ele)
    elif n == 6:
        ele = input("Enter the value to insert:")
        pos = int(input("Enter the position:"))
        dll.insert_at_position(pos, ele)
        dll.forward_display()
    elif n == 7:
        pos = int(input("Enter the position, to delete the node:"))
        dll.delete_at_position(pos)
        dll.forward_display()
    elif n == 8:
        print(f"Total number of elements in the list are:{dll.count}")
    else:
        print("Input wrong...!")
