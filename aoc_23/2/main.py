r = {'red': 12, 'green': 13, 'blue':14}

TEST ="""Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

def is_valid(num, color): 
    #print('num: ', num, ' color: ', color, '  -> ', r[color], ' => ', num<r[color])
    return num <= r[color]
    

PUZZLE_INPUT = open('./p.txt').read()

def S1(P):
    total = 0
    total_s2 = 0
    for l in P.split('\n'):
        if not l:
            continue
        slots = l.split(':')
        game_id = int(str(slots[0].split(' ')[1].replace(':', '')))
        sets = slots[1].split(';') 
        
        #print("game id: ", game_id)
        #print('sets: ', sets)

        rgb = {'red':-1, 'blue':-1, 'green': -1}
        
        valid = True 
        for cset in sets: 
            colors = cset.split(',')
            #print('colors: ', colors) 
            for color in colors:
                c = color.split(' ')
                cvalue = int(c[1])
                cname = c[2].strip()
                if not is_valid(cvalue, cname):   
                    valid = False 

                rgb[cname] = rgb[cname] if rgb[cname] > cvalue else cvalue          

        total_s2 += (rgb['red'] * rgb['green'] * rgb['blue'])
        print('line: ', l, ' valid: ', valid, ' rgb: ', rgb, '  -> ', (rgb['red'] * rgb['green'] * rgb['blue']))
        if valid:
            total += game_id

            

    print('final score: ', total, ' section 2: ', total_s2)
    return total
S1(PUZZLE_INPUT)

