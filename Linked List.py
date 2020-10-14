# 1 Design Linked List
'''
Find the predecessor of the node to insert, if the node is to be inserted at head, its predecessor is a sentinel head
If the node is to be inserted at tail, its predecessor is the last node
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None
class MyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        if index<0 or index >= self.size:
            return -1
        curr = self.head
        for i in range(index+1):
            curr = curr.next
        return curr.val
    def addAtHead(self,val):
        self.addAtIndex(0,val)
    def addAtTail(self,val):
        self.addAtIndex(self.size,val)
    def addAtIndex(self,index,val):
        if index > self.size:
            return
        if index<0:
            index = 0
        self.size += 1
        pred = self.head
        for i in range(index):
            pred = pred.next
        to_add = ListNode(val)

        to_add.next = pred.next
        pred.next = to_add
    def deleteAtIndex(self,index):
        if index < 0 or index > self.size:
            return
        self.size -= 1
        pred = self.head
        for i in range(index):
            pred = pred.next

        pred.next = pred.next.next