STACK_SIZE = 10
top = 987654321

def push(stack, data):
    global top
    if top + 1 == STACK_SIZE:
        raise OverflowError('stack_isFull')
    else:
        top += 1
        stack[top] = data


def pop(stack):
    global top
    if top == -1:
        raise OverflowError('stack_isEmpty')
    else:
        result = stack[top]
        stack[top] = 0
        top -= 1
        return result


def stack_isEmpty(stack):
    global top
    if top == -1:
        return True
    else:
        return False

def stack_isFull(stack):
    global top

stack = [0] * STACK_SIZE
top = -1
'a'
'b'
'c'
print(stack_isEmpty(stack))
push(stack, 'a')
push(stack, 'b')
push(stack, 'c')
print(stack_isEmpty(stack))
push(stack, 'd')
push(stack, 'e')
print(stack, top)

print(pop(stack))
print(pop(stack))
print(pop(stack))

print(stack, top)




def stack_peek(stack, stack_info):
    pass

