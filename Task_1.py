from timeit import Timer


def isEven(value): 
    return value % 2 == 0


def is_even(num):
    return num & 1 == 0


if __name__ == '__main__':
    value = int(input("Введите целое число: "))
    t = Timer("isEven(value)", "from __main__ import isEven, value",)
    print(t.timeit())
    print(is_even(value))
    data = int(input("Введите целое число: "))
    t = Timer("is_even(data)", "from __main__ import is_even, data",)
    print(t.timeit())
    print(is_even(data))