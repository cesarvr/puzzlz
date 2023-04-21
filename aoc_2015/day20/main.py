def naive_get_gift_for_house(_house):
    gifts_total = 1
    for h in range(2, _house):
        if _house % h == 0:
            gifts_total += h

    return gifts_total * 10

def get_gifts_for_house_solution_1(_house, target=0):
    tail = _house
    gift_total = 0
    start = 1
    gift_factors = 0

    while tail > start:
        if _house % start == 0:
            tail = _house / start

            if tail > start:
                gift_total = gift_total + tail

            gift_total = gift_total + start
            gift_factors += start
        start+=1

        if start > 8 and gift_factors < 36:
           return 0

    return int(gift_total * 10)

def get_gifts_for_house_solution_2(_house, target_score):
    tail = _house
    gift_total = 0
    start = 1
    gift_factors = 0

    discard = []
    prime=0

    while tail > start:
        if _house % start == 0:
            tail = _house / start

            if tail * 50 <= _house:
                discard.append(tail)

            if tail * 50 >= _house and tail > start:
                gift_total = gift_total + tail

            if  start * 50 >= _house:
                gift_total = gift_total + start
                gift_factors += start
            else:
                discard.append(start)
        else:
            prime+=1

        if (10 < start < 15) and prime > 5:
            return 0

        start+=1

    return int(gift_total * 11)
def find_best_house(gift_target, getGiftForHouseFn):
    _house = 1
    while True:
        _gifts = getGiftForHouseFn(_house, gift_target)
        if _gifts >= gift_target:
            return _house

        if _house % 1000000 == 0:
            print("1 Million")

        _house += 1

    return -1


def factors50(h):
    r = []
    for n in range(1, h):
        if h % n == 0 and n*50 >= h:
            r.append(n)

    r.append(h)
    return r
def factors(h):
    r = []

    for n in range(1, h):
        if h % n == 0:
            r.append(n)

    r.append(h)
    return r

def test1(_house, expected_res):
    _best = find_best_house(_house)
    status = "Pass" if _best==expected_res else "Fail"
    print("Best house after house: ", _house, " =>", _best, " =>", status)
    print("gifts on house target: ", get_gifts_for_house_solution_1(_house))
    print("gifts on best house: ", get_gifts_for_house_solution_1(_best))



P = 29000000
best_house = find_best_house(P, get_gifts_for_house_solution_1)
print("solution 1: ", best_house)
best_house_solution_2 = find_best_house(P, get_gifts_for_house_solution_2)
print("solution 2: ", best_house_solution_2)
