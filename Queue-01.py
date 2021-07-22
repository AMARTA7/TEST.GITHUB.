"""
A queue is a useful data structure in programming. It is similar to the ticket queue 
outside a cinema hall, where the first person entering the queue is the first person 
who gets the ticket.
-----------------------------------------------------------------------------------------------------

Queue follows the First In First Out (FIFO) rule - the item that goes in first is the 
item that comes out first.

***Basic Operations of Queue:
    A queue is an object (an abstract data structure - ADT) that allows the following operations:

        1. Enqueue: Add an element to the end of the queue
        2. Dequeue: Remove an element from the front of the queue
        3. IsEmpty: Check if the queue is empty
        4. IsFull: Check if the queue is full
        5. Peek: Get the value of the front of the queue without removing it

* Working of Queue:
    Queue operations work as follows:
        two pointers 'FRONT' and 'REAR'
        'FRONT' track the first element of the queue
        'REAR' track the last element of the queue
        initially, set value of 'FRONT' and 'REAR' to -1

* Enqueue Operation:
    Check if the queue is full:
    for the first element, set the value of 'FRONT' to 0
    increase the 'REAR' index by 1
    add the new element in the position pointed to by 'REAR'

* Dequeue Operation:
    Check if the queue is empty
    return the value pointed by 'FRONT'
    increase the 'FRONT' index by 1
    for the last element, reset the values of 'FRONT' and 'REAR' to -1        
"""


# Q1: Queue implementation in Python
class Queue:
    def __init__(self):
        self.queue=[]

    # Add an element
    def enqueue(self,item):
        self.queue.append(item)

    # Remove an element
    def dequeue(self):
        if len(self.queue)<0:
            return "Empty Queue."
        return self.queue.pop(0)

    # Display the queue
    def display(self):
        print(f"Queue Element Is: {self.queue}")

    #Size of the Queue
    def size(self):
        print(f"Size of the Queue is: {len(self.queue)}")

q=Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)

q.display()
q.dequeue()

print("After removing an element...")
q.display()
q.size()


"""
Applications of Queue:
    1. CPU scheduling, Disk Scheduling

    2. When data is transferred asynchronously between two processes. The queue is used 
    for synchronization. For example: IO Buffers, pipes, file IO, etc

    3. Handling of interrupts in real-time systems.

    4. Call Center phone systems use Queues to hold people calling them in order.
"""