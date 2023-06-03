class ThreeStacks:
    def __init__(self, stack_size):
        self.stack_size = stack_size
        self.stack = [None] * (stack_size * 3)
        self.pointers = [-1, -1, -1]

    def push(self, stack_num, value):
        if self.pointers[stack_num] + 1 >= self.stack_size:
            return False
        self.pointers[stack_num] += 1
        self.stack[self.stack_index(stack_num)] = value
        return True

    def pop(self, stack_num):
        if self.pointers[stack_num] < 0:
            return None
        value = self.stack[self.stack_index(stack_num)]
        self.stack[self.stack_index(stack_num)] = None
        self.pointers[stack_num] -= 1
        return value

    def peek(self, stack_num):
        if self.pointers[stack_num] < 0:
            return None
        return self.stack[self.stack_index(stack_num)]

    def stack_index(self, stack_num):
        return stack_num * self.stack_size + self.pointers[stack_num]

stacks = ThreeStacks(5)
stacks.push(0, 1)
stacks.push(0, 2)
stacks.push(0, 3)
stacks.push(1, 4)
stacks.push(1, 5)
stacks.push(1, 6)
stacks.push(2, 7)
stacks.push(2, 8)
stacks.push(2, 9)

print(stacks.stack)
print(stacks.pop(0))
print(stacks.pop(0))
print(stacks.pop(0))
print(stacks.pop(1))
print(stacks.pop(1))
print(stacks.pop(2))
print(stacks.stack)
