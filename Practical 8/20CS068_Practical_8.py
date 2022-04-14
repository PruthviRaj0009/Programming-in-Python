'''
Write a Program in Python to implement a Stack Data Structure using Class and Objects, with push, pop, and traversal method.
'''
# Pruthvi Raj
# 20CS068

# Stack implementation with class and object using pyhton.
class Stack:

    # Initializing stack.
    def __init__(self):
        self.stack = []

    # Function to check if the stack is empty or not.
    def check_for_empty(self):
        return self.stack == []

    # Function push to push the element
    def push(self, value):
        self.stack.append(value)

    # Function pop to delete the top most element
    def pop(self):
        if self.check_for_empty():
            print("Stack is Empty!!\n")
        else:
            print("\npopped item: ", self.stack.pop())

    # Function to traverse the stack.
    def traversal(self):
        print("\nStack traversal: ")
        for i in reversed(range(0, len(self.stack))):
            print("data = ", self.stack[i], "index = ", i)


# Creating an object of stack.
v = Stack()

# Giving menu_no to the user.
while True:
    print("\nStack\n1. push\n2. pop\n3. traversal\n4. isEmpty\n5. Quit.")
    print("Enter from below option :")
    menu_no = int(input())

    if menu_no == 1:
        print("Enter element : ")
        element = int(input())
        v.push(element)
    elif menu_no == 2:
        v.pop()
    elif menu_no == 3:
        v.traversal()
    elif menu_no == 4:
        status = v.check_for_empty()
        print(f'Empty Status : {status}\n')
    elif menu_no == 5:
        break
    else:
        print("Enter valid menu_no!!\n")
        continue
