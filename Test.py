
class List:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, value):
        if self.head == None:
            self.head = List(value)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = List(value)

    def reverse(self):
        prev = None
        current = self.head
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

if __name__ == '__main__':
    l = LinkedList()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.add(7)
    l.add(8)
    l.add(9)
    l.add(10)
    l.reverse()
    current = l.head
    while current != None:
        print(current.value)
        current = current.next
