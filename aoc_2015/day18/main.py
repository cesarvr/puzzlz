raw_grid = ''

with open('puzzle.txt') as f:
    raw_grid = f.readlines()


def int_matrix(raw_str_grid):
    matrix = []
    for row in raw_str_grid:
        matrix.append(list(row.split()[0]))
    return matrix


def dbg(mtx):
    for row in mtx:
        print(''.join(row))


def is_lighted(mtx, x, y):
    if mtx[y][x] == '#':
        return 1
    else:
        return 0


def find_lights_nearby(mtx, pos):
    x = pos['x']
    y = pos['y']

    lights = 0

    left = 1
    right = 1
    top = 1
    bottom = 1

    if x == 0:
        left = 0

    if x == len(mtx[0]) - 1:
        right = 0

    if y == 0:
        top = 0

    if y == len(mtx) - 1:
        bottom = 0

    # Check Top
    if top > 0 and left > 0:
        lights += is_lighted(mtx, x - left, y - top)

    if top > 0:
        lights += is_lighted(mtx, x, y - top)

    if top > 0 and right > 0:
        lights += is_lighted(mtx, x + right, y - top)

    if right > 0:
        lights += is_lighted(mtx, x + right, y)

    if bottom > 0 and right > 0:
        lights += is_lighted(mtx, x + right, y + bottom)

    if bottom > 0:
        lights += is_lighted(mtx, x, y + bottom)

    if bottom > 0 and left > 0:
        lights += is_lighted(mtx, x - left, y + bottom)

    if left > 0:
        lights += is_lighted(mtx, x - left, y)

    return lights


def is_on(mtx, x, y):
    return mtx[y][x] == '#'


def turn_switch(mtx, x, y, state=True):
    if state:
        mtx[y][x] = '#'
    else:
        mtx[y][x] = '.'


def deep_copy(mtx):
    tmp = []
    for rows in mtx:
        tmp.append(rows.copy())
    return tmp


def count_active_lights(mtx):
    total = 0
    for row in mtx:
        total += ''.join(row).count('#')
    return total


def set_corners(mtx):
    tmp = deep_copy(mtx)
    tmp[0][0] = '#'
    tmp[0][-1] = '#'
    tmp[-1][0] = '#'
    tmp[-1][-1] = '#'

    return tmp


def is_corner_light(mtx, x,y):
    if x == 0 and y == 0:
        return True

    if x == len(mtx[0]) - 1 and y == 0:
        return True

    if x == 0 and y == len(mtx) - 1:
        return True

    if x == len(mtx[0]) - 1 and y == len(mtx) - 1:
        return True
    return False


def transitions(mtx, steps, corner_case = False):
    ret_mtx = deep_copy(mtx.copy())

    for step in range(steps):
        for y in range(len(mtx)):
            for x in range(len(mtx[y])):
                lights_nearby = find_lights_nearby(ret_mtx, {'x': x, 'y': y})

                if not is_on(ret_mtx, x, y) and lights_nearby == 3:
                    turn_switch(mtx, x, y)
                    continue

                if is_on(ret_mtx, x, y) and (lights_nearby == 2 or lights_nearby == 3):
                    continue
                else:

                    if corner_case and is_corner_light(mtx, x, y):
                        continue

                    turn_switch(mtx, x, y, False)
                    continue

        print('step: ', step + 1)
        dbg(mtx)
        print('----')
        ret_mtx = deep_copy(mtx)

    return mtx


_mtx = int_matrix(raw_grid)

print('raw_grid: ', raw_grid, _mtx)
dbg(_mtx)

print('neighbours for 0,0 ', find_lights_nearby(_mtx, {'x': 0, 'y': 0}) == 1)
print('neighbours for 3,0 ', find_lights_nearby(_mtx, {'x': 3, 'y': 0}) == 2)


#final_mm = transitions(_mtx, 100)
#print('active lights: ', count_active_lights(final_mm))


mtx_with_corners = set_corners(_mtx)
final_corners_mm = transitions(mtx_with_corners, 100, True)
print('active lights: ', count_active_lights(final_corners_mm))


