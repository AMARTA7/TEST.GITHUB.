"""
CIRCULAR QUEUE: A circular queue is the extended version of a regular queue where the last element 
is connected to the first element. Thus forming a circle-like structure.

The circular queue solves the major limitation of the normal queue. In a normal queue, after a bit 
of insertion and deletion, there will be non-usable empty space.

How Circular Queue Works:
Circular Queue works by the process of circular increment i.e. when we try to increment the pointer 
and we reach the end of the queue, we start from the beginning of the queue.
    
    Here, the circular increment is performed by modulo division with the queue size. That is:
        ### if REAR + 1 == 5 (overflow!), REAR = (REAR + 1)%5 = 0 (start of queue) ###

* Circular Queue Operations:
    
    The circular queue work as follows:
        1. two pointers 'FRONT' and 'REAR'
        2. 'FRONT' track the first element of the queue
        3. 'REAR' track the last elements of the queue
        4. initially, set value of 'FRONT' and 'REAR' to -1.

** Enqueue Operation:
    1. check if the queue is full
    2. for the first element, set value of 'FRONT' to 0
    3. circularly increase the 'REAR' index by 1 (i.e. if the rear reaches the end, next it would be at the start of the queue)
    4. add the new element in the position pointed to by 'REAR'

** Dequeue Operation:
    1. check if the queue is empty
    2. return the value pointed by 'FRONT'
    3. circularly increase the 'FRONT' index by 1
    4. for the last element, reset the values of 'FRONT' and 'REAR' to -1

    ## However, the check for full queue has a new additional case:
        Case 1: 'FRONT' = 0 && 'REAR' == (SIZE - 1)
        Case 2: 'FRONT' = ('REAR' + 1)

        # The second case(Case 2) happens when 'REAR' starts from 0 due to circular increment and when its value is 
        just 1 less than 'FRONT', the queue is full.
"""


# Q1: Circular Queue implementation in Python.

class MyCircularQueue():

    # Initialize the Queue
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = [None] * capacity
        self.head = self.tail = -1

    # Insert an element into the circular queue
    def enqueue(self, data):

        if ((self.tail + 1) % self.capacity == self.head):
            print("The circular queue is full\n")

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = data
        else:
            # For increase (self.tail + 1)
            self.tail = (self.tail + 1) % self.capacity
            self.queue[self.tail] = data

    # Delete an element from the circular queue
    def dequeue(self):
        if (self.head == -1):
            print("The circular queue is empty\n")
        
        # If Queue contain only one element.
        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return temp

        else:
            temp = self.queue[self.head]
            # For increase (self.head + 1)
            self.head = (self.head + 1) % self.capacity
            return temp

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

        else:
            for i in range(self.head, self.capacity):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()


# MyCircularQueue object will be instantiated and called as such:
obj = MyCircularQueue(5)

obj.enqueue(1)
obj.enqueue(2)
obj.enqueue(3)
obj.enqueue(4)
obj.enqueue(5)
print("Initial queue")
obj.printCQueue()

obj.dequeue()
print("After removing an element from the queue")
obj.printCQueue()


"""
Applications of Circular Queue:
    1. CPU scheduling
    2. Memory management
    3. Traffic Management
"""