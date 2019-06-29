class Node:
    def __init__(self,data):
        self.data=data
        self.next= None

'''n1= Node(10)
n2= Node(20)

head=n1
n1.next= n2
n2.next= None
print(head.data)
aise krna coding wise galat nai hai but linked list mai we can not make reference to each node, hume sbko head
ke through hi access krna hota hai. so better is this...
'''
head = Node(2)
head.next = Node(1)

print(head.data)
print(head.next.data)
