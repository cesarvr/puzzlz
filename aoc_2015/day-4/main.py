import hashlib
import time

input = "ckczppom"
f1 = b"abcdef"
f2 = b"609043"


def time_this_func(fn):
    start = time.time()
    fn()
    end = time.time()
    print("time it took: ", end - start)


def check_zeroes(intake, zeroes_length=5):
    intake = str(intake)

    for n in range(zeroes_length):
        if intake[n] != "0":
            return False

    return True


def solving_puzzle(len=5):
    for i in range(1000000000):
        input_in_bytes = str.encode(input + str(i))
        result = hashlib.md5(input_in_bytes).hexdigest()
        r = check_zeroes(result, len)

        if r:
            print("correct response: ", str(input_in_bytes))
            break


time_this_func(lambda: solving_puzzle(5))
time_this_func(lambda: solving_puzzle(6))

