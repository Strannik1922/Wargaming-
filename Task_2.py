class MyQueueSized:
    def __init__(self, max_size):
        self.queue = [None] * max_size
        self.max_n = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def push(self, x):
        if self.size < self.max_n:
            self.queue[self.tail] = x
            self.tail = (self.tail + 1) % self.max_n
            self.size += 1
            return 'OK'
        else:
            return 'error'

    def pop(self):
        if self.is_empty():
            return None
        x = self.queue[self.head]
        self.queue[self.head] = None
        self.head = (self.head + 1) % self.max_n
        self.size -= 1
        return x

    def peek(self):
        if self.is_empty():
            return None
        return self.queue[self.head]


n = int(input())
max_size = int(input())
q = MyQueueSized(max_size)
result = []
for i in range(n):
    command = input().split()
    if command[0] == 'push':
        q.push(command[1])
        if q.push(command[1]) == 'error':
            result.append(q.push(command[1]))
    if command[0] == 'pop':
        result.append(q.pop())
    if command[0] == 'peek':
        result.append(q.peek())
    if command[0] == 'size':
        if command[0] == 'size':
            result.append(q.size)
for x in result:
    print(x)


class Deque:
    """
    Клас Deque для реализации работы дека.
    Фун-я is_empty проверяет наличие данных.
    Фун-я push_back добовляет элемент в конец дека.
    Фун-я push_front добавляет элемент в начало списка.
    Фун-я pop_back извлекает элемент с конца дека.
    Фун-я pop_front извлекает элемент с начала дека.
    """
    def __init__(self, max_size: int):
        self.__deque = [None] * max_size
        self.__max_elem = max_size
        self.__head = 0
        self.__tail = 0
        self.__size = 0

    def is_empty(self):
        return self.__size == 0

    def push_back(self, value):
        if self.__size != self.__max_elem:
            self.__deque[self.__tail] = value
            self.__tail = (self.__tail + 1) % self.__max_elem
            self.__size += 1
        else:
            raise OverflowError

    def push_front(self, value):
        if self.__size != self.__max_elem:
            self.__deque[self.__head - 1] = value
            self.__head = (self.__head - 1) % self.__max_elem
            self.__size += 1
        else:
            raise OverflowError

    def pop_back(self):
        if self.is_empty():
            raise IndexError
        x = self.__deque[self.__tail - 1]
        self.__deque[self.__tail - 1] = None
        self.__tail = (self.__tail - 1) % self.__max_elem
        self.__size -= 1
        return x

    def pop_front(self):
        if self.is_empty():
            raise IndexError
        x = self.__deque[self.__head]
        self.__deque[self.__head] = None
        self.__head = (self.__head + 1) % self.__max_elem
        self.__size -= 1
        return x


def main():
    deque = Deque(deque_size)
    for i in range(command_count):
        operation, *value = input().split()
        if value:
            try:
                result = getattr(deque, operation)(*value)
                if result is not None:
                    print(result)
            except OverflowError:
                print('error')
        else:
            try:
                result = getattr(deque, operation)()
                if result is not None:
                    print(result)
            except IndexError:
                print('error')


if __name__ == '__main__':
    command_count = int(input())
    deque_size = int(input())
    main()