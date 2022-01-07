#Algorithm - Linked list #1

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self,data):
        self.head = Node(data)

    def add(self,data):
        if self.head=="":
            self.head=Node(data)
        else:
            node=self.head
            while node.next:
                node=node.next
            node.next=Node(data)
    def desc(self):
        node=self.head
        while node:
            print(node.data)
            node=node.next

    def delete(self,data):
        if self.head=="":
            print("Error")
            return
        if self.head.data==data:
            temp=self.head
            self.head=self.head.next
            del temp
        else:
            node=self.head
            while node.next:
                if node.next.data == data:
                    temp=node.next
                    node.next=node.next.next
                else:
                    node=node.next

    def search(self,data):
        if self.head=="":
            print("Error")
            return
        node = self.head
        if self.head.data==data:
            return node.data
        else:
            while node.next:
                if node.next.data==data:
                    return node.data
                node=node.next


linkedlist1=NodeMgmt(0)
linkedlist1.desc()

for data in range(1,10):
    linkedlist1.add(data)
linkedlist1.desc()
linkedlist1.delete(4)
print(linkedlist1.search(3))