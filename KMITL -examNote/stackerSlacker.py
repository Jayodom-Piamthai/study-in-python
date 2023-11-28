stack = []
top = -1
def push(num):
    global top
    global stack
    stack.append(num)
    top += 1
    print(f"push {num} successful")
def pop():
    global top
    global stack
    if top > -1 :
        nah = stack[top]
        stack.pop(top)
        top -= 1
        print(f"pop {nah} successful")
    else :
        print(f"ERROR,stack underflow")
    
push(0)
push(1)
push(2)
push(3)
push(4)
push(5)
print(stack)

pop()
pop()
pop()
pop()
print(stack)
