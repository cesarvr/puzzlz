class DocV2:
    def __init__(self):
        doc = """
xx1xx
x234x
56789
xABCx
xxDxx
"""

        self.doc = list(map(lambda n: n.replace(' ', '') , doc.split('\n')))
        self.doc = list(filter(lambda n: n != "",self.doc))
        self.y = 2
        self.x = 0

    def nav(self, pos = None):
        y = self.y 
        x = self.x 

        if pos == 'U':
            y = y - 1

        if pos == 'D': 
            y = y + 1 

        if pos == 'L':
            x = x - 1

        if pos == 'R':
            x = x + 1
        

        if y >= 0 and y <= len(self.doc) and self.doc[y][x] != 'x':
            self.y = y

        if x >= 0 and x <= len(self.doc[0]) and self.doc[y][x] != 'x':
            self.x = x
    
        return self.doc[self.y][self.x]


    def locate(self, positions = ''):
        curr = ''
        if positions == '':
            return self.nav(None)
        for position in positions:
            curr = self.nav(position)

        return curr



        

        


    def print(self):
        print(f'self.doc {self.doc}')




class Doc:
    def __init__(self):
        doc = """1 2 3
            4 5 6
            7 8 9"""

        self.doc = list(map(lambda n: n.replace(' ', '') , doc.split('\n')))
        self.y = 1
        self.x = 1

    def nav(self, pos = None):
        if pos == 'U' and self.y >= 1:
            self.y = self.y - 1

        if pos == 'D' and self.y <= 1:
            self.y = self.y + 1
        
        if pos == 'L' and self.x >= 1:
            self.x = self.x - 1

        if pos == 'R' and self.x <= 1:
            self.x = self.x + 1

        print(f'wtf => y:{self.y}, x:{self.x} ')
        print(f'self.doc {self.doc[self.y]}')
        return self.doc[self.y][self.x] 

    def locate(self, positions = ''):
        curr = ''
        if positions == '':
            return self.nav(None)
        for position in positions:
            curr = self.nav(position)

        return curr










    
def testing():
    doc = Doc()
    curr = doc.nav()
    doc.nav('U')
    doc.nav('L')
    curr = doc.nav('L')
    print(f'doc => {curr}')

    curr = doc.locate('RRDDD')
    print(f'current should be equal to 9 => {curr} -> {curr == "9"}')
    
    curr = doc.locate('LURDL')
    print(f'current should be equal to 8 => {curr} -> {curr == "8"}')

    curr = doc.locate('UUUUD')
    print(f'current should be equal to 5 => {curr} -> {curr == "5"}')




