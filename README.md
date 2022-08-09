# Тестовое задание на позицию Programming intern в компании Wargaming Санкт-Петербург

### Задание 1
Сравниваем варианты:

1.
```
def isEven(value): 
    return value % 2 == 0
```

2.
```
def is_even(num):
    return num & 1 == 0
```

Плюс второй реализации в том, что мы изначально используем более быструю операцию - побитовое "и".

### Задание 2
На языке Python, написать минимум по 2 класса реализовывающих циклический буфер FIFO.

Первый класс MyQueueSized представляет собой простую реализацию массива FIFO:
```
class MyQueueSized:
```

Второй класс Deque представляет собой кольцевой буфер с возможностью перезаписи существующих данных:
```
Deque:
```

### Задание 3

На языке Python реализовать функцию, которая быстрее всего (по процессорным тикам) отсортирует данный ей массив чисел. Массив может быть любого размера со случайным порядком (в том числе и отсортированным). Объяснить почему вы считаете, что функция соответствует заданным критериям.

Встроенные функции сортировки во многих языках программирования используют модификации именно алгоритма быстрой сортировки, поскольку на практике она нередко работает даже быстрее сортировки слиянием.

Я сформулирую алгоритм быстрой сортировки:

```
Выбираем опорный элемент.
```

```
Делим массив на два подмассива: слева элементы меньше опорного, справа — больше, посередине — равные опорному. Этот этап часто выделяют в отдельную функцию, которую называют partition.
```

```
Применяем быструю сортировку к двум подмассивам, левому и правому.
```

```
Объединяем результат.
```

Чтобы избежать использования дополнительной памяти, нужно сделать класс Participant:

```
class Participant:
        def __init__(self, name: str, tasks: str, penalties: str) -> None:
            self.name = name
            self.tasks = int(tasks)
            self.penalties = int(penalties)
```