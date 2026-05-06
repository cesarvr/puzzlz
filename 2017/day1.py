'''

--- Day 1: Inverse Captcha ---


'''


t1 = '1122'


def solve_1(_input):
    for index, character in enumerate(_input):
        if (index + 1) >= len(_input):
            print('iter from the beginning: ', _input[index], ' -> ', _input[0])
        else:
            print('iter: ', _input[index], ' -> ', _input[index+1])


solve_1(t1)
    
