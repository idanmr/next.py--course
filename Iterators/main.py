import functools
from IDiterator import *


def check_id_valid(id_number):
    id_str = str(id_number)

    if len(id_str) != 9:
        return False

    # Step 1: Multiply each digit by 1 or 2 based on its position
    mul = [(int(id_str[i]) * (1 if i % 2 == 0 else 2)) for i in range(9)]

    # Step 2: If any number is greater than 9, sum its digits
    digit_sum = [x if x < 10 else x % 10 + x // 10 for x in mul]

    # Step 3: Sum all the digits
    total_sum = functools.reduce(lambda x, y: x + y, digit_sum)

    # Step 4: Check if the total sum is divisible by 10
    return total_sum % 10 == 0


def id_generator(id_number):
    while id_number < 999999999:
        id_number += 1
        if check_id_valid(id_number):
            yield id_number
    raise StopIteration()


class IDiterator:
    def __init__(self, start_id=0):
        self.id = start_id

    def _iter_(self):
        return self

    def __next__(self):
        while self.id < 999999999:
            self.id += 1
            if check_id_valid(self.id):
                return self.id
        raise StopIteration()


def main():
    print(check_id_valid(123456790))
    user_id = int(input("enter you id"))
    gen_it = input("Generator or Iterator? (gen/it)?")
    if gen_it == "it":
        id_iterator = IDiterator(user_id)
        for i in range(10):
            print(id_iterator.__next__())
    else:
        id_gen = id_generator(user_id)
        for _ in range(10):
            print(next(id_gen))



if __name__ == "__main__":
    main()
