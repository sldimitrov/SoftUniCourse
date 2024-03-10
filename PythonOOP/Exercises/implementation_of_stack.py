
class Stack:
    def __init__(self):
        self.stack = []

    def empty(self):
        if self.stack:
            return False
        return True

    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop_end(self, idx=-1):
        if idx != -1:
            try:
                popped_element = self.stack.pop(idx)
                return popped_element
            except IndexError:
                return f"Invalid index given."
        popped_element = self.stack.pop()
        return popped_element

    def __str__(self):
        return str(self.stack)


# Initialise a new instance of the Stack class
stack_object = Stack()

# Test all methods within our Class that imitates the behaviour of Stack
stack_object.push(1)
stack_object.push(2)
stack_object.push(3)
stack_object.push(4)
print(f"\nAfter adding elements {stack_object}")

print(f"Popped element : {stack_object.pop_end(2)}")

print(f"After popping element {stack_object}")

print(f"Is our stack empty? {stack_object.empty()}")

print(f"The size of our stack: {stack_object.size()}")
