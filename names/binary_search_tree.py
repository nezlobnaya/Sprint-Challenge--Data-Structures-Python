
class Node:
    def __init__(self, value=None,prev = None, next_node=None):
        self.value = value
        self.next_node = next_node
        self.prev = prev
        
    

# build a class to manage nodes
class LinkedList:
    def __init__(self, prev = None, node = None, next_node=None):
        self.head = None  # stores a node that is the begining of the list
        self.tail = None  # stores a node that is the end of the list
        self.prev = prev
        self.next_node = next_node
        self.length = 1 if node is not None else 0
    
    def __len__(self): # built in method, allows easy access
        return self.length

    def add_to_head(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to the new node
            self.head = new_node
    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail to the new node
            self.tail.next_node = new_node
            self.tail = new_node
    def remove_head(self):
        # if list is empty, do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value
    def contains(self, value):
        if self.head is None:
            return False
        # loop through each node, until we see the value, or we cannot go further
        current_node = self.head
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True
            # otherwise, go to the next node
            current_node = current_node.next_node
        return False

    def get_max(self):
        if not self.head: 
            return None
        if self.head.next_node is None:
            return self.head.value
        max_value = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value > max_value:
                max_value = current_node.value
            current_node = current_node.next_node
        return max_value

    








class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
    
    def __len__(self):
        return self.size

    def enqueue(self, value):
        self.size += 1
        return self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
    
    def len(self):
        return len(self.storage)


class Stack:# In a stack, a new element is added at one end and an element is removed from that end only. 
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()
        
    def __len__(self):
        return self.size

    def push(self, value):
        self.size += 1
        self.storage.add_to_head(value)
       

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_head()
        else:
            return None

    def len(self):
        return self.size



"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        if value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)


        



    # Return True if the tree contains the value
    # False if it does not
    # def contains(self, target):
    #     if self.value == target:
    #         return True
    #     found = False
    #     if self.value < target:
    #         if self.left is None:
    #             return False
    #         found = self.left.contains(target)
    #     if self.value >= target:
    #         if self.right is None:
    #             return False
    #         found = self.right.contains(target)
    #     return found

    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value: 
            if not self.left: 
                return False 
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

        

    # Return the maximum value found in the tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return
        else:
            self.in_order_print(node.left)
            # Traverse root
            print(node.value)
            self.in_order_print(node.right)

        
       
     
        


        
    
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # not using recursion!
        # use a queue
        queue = Queue()
        # start queue with root node
        queue.enqueue(node)
        # while loop that checks size of queue
        # until the queue is empty
        while queue.size > 0:
            # pointer variable that updates 
            # at the beginning of each loop
            current_node = queue.dequeue()
            print(current_node.value)
            if current_node.left:
                queue.enqueue(current_node.left)
            if current_node.right:
                queue.enqueue(current_node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(node)
        while stack.size > 0:
            current_node = stack.pop()
            print(current_node.value)
            if current_node.left:
                stack.push(current_node.left)
            if current_node.right:
                stack.push(current_node.right)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        if node is None:
            return
        else:
            print(node.value)
            self.pre_order_dft(node.left)
            self.pre_order_dft(node.right)
     

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node is None:
            return
        else:          
            self.post_order_dft(node.left)
            self.post_order_dft(node.right)
            print(node.value)
      
