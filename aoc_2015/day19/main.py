def get_replacements(raw_file):
    ret = {}
    for line in raw_file:
        packet = line.split()

        if line == "" or len(packet) < 2:
            continue

        k = packet[0]
        v = packet[2]

        if k not in ret:
            ret[k] = []

        ret[k].append(v)

    return ret


def read_target(raw_file):
    return raw_file[-1]


def solution_one(_target, _replacements={}):
    ret = {}

    for replacement in _replacements.keys():
        size = len(replacement)
        pos = _target.find(replacement, 0)
        candidates = _replacements[replacement]

        while pos != -1:
            for r in candidates:
                tmp = list(_target)
                tmp[pos:(pos + size)] = r
                ret["".join(tmp)] = 1

            pos = _target.find(replacement, pos + size)

    return ret.keys()


def get_progress(word1, word2):
    size = min(len(word1), len(word2))
    progress = 0
    for index in range(size):
        if word1[index] == word2[index]:
            progress += 1
        else:
            return progress
    return progress


def get_max_progress(_mutations, _target):
    max_progress = -1
    ret = ""

    for mutation in _mutations:
        before = max_progress
        max_progress = max(max_progress, get_progress(_target, mutation))

        if before != max_progress:
            ret = mutation

    return max_progress, ret


def solution_two(_target, _replacements):
    seeds = _replacements['e']
    del _replacements['e']
    cycles = 2
    cache = {}

    while True:
        for seed in seeds:
            mutations = solution_one(seed, _replacements)

            for mutation in mutations:
                cache[mutation] = 1

            if _target in cache:
                print("response: ", _target)
                return cycles

            progress, candidate_word = get_max_progress(mutations, _target)
            if progress >= len(_target):
                print("partial response: ", _target)
                print("partial candidate_word: ", candidate_word)
                return cycles

        seeds = list(cache.keys())
        cache.clear()
        cycles += 1

    return cycles


data = open("test3.txt", "r").read().split("\n")
replacements = get_replacements(data)
target = read_target(data)


print("data -> ", replacements)
print("target -> ", target)

sol1 = solution_one(target, replacements)

print("solution 1 -> ", len(sol1))
print("solution 2 -> ", solution_two(target, replacements))