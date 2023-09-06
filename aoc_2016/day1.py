class GridTaxi:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.orientation = {'x': 0, 'y':1}

    #
    #  start R2, R2, R2, R2
    #  R2 =>    x:1, y:0  
    #  R2 =>    x:0, y:-1 
    #  R2 =>    x:-1, y:0  
    #  R2 =>    x:0, y:1

    def rotate_right(self):
        tx = self.orientation['y']  
        ty = self.orientation['x'] * -1 

        self.orientation['x'] = tx
        self.orientation['y'] = ty

        return self

    #
    #  start L2, L2, L2, L2
    #  L2 =>    x:-1, y:0  
    #  L2 =>    x:0, y:-1 
    #  L2 =>    x:1, y:0  
    #  L2 =>    x:0, y:-1

    def rotate_left(self):
        tx = (self.orientation['y'] * -1)  
        ty = (self.orientation['x']) 
        self.orientation['y'] = ty 
        self.orientation['x'] = tx 

        return self


    def len(self):
        return abs(self.x) + abs(self.y)

    def rotate(self, direction):
        if direction == 'R':
            self.rotate_right() 

        if direction == 'L': 
            self.rotate_left()

    def accel(self, times):
        dx = self.orientation['x']
        dy = self.orientation['y']
        #print(f'dx {dx}, dy {dy}')

        self.x = self.x + (dx*times)
        self.y = self.y + (dy*times)
        

    def move(self, direction, times): 
        self.rotate(direction)
        self.accel(times)
    

def solution_1(_in):
    tokens = _in.replace(' ', '').split(',')
    taxi = GridTaxi()

    for token in tokens:
        direction = token[0]
        steps = int(token[1:])

        taxi.move(direction, steps)

    return taxi.len()


class DB:
    def __init__(self):
        self.db = {} 

    def collision(self, x,y): 
        _hash = f'x{x},y{y}' 
        #print('hash: ', _hash)

        if _hash in self.db: 
            return True
        else: 
            self.db[_hash] = '#'
            return False
       
def solution_2(_in):
    tokens = _in.replace(' ', '').split(',')
    taxi = GridTaxi()
    db = DB()

    for token in tokens:
        direction = token[0]
        steps = int(token[1:])
        taxi.rotate(direction)

        for step in range(1, steps+1):
            
            taxi.accel(1)
            collided = db.collision(taxi.x, taxi.y)
            #print(f'taxi.x {taxi.x}, taxi.y {taxi.y}, step: {step}')

            if collided: 
                print(f'collision site x: {taxi.x} y: {taxi.y}, blocks from origin: {taxi.len()}')
                return taxi.len()

    return -1




def testing():
    input1 = 'R2, L3'
    in2 = 'R2, R2, R2'
    in3 = 'R5, L5, R5, R3'

    st1 = solution_1(input1)
    st2 = solution_1(in2)
    st3 = solution_1(in3)

    print(f'solution t1: {st1}')
    print(f'solution t2: {st2}, expected 2, result: {st2 == 2}')
    print(f'solution t3: {st3}, expected 12, result: {st3 == 12}')

def testing_2():
    test_input = 'R8, R4, R4, R8'
    test = solution_2(test_input)
    print(f'test -> {test}')

    


day1 = 'R5, L2, L1, R1, R3, R3, L3, R3, R4, L2, R4, L4, R4, R3, L2, L1, L1, R2, R4, R4, L4, R3, L2, R1, L4, R1, R3, L5, L4, L5, R3, L3, L1, L1, R4, R2, R2, L1, L4, R191, R5, L2, R46, R3, L1, R74, L2, R2, R187, R3, R4, R1, L4, L4, L2, R4, L5, R4, R3, L2, L1, R3, R3, R3, R1, R1, L4, R4, R1, R5, R2, R1, R3, L4, L2, L2, R1, L3, R1, R3, L5, L3, R5, R3, R4, L1, R3, R2, R1, R2, L4, L1, L1, R3, L3, R4, L2, L4, L5, L5, L4, R2, R5, L4, R4, L2, R3, L4, L3, L5, R5, L4, L2, R3, R5, R5, L1, L4, R3, L1, R2, L5, L1, R4, L1, R5, R1, L4, L4, L4, R4, R3, L5, R1, L3, R4, R3, L2, L1, R1, R2, R2, R2, L1, L1, L2, L5, L3, L1'


def solution1(day1_input):
    solution = solution_1(day1_input)
    print(f'solution: {solution}, expected solution 287, solved: {287 == solution}')


def solution2(day1_input): 
    solution = solution_2(day1_input)
    return -1


solution1(day1)
solution2(day1)















