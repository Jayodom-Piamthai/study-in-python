class stack:
    def __init__(self,stacker = [],top = -1):
        self.stacker = stacker
        self.top = top
        
    def push(self,num):
        self.stacker.append(num)
        self.top += 1
        print(f"push {num} successful")
        
    def pop(self):
        num = self.stacker[self.top]
        self.stacker.pop(self.top)
        self.top -= 1
        print(f"pop {num} successful")
        
    def display(self):
        print(self.stacker)
stack = stack()
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.display()

stack.pop()
stack.pop()
stack.pop()
stack.pop()
stack.display()
