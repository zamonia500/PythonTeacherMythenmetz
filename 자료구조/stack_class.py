class Stack:

    def create(self, size=5):
        self.STACK_SIZE = size
        self.top = -1
        self.stack = [0] * self.STACK_SIZE

    def push(self, data):
        if self.is_full():
            raise OverflowError('stack_isfull')
        else:
            self.top += 1
            self.stack[self.top] = data

    def pop(self):
        if self.is_empty():
            raise OverflowError('stack is_empty')
        else:
            result = self.stack[self.top]
            self.stack[self.top] = 0
            self.top -= 1
            return result

    def destroy(self):
        del self.stack

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

    def is_valid_expr(self, expr):
        """
        
        :param expr: infix expression ex) (1+2)*(3+4)
        :return: valid expression 이면 True
                 invalid expression 이면 False를 return 한다.
        """
        for letter in expr:
            if letter == '(':
                self.push(letter)
            if letter == ')':
                self.pop()

        return self.is_empty()

    def infix_to_postfix(self, expr):
        pass

    def eval_postfix(self, postfix_expr):
        for letter in postfix_expr:
            if letter.isdigit():
                # stack에 push한다.
            if # letter가 operator 라면
                # pop 2번 후 operator에 맞게 계산
        # 1.2. letter가 operator 라면 stack에서 2개의 operand를 pop하여 계산하고 결과를 push한다
        # 2. stack에서 pop 하여 나온 결과를 return한다,
        #
        #
        #
    def cal_expr(self, expr):
        if self.is_valid_expr(expr):
            pass
        else:
            pass
        postfix_expr = self.infix_to_postfix(expr)
        result = self.eval_postfix(postfix_expr)
        return result


stack = Stack()
stack.create()


postfix = ['3', '5', '*', '6', '2', '/', '-']
result = stack.eval_postfix(postfix)