class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = None
        self.head.next = self.tail


    def traverse(self):
        result = []
        curr = self.head
        while curr.next:
            curr = curr.next
            result.append(curr.data)
        return result


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        i = 0
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAfter(self, prev, newNode):
        newNode.next = prev.next
        if prev.next is None:
            self.tail = newNode
        prev.next = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos != 1 and pos == self.nodeCount + 1:
            prev = self.tail
        else:
            prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


    def popAfter(self, prev):
        # if prev.next == None:
        #     return None
        #
        # curr = prev.next
        # if curr.next == None:
        #     prev.next = None
        #     self.tail = prev
        # else:
        #     prev.next = curr.next
        #
        # self.nodeCount -= 1
        # return curr.data

        preNode = self.getAt(prev)

        if preNode == None:
            return None

        currNode = preNode.next
        if currNode.next == None:
            preNode.next = None
            self.tail = preNode

        else:
            preNode.next = currNode.next

        self.nodeCount -= 1
        return currNode.data


    def popAt(self, pos):
        if not(1 <= pos and pos <= self.nodeCount):
            raise IndexError
        return self.popAfter(pos-1)
        # return self.popAfter(self.getAt(pos-1))


def solution(x):
    return 0