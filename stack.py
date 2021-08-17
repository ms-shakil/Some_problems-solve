class Stack:
    def __init__(self):
        self.item = []

    def Push (self,value):
        self.item.append(value)

    def Pop(self):
        if self.item == []:
            print("This list is empty.")
        else:
            self.item.pop()
My_stack = Stack()

My_stack.Push("Shakil")
My_stack.Push("main")
My_stack.Pop()
My_stack.Pop()
My_stack.Pop()
print(My_stack.item)
