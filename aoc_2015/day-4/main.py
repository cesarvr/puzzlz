import hashlib
input = "ckczppom"
f1 = b"abcdef"
f2 = b"609043"

def check_zeroes(intake, zeroes_length=5):
    intake = str(intake)

    for n in range(zeroes_length):
        if intake[n] != "0":
            return False

    return True


def solving_puzzle(len=5):
    for i in range(1000000000):
        input_in_bytes = str.encode(input+str(i))
        result = hashlib.md5(input_in_bytes).hexdigest()
        r = check_zeroes(result, len)

        if r:
            print("correct response: ", str(input_in_bytes))
            break



solving_puzzle(5)
solving_puzzle(6)
