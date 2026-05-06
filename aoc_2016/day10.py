input1 = '''
value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2
'''

class E:
    def __init__(self, name):
        self.name = name
        self.values = []
class Link:
    provider = None
    links = []

    def add(self, children=None):
        self.links = children



def parse_line(line):
    line = line.strip(' ')
    entity = None

    if 'value' == line[0]:
        name = f'{line[-2]}_{line[-1]}'
        entity = E(name)
        entity.values.append(int(line[1]))

    if 'bot' == line[0]:
        name = f'{line[0]}_{line[1]}'
        provider_entity = E(name)
        low_entity = E(f'{line[5]}_{line[6]}')
        high_entity = E(f'{line[-2]}_{line[-1]}')




    return entity

def parse(_input):
    lines = _input.split('\n')
    lines = [line  for line in lines if line]
    print('lines: ', lines)
    lines = list(map(lambda line: parse_line(line),lines))

def solve(_input):

    return True

solve(_input=input1)