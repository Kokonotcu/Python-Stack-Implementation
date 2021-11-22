max_size=5
stack=[]
stackIndexNoter=-1



def main():
    push(2)
    push(3)
    push(4)
    push(5)
    push(6)
    push(7)
    peek()
    print(isFull())
    print(isEmpty())
    
    

def push(value):
    global stackIndexNoter
    global stack
    global max_size
    if  stackIndexNoter!= (max_size-1):
         stack.append(value)
         stackIndexNoter += 1
    else:
         print("The stack is full!")

def pop():
    global stackIndexNoter
    global stack
    if stackIndexNoter == -1:
        print("this stack is already empty!")
    else:
        del stack[-1]
        stackIndexNoter -=1
        
def peek():
    global stack
    print(stack[-1])


def isFull():
    global stackIndexNoter
    global max_size
    if stackIndexNoter == (max_size-1):
        return True
    else:
        return False

def isEmpty():
    global stackIndexNoter
    if stackIndexNoter == -1:
        return True
    else:
        return False


main()



