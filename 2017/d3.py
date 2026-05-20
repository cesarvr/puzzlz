



class Snake:
    def __init__(self, dx, dy):
        self.directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
        self.position = -1
        self.x = dx
        self.y = dy
        self.center = (dx, dy)

    def rotate_fw(self):
        self.position = (self.position + 1) % len(self.directions)
        return self

    def rotate_bw(self):
        self.position = (self.position - 1) % len(self.directions)
        return self

    def look_ahead_bw(self):
        pos = (self.position - 1) % len(self.directions)
        return (self.x + self.directions[pos][0]), (self.y + self.directions[pos][1])

    def look_ahead_fw(self):
        pos = (self.position + 1) % len(self.directions)
        return (self.x + self.directions[pos][0]), (self.y + self.directions[pos][1])

    def move(self):
        self.x += self.directions[self.position][0]
        self.y += self.directions[self.position][1]
        return self

    def backtrack(self):
        self.position = (self.position - 1) % len(self.directions)
        return self


    def current(self):
        return self.x, self.y

class Grid:
    def __init__(self, size=10):
        self.grid = []
        for n in range(size):
            self.grid.append([None] * size)

        self.size = size
        self.center_x = size//2
        self.center_y = size//2
        self.snake = Snake(self.center_x, self.center_y)
        self.limit = 265149
    def calculate_manhattan_distance(self, x, y, center):
        return abs(x-center[0]) + abs(y-center[1])

    def dbg(self):
        for row in self.grid:
            print(''.join(el[0] if el else '.' for el in row))

    def find_the_manhattan_distance_for_the_number(self, num):
        for row in self.grid:
            for element in row:
                if element and int(element[0]) == num:
                    return element[1]
        return None

    def solve_puzzle_two(self, x, y, step):
        acc = 0


        right = (1,0)
        left = (-1, 0)
        up = (0,1)
        down = (0, -1)

        # t z b
        # f x a
        # h o p

        #x       a     b    z     t     f    h      o      p
        box = [right, up, left, left, down, down, right, right]

        if step == 1:
            self.solve_puzzle_one(x, y, 1)
            return False

        px = 0
        py = 0
        for [sx, sy] in box:
            px += sx
            py += sy
            value = self.grid[y+py][x+px]
            v = int(value[0]) if value else 0
            print('surroundings: ', v)
            acc += v

        if acc > self.limit:
            print(f'acc: {acc}!! is larger than limit: {self.limit}')
            return True

        self.solve_puzzle_one(x,y, acc)
        return False

    def solve_puzzle_one(self, x, y, step):
        self.grid[y][x] = [str(step), self.calculate_manhattan_distance(x, y, self.snake.center)]
        return True

    def run(self, steps, fn_solver=None):
        for step in range(1, steps+1):
            x, y = self.snake.current()

            should_it_end = fn_solver(x, y, step)

            if should_it_end:
                return True

            ax, ay = self.snake.look_ahead_fw()

            if self.grid[ay][ax] is None:
                self.snake.rotate_fw()

            self.snake.move()

        return True

def testing(grid, n):
    print(f"manhattan for {n}: ", grid.find_the_manhattan_distance_for_the_number(n))

def number_spiral(num):
    """Create a spiral of numbers starting from 0"""

    # grid = Grid(size=520)
    # grid.run(265149, fn_solver=grid.solve_puzzle_one)
    #
    # testing(grid, 1)
    # testing(grid, 12)
    # testing(grid, 23)
    # testing(grid, 1024)
    # testing(grid, 265149)

    grid2 = Grid(size=500)
    grid2.run(1024, fn_solver=grid2.solve_puzzle_two)
    #grid2.dbg()

    return False


number_spiral(25)