"""
You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.

Function Description

Complete the insertNodeAtTail function in the editor below.

insertNodeAtTail has the following parameters:

SinglyLinkedListNode pointer head: a reference to the head of a list
int data: the data value for the node to insert
Returns

SinglyLinkedListNode pointer: reference to the head of the modified linked list
Input Format

The first line contains an integer , the number of elements in the linked list.
The next  lines contain an integer each, the value that needs to be inserted at tail.
"""

class SinglyLinkedListNode:  ## create node
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:   ## initialising head
    def __init__(self):
        self.head = None

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)  ##create new node with data and pointer
    if not head:   ## checking if the head is empty ??
        head = new_node   # if empty, then just add new node to head and return head
        return head
    
    # if linked list is not empty
    current = head   ## current is assigned to the first node in linked list
    while current.next:   ## this loop will help us to traverse to last node from the first node
        current = current.next     ## for the lase node .next (pointer) will be 'None'.
    
    ## assign new node to the pointer of the last node --> pointer is also a node (which is the next node)
    current.next = new_node
    
    return head  ## return head