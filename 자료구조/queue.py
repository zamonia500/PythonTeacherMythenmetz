QUEUE_SIZE = 4

front = 987654321
rear = 987654321


def queue_Create():
    global front
    front = -1
    global rear
    rear = -1

    return [0] * QUEUE_SIZE

def enQueue(Q, data):
    global rear
    if rear + 1 == QUEUE_SIZE:
        raise OverflowError()
    else:
        rear += 1
        Q[rear] = data


def deQueue(Q):
    global front
    global rear
    if rear == front:
        raise OverflowError()
    else:
        front += 1
        result = Q[front]
        Q[front] = 0
        return result


def queue_isEmpty(Q):
    pass

def queue_isFull(Q):
    pass

def peek(Q):
    pass

queue = queue_Create()
