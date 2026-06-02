t1 = [0, 2, 7, 0]
t2 = '4	10	4	1	8	4	9	14	5	1	14	15	0	15	3	5'
def serialize(blk):
    b = map(str, blk)
    return '-'.join(b)

def find_max_and_index(blk):
    m = -1
    ix = -1
    for i in range(len(blk)):
        if blk[i] > m:
            m = blk[i]
            ix = i 
    return ix, m


def redistribute(blk, ix):
    start_index = (ix + 1) % len(blk)
    candidate = blk[ix]
    blk[ix] = 0
    for i in range(candidate):
        blk[start_index] += 1
        start_index = (start_index + 1) % len(blk)

        #8512 wrong
        #12425 wrong
    return blk, -1


def solution1(block):
    patterns = [serialize(block)]
    steps = 0
    print('p: ', find_max_and_index(block))
    print('firm: ', serialize(block))
    while True:
        steps += 1
        ix, mx = find_max_and_index(block)
        block, blk_r = redistribute(block, ix)
        firm = serialize(block)
        print('firm: ', firm, ' ->', blk_r, ' ', len(block)-1)
        if firm not in patterns:
            patterns.append(firm)
        else:
            return steps, patterns.index(firm), len(patterns)

            break

    return steps





t2 = t2.split('\t')
t2 = list(map(int, t2))
steps = solution1(t2)
print('solution 1: ', steps)