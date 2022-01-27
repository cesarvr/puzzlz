liters = None
with open('input.txt') as file:
    liters = file.readlines()

liters = list(map(lambda n: int(n.rstrip('\n')), liters))


def total_sum(num_set):
    total = 0
    for n in num_set:
        total += n
    return total


# def find_combinations(liters_selection, target_score, index=0):
# [1,2,3,4,5,6,1] with limit 7
# [1,2,3,1] = 7
# [1,2,4] = 7
# [1,2,5] = 8
# [1,2,6] = 9
# [1,3,4] = 8
# [1,5,1] = 7
# [1,6] = 7

def removeUntilLimit(base, limit):
    while base[:-1] not in limit:
        base.pop()
    return base

store = 0

def find_combinations(candidates, target_score, arr = [], level = 0):
    combinations = 0
    minimum_blocks = 1000

    if len(candidates) == 0:
        return [0, minimum_blocks]

    arr = arr if arr else [candidates.pop(0)]
    local = candidates.copy()
    while len(local) > 0:

        arr.append(local.pop(0))
        total = total_sum(arr)

        if total == target_score:
            print('arr ->', arr, ' ->', total, ' ->', len(arr))

            if len(arr) == 4:
                global store
                store += 1

        if total == target_score:
            combinations += 1
            if minimum_blocks > len(arr):
                minimum_blocks = len(arr)

        if total < target_score:
            ret = find_combinations(local, target_score, arr, level + 1)
            combinations += ret[0]
            minimum_blocks = ret[1] if ret[1] < minimum_blocks else minimum_blocks
        arr.pop()

    if level == 0:
        ret = find_combinations(candidates, target_score)
        combinations += ret[0]
        minimum_blocks = ret[1] if ret[1] < minimum_blocks else minimum_blocks


    return [combinations, minimum_blocks]


print('liters ->', liters)
print('combinations ->', find_combinations(liters, 150))
print('store->', store)