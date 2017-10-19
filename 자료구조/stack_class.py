class Stack:

    def create(self, size=5):
        self.STACK_SIZE = size
        self.top = -1
        self.stack = [0] * self.STACK_SIZE
        print('stack created!')

    def push(self, data):
        if self.is_full():
            raise OverflowError('stack_isfull')
        else:
            self.top += 1
            self.stack[self.top] = data
            print('push! stack :', self.stack)

    def pop(self):
        if self.is_empty():
            raise OverflowError('stack is_empty')
        else:
            result = self.stack[self.top]
            self.stack[self.top] = 0
            self.top -= 1
            print('pop! pop data :', result, '\nstack :', self.stack)
            return result

    def destroy(self):
        del self.stack
        print('stack destroyed')

    def peek(self):
        if self.is_empty():
            raise OverflowError('peek: stack is empty')
        else:
            return self.stack[self.top]

    def is_empty(self):
        if self.top == -1:
            return True
        else :
            return False

    def is_full(self):
        if self.top + 1 == self.STACK_SIZE:
            return True
        else:
            return False


stack = Stack()
stack.create()

for i in range(ord('a'), ord('e')+1):  # stack에 a,b,c,e,d 를 push 한다.
    stack.push(chr(i))

for i in range(3):  # pop을 세 번 호출한다.
    stack.pop()