def solution1():
    _input = """LRRLLLRDRURUDLRDDURULRULLDLRRLRLDULUDDDDLLRRLDUUDULDRURRLDULRRULDLRDUDLRLLLULDUURRRRURURULURRULRURDLULURDRDURDRLRRUUDRULLLLLDRULDDLLRDLURRLDUURDLRLUDLDUDLURLRLDRLUDUULRRRUUULLRDURUDRUDRDRLLDLDDDLDLRRULDUUDULRUDDRLLURDDRLDDUDLLLLULRDDUDDUUULRULUULRLLDULUDLLLLURRLDLUDLDDLDRLRRDRDUDDDLLLLLRRLLRLUDLULLDLDDRRUDDRLRDDURRDULLLURLRDLRRLRDLDURLDDULLLDRRURDULUDUDLLLDDDLLRLDDDLLRRLLURUULULDDDUDULUUURRUUDLDULULDRDDLURURDLDLULDUDUDDDDD
RUURUDRDUULRDDLRLLLULLDDUDRDURDLRUULLLLUDUDRRUDUULRRUUDDURDDDLLLLRRUURULULLUDDLRDUDULRURRDRDLDLDUULUULUDDLUDRLULRUDRDDDLRRUUDRRLULUULDULDDLRLURDRLURRRRULDDRLDLLLRULLDURRLUDULDRDUDRLRLULRURDDRLUDLRURDDRDULUDLDLLLDRLRUDLLLLLDUDRDUURUDDUDLDLDUDLLDLRRDLULLURLDDUDDRDUDLDDUULDRLURRDLDLLUUDLDLURRLDRDDLLDLRLULUDRDLLLDRLRLLLDRUULUDLLURDLLUURUDURDDRDRDDUDDRRLLUULRRDRULRURRULLDDDUDULDDRULRLDURLUDULDLDDDLRULLULULUDLDDRDLRDRDLDULRRLRLRLLLLLDDDRDDULRDULRRLDLUDDDDLUDRLLDLURDLRDLDRDRDURRDUDULLLDLUDLDRLRRDDDRRLRLLULDRLRLLLLDUUURDLLULLUDDRLULRDLDLDURRRUURDUDRDLLLLLLDDDURLDULDRLLDUDRULRRDLDUDRLLUUUDULURRUR
URRRLRLLDDDRRLDLDLUDRDRDLDUDDDLDRRDRLDULRRDRRDUDRRUUDUUUDLLUURLRDRRURRRRUDRLLLLRRDULRDDRUDLRLUDURRLRLDDRRLUULURLURURUDRULDUUDLULUURRRDDLRDLUDRDLDDDLRUDURRLLRDDRDRLRLLRLRUUDRRLDLUDRURUULDUURDRUULDLLDRDLRDUUDLRLRRLUDRRUULRDDRDLDDULRRRURLRDDRLLLRDRLURDLDRUULDRRRLURURUUUULULRURULRLDDDDLULRLRULDUDDULRUULRRRRRLRLRUDDURLDRRDDULLUULLDLUDDDUURLRRLDULUUDDULDDUULLLRUDLLLRDDDLUUURLDUDRLLLDRRLDDLUDLLDLRRRLDDRUULULUURDDLUR
UULDRLUULURDRLDULURLUDULDRRDULULUDLLDURRRURDRLRLLRLDDLURRDLUUDLULRDULDRDLULULULDDLURULLULUDDRRULULULRDULRUURRRUDLRLURDRURDRRUDLDDUURDUUDLULDUDDLUUURURLRRDLULURDURRRURURDUURDRRURRDDULRULRRDRRDRUUUUULRLUUUDUUULLRRDRDULRDDULDRRULRLDLLULUUULUUDRDUUUDLLULDDRRDULUURRDUULLUUDRLLDUDLLLURURLUDDLRURRDRLDDURLDLLUURLDUURULLLRURURLULLLUURUUULLDLRDLUDDRRDDUUDLRURDDDRURUURURRRDLUDRLUULDUDLRUUDRLDRRDLDLDLRUDDDDRRDLDDDLLDLULLRUDDUDDDLDDUURLDUDLRDRURULDULULUDRRDLLRURDULDDRRDLUURUUULULRURDUUDLULLURUDDRLDDUDURRDURRUURLDLLDDUUDLLUURDRULLRRUUURRLLDRRDLURRURDULDDDDRDD
LLRUDRUUDUDLRDRDRRLRDRRUDRDURURRLDDDDLRDURDLRRUDRLLRDDUULRULURRRLRULDUURLRURLRLDUDLLDULULDUUURLRURUDDDDRDDLLURDLDRRUDRLDULLRULULLRURRLLURDLLLRRRRDRULRUDUDUDULUURUUURDDLDRDRUUURLDRULDUDULRLRLULLDURRRRURRRDRULULUDLULDDRLRRULLDURUDDUULRUUURDRRLULRRDLDUDURUUUUUURRUUULURDUUDLLUURDLULUDDLUUULLDURLDRRDDLRRRDRLLDRRLUDRLLLDRUULDUDRDDRDRRRLUDUDRRRLDRLRURDLRULRDUUDRRLLRLUUUUURRURLURDRRUURDRRLULUDULRLLURDLLULDDDLRDULLLUDRLURDDLRURLLRDRDULULDDRDDLDDRUUURDUUUDURRLRDUDLRRLRRRDUULDRDUDRLDLRULDL"""

    i = _input.split("\n")
    digit = ""

    print(f"input: {len(i)}")
    doc = Doc()

    for line in i:
        digit = digit + doc.locate(line)


    print("code: ", digit)
        




def testingv2():
    d = DocV2()

    d.print()



testingv2()
