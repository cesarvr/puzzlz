d = open('./p.txt').read()
h = ["zero","one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def calibrate(l):
    first = -1
    last = -1 
    if not l:
        return 0

    for t in range(len(h)):
        l = l.replace(h[t], h[t][0]+str(t)+h[t][-1])

    for d in l:
        if d.isdigit() and first == -1:
            first = last = d 
            continue

        if d.isdigit():
            last = d
    return int(first+last)        
            


r = 0
for l in d.split('\n'):
    n = calibrate(l)
    r += n
print('r: ', r)

    


