from typing import Iterable


def fib(max_value: int):
    a, b = 0, 1

    while a <= max_value:
        print(a)
        a, b = b, a + b


def fib_list(max_value: int) -> Iterable[int]:
    a, b = 0, 1

    result = []

    while a <= max_value:
        result.append(a)
        a, b = b, a + b

    return result


def fib_gen(max_value: int) -> Iterable[int]:
    a, b = 0, 1

    while a <= max_value:
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    fib(42)

    print('-----')

    for n in fib_list(42):
        print(n)

    print('-----')

    for n in fib_gen(42):
        print(n)


names = ['Alice', 'Bob', 'Carlos', 'David', 'Eva']
filtered_names = (name for name in names if len(name) > 3)
