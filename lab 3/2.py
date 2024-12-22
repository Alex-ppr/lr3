import random
def gen_random(num_count, begin, end):
    for i in range(num_count):
        if i < (num_count-1):
            print(f"{random.randint(begin, end)},", end = " ")
        else:
            print(f"{random.randint(begin, end)}.")
    pass

gen_random(5, 1, 3)