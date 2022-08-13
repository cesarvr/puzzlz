import time


def read_puzzle_input(filename):
    lines = open(filename, 'r').read().split('\n')
    return [lines[0:-2], lines.pop()]


def turn_into_dict(parts):
    dict = {}
    for part in parts:
        p = part.split('=>')
        key = p[0].strip()
        val = p[1].strip()
        store = [] if key not in dict else dict[key]
        store.append(val)
        dict[key] = store
    return dict


def solving_part_one(parts, initial_molecule):
    mutations = []
    for part in parts:
        _molecule = list(initial_molecule)
        for index in range(len(_molecule)):
            ini = index
            end = index + len(part)
            section = ''.join(_molecule[ini:end])
            if part == section:
                for _replacement in parts[part]:
                    copy = list(initial_molecule)
                    copy[ini:end] = _replacement
                    mutations.append(copy)

    _m = []
    for m in mutations:
        _molecule = ''.join(m)
        if _molecule not in _m:
            _m.append(_molecule)

    return _m


def count_str(line, desired_molecule):
    n = 0
    minimum = min(len(line), len(desired_molecule))
    for index in range(minimum):
        if line[index] == desired_molecule[index]:
            n = n + 1
        else:
            return n

    return n


def remove_duplicates(mutations):
    _m = []
    for m in mutations:
        if m not in _m:
            _m.append(m)
    return _m


def progress(m, desired_molecule, k=''):
    cnt = 0
    word = ''
    for tokens in m:
        n = count_str(k + tokens, desired_molecule)

        if n > cnt:
            cnt = n
            word = k+tokens
    return [cnt, word]


def minimum_progress(m, desired_molecule, k=''):
    cnt = 1000
    word = ''
    for tokens in m:
        n = count_str(k+tokens, desired_molecule)
        if cnt > n:
            cnt = n
            word = k+tokens
    return [cnt, word]


def is_partially_correct(k='', m=[], desired_molecule=''):
    for tokens in m:
        tokens = tokens if k == '' else k + tokens
        if desired_molecule in tokens:
            print('is_partially_correct: chosen one: ', tokens)
            return True
    return False


def is_correct(m, desired_molecule):
    for tokens in m:
        if tokens == desired_molecule:
            return True
    return False


def cleanup(_m, desired_molecule, k=''):
    [max_progress, _] = progress(_m, desired_molecule, k)

    if len(_m) > 2000:
        x = list(filter(lambda n: count_str(k+n, desired_molecule) > round(max_progress * .86), _m))
        x = remove_duplicates(x)
        return x

    return _m


def reduce_size(_m, desired_molecule, key=''):
    [minimum, word] = minimum_progress(_m, desired_molecule, key)

    slice = minimum - len(key)
    if slice > 10:
        print('minimum progress ->', word, ' len:', minimum)
        key = key + _m[0][:slice]

        for index in range(len(_m)):
            _m[index] = _m[index][slice:]

    return [key, _m]


def solving_part_two(parts, desired_molecule):
    seeds = parts['e']
    del parts['e']
    _m = seeds
    k = ''
    _steps = 0
    while True:
        _steps = _steps + 1
        t = []
        start = time.time()
        for _molecule in _m:
            m = solving_part_one(parts, _molecule)
            t = t + m

        if is_partially_correct(k, _m, desired_molecule):
            return _steps

        end = time.time()

        _m = t
        print('compute time: ', end - start)
        _m = cleanup(_m, desired_molecule, k)
        [k, _m] = reduce_size(_m, desired_molecule, k)
        print('progress: ', progress(_m, desired_molecule, k), ' size: ', len(_m))


[replacements, molecule] = read_puzzle_input('p4.txt')
print('replacements: ', replacements, ' \nmolecule:', molecule)
sol = solving_part_one(turn_into_dict(replacements), molecule)

# print('solution 1: ', len(sol))

sol = solving_part_one(turn_into_dict(replacements), molecule)

i1 = time.time()
steps = solving_part_two(turn_into_dict(replacements), molecule)

print('Solution puzzle 2: ', steps, ' time: ', time.time() - i1)
