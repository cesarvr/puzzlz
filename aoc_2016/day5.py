import hashlib


    

def sol1(_id):
    cnt = 0
    acc = ''
    acc_s2 = [-1,-1,-1,-1,-1,-1,-1,-1] 
    digits = 0
    digits_s2 = 0
    

    while True:
        i =  _id + str(cnt)
        hex_hash = hashlib.md5(bytes(i,'utf-8')).hexdigest()
        if hex_hash[0:5] == '00000' and digits < 8: 
            #print('we got the one at: ', cnt , ' -> ', hex_hash, ' char: ', hex_hash[5])
            acc = acc + hex_hash[5]
            digits = digits + 1

        if hex_hash[0:5] == '00000': 
            i = hex_hash[5]
            if i.isdigit() and int(i) < len(acc_s2):
                acc_s2[int(i)] = hex_hash[6] if acc_s2[int(i)] == -1 else acc_s2[int(i)]
                
                print('we got the one at: ', cnt , ' -> ', hex_hash, ' => ', acc_s2)

                n = 0 
                for d in acc_s2:
                    n = n + 1
                    if d == -1:
                        break
                digits_s2 = n
                print('len => ', n)


        if digits >= 8 and digits_s2 >= 8:
            nn = map(lambda t: str(t), acc_s2)
            return acc, ''.join(acc_s2)

        cnt = cnt + 1




print('solution 1 and 2: ', sol1('abc'))
print('solution 1 and 2: ', sol1('abbhdwsy'))

