max_size=5 #You can edit this max size, this corresponds to arr[max_size] in c++
stack=[]
stackIndexNoter=-1  # Our initial index count is -1 thus when we insert a first value, its index becomes 0



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
    global stackIndexNoter  # We are saying that we use the stackIndexNoter we defined previously
    global stack
    global max_size
    
    if  stackIndexNoter < (max_size-1):  # if stackIndexNoter becomes (max_size -1) then it is full 
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
    print(stack[-1]) #Print the last value of this stack


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



