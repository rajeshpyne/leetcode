"""
Given a linked list, 
swap every two adjacent nodes and return its head. 
You must solve the problem without modifying the values in the list's nodes 
(i.e., only nodes themselves may be changed.)


Example 1:

Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:

Input: head = []
Output: []

Example 3:

Input: head = [1]
Output: [1]

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100
"""

class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert(self, data):
        newNode = Node(data)
        if self.head:
            current = self.head
            while(current.next):
                current = current.next
            current.next = newNode
        else:
            self.head = newNode

    def swapPairs(self):
        current = self.head

        if current is None:
            return

        while(current and current.next):
            if current.val != current.next.val:
                current.val, current.next.val = current.next.val, current.val
            current = current.next.next
    
    def printLL(self):
        current = self.head
        lst = []
        while(current):
            lst.append(current.val)
            current = current.next
        return lst


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(3)
    ll.insert(4)
    ll.insert(5)
    ll.insert(6)
    d = ll.printLL()
    print(d)
    ll.swapPairElement()
    print(ll.printLL())

    

