class Ingredient:
    def __init__(self, ing, tblspn=0):
        self.ingredient_list = ing
        self.tablespoon = int(tblspn)

    def __repr__(self):
        return str([self.ingredient_list, self.tablespoon])

    def stole(self, n):
        if self.tablespoon < n or self.tablespoon == 1:
            return 0
        else:
            self.tablespoon -= n
            return n

    def add(self, n):
        if self.tablespoon + n < 100:
            self.tablespoon += n
            return True
        else:
            return False


def find_permutations(arr, current_position, permutations=[]):
    tail = len(arr) - 1
    local = arr.copy()
    local[current_position] -= 1
    local[current_position + 1] += 1

    permutations.append(local.copy())

    if current_position + 1 < tail:
        find_permutations(local, current_position + 1)

    if local[current_position] > 1 and current_position != tail:
        find_permutations(local, current_position)

    return permutations


def back_track(actors):
    tablespoon_limit = 100
    permutations = [0] * actors

    permutations[0] = tablespoon_limit
    return find_permutations(permutations, 0)


def remove_calories(ingredients):
    ret = []
    for ingredient in ingredients:
        ret.append(ingredient.copy()[:-1])
    return ret


def pack_ingredients_into_pair(ingredients):
    pack = []
    for ingredient in ingredients:
        for index in range(len(ingredient)):
            if index >= len(pack):
                pack.append([])
            pack[index].append(ingredient[index])

    print('packed result: ', pack)
    return pack


def compute_calories(calories_vec, permutation):
    total_calories = 0

    for index in range(len(calories_vec)):
        total_calories += calories_vec[index] * permutation[index]

    return total_calories

def find_best_score(pck_ingredients, permutations_list):
    max_score = -1
    max_calories_score = -1

    ingredient_calories = pck_ingredients[-1]
    pck_ingredients = pck_ingredients[:-1]

    for permutation in permutations_list:
        total = 1


        for pack in pck_ingredients:
            acc = 0
            for index in range(len(pack)):
                acc += pack[index] * permutation[index]
            total *= acc if acc > 0 else 0

            total_calories = compute_calories(ingredient_calories, permutation)

        #57600000
        if(total_calories == 500 and max_calories_score < total):
            max_calories_score = total

        if max_score < total:
            max_score = total


    return [max_score, max_calories_score]


lines = ''
with open('input.txt') as f:
    lines = f.readlines()

rows = []


def is_int(n):
    return n.lstrip('-').rstrip(',').isdigit()


for line in lines:
    l = list(filter(is_int, line.split()))
    li = list(map(lambda n: int(n.rstrip(',')), l))
    rows.append(li)

#ingredients = remove_calories(rows)
packed_ingredients = pack_ingredients_into_pair(rows)

permutations = back_track(len(rows))
best_score = find_best_score(packed_ingredients, permutations)

print('best score is: ', best_score[0], ' is correct answer -> ', best_score[0] == 13882464)
print('best calorie score @500 ->: ', best_score[1])



# print('permutations are valid: ', len(permutations) == 156848, permutations)
