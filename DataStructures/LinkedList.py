'''n1= Node(10)
n2= Node(20)

head=n1
n1.next= n2
n2.next= None
print(head.data)
aise krna coding wise galat nai hai but linked list mai we can not make reference to each node, hume sbko head
ke through hi access krna hota hai. so better is this...
'''

class Node:
    def __init__(self,data):
        self.data=data
        self.next= None
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def generate_LinkedList(self,input_list):
        for i in input_list:
            if self.head is None:
                self.head = Node(i)
                self.tail = self.head
            else:
                self.tail.next = Node(i) #connecting
                self.tail = self.tail.next #moving tail to the last element of the linked list


    def print_LinkedList(self):
        temp=self.head
        while temp is not None:
            print((temp.data), end="")
            temp= temp.next
        print()
    def appendToList(self,data):
        if self.head is None:
            self.head = Node(data)
            self.tail = Node(data)
        else:
            self.tail.next=Node(data)
            self.tail = self.tail.next


l = LinkedList()
input_list=[1,2,3,4,5]
l.generate_LinkedList(input_list)
l.print_LinkedList()
l.appendToList(6)
l.print_LinkedList()
