import random


def gen_random(qty: int, begin: int, end: int):
    for _ in range(qty):
        yield random.randint(begin, end)


if __name__ == '__main__':
    print(str(list(gen_random(5, 1, 3)))[1:-1])
    print(str(list(gen_random(3, 1, 10)))[1:-1])
