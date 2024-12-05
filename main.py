def decimalToBase(origin: int, base: int = 2):
    i = 0
    target = 0
    result_list = []
    result = ''
    largest_exponent=0
    while base**largest_exponent < origin:
        largest_exponent+=1
    while target<origin:
        for m in range(largest_exponent, -1, -1):
            for j in range(base):
                target += (base**m)
                if target > origin:
                    target -= (base**m)
                    break
            if j >= 10:
                alphabet = 'abcdefghijklmnopqrstuvxyz'
                char = alphabet[j-10]
                result_list.append(char)
            else:
                result_list.append(j)
            print(target, i,j,m, result_list)
        i+=1
    try:
        result_list.remove(0)
    except:
        pass
    for k in result_list:
        result += str(k)
    return result

def baseToDecimal(origin:int, base:int=2):
    result=0
    for iterator, number in enumerate(str(origin)[::-1]):
        result += int(number)*(base**iterator)
        print(number, iterator)
    return result
def baseToBase(origin, obase, tbase):
    dorigin = baseToDecimal(origin, obase)
    print(dorigin)
    return decimalToBase(dorigin, tbase)

while True:
    base  = int(input('base>'))
    tbase = int(input('target base>'))
    user = int(input('input>'))
    print(baseToBase(user,base,tbase))