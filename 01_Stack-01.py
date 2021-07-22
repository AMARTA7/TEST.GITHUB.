"""
STACK: A stack is a linear data structure that follows the principle of 
Last In First Out (LIFO). This means the last element inserted inside the 
stack is removed first.
-------------------------------------------------------------------------------------------------

*** Working of Stack Data Structure:

    1. A pointer called 'TOP' is used to keep track of the top element in the stack.

    2. When initializing the stack, we set its value to -1 so that we can check if 
    the stack is empty by comparing 'TOP == -1'.

    3. On pushing an element, we increase the value of 'TOP' and place the new element 
    in the position pointed to by 'TOP'.

    4. On popping an element, we return the element pointed to by 'TOP' and reduce its value.

    5. Before pushing, we check if the stack is already full.

    6. Before popping, we check if the stack is already empty.
"""


# Q1: Stack implementation in python

# Creating a stack
def create_stack():
    stack=[]
    return stack

# Check for empty stack
def check_empty(stack):
    return len(stack)==0

# Adding items into the stack
def push(stack, item):
    stack.append(item)
    print("push iten is :"+item)

# Removing an element from the stack
def pop(stack):
    if (check_empty(stack)):
        return "stack is empty"
    return stack.pop()

stack=create_stack()
push(stack,str(1))
push(stack,str(2))
push(stack,str(3))
push(stack,str(4))
print("popped item: " + pop(stack))
print("stack after popping an element: " + str(stack))



"""
Applications of Stack Data Structure:

    Although stack is a simple data structure to implement, it is very powerful. 
    The most common uses of a stack are:

        1. To reverse a word : Put all the letters in a stack and pop them out. 
        Because of the LIFO order of stack, you will get the letters in reverse order.

        2. In compilers : Compilers use the stack to calculate the value of expressions 
        like "2 + 4 / 5 * (7 - 9)" by converting the expression to prefix or postfix form.

        3. In browsers : The back button in a browser saves all the URLs you have visited 
        previously in a stack. Each time you visit a new page, it is added on top of the stack. 
        When you press the back button, the current URL is removed from the stack, and the 
        previous URL is accessed.
"""