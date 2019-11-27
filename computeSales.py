receipts = {}

def parse_into_list(file):
    res, temp = [],[]
    for l in file:
        if l[0] == '-':
            res.append(temp)
            temp = []
        else:
            temp.append(l)
    #print(res)
    return res


def readFile(filename):

    file = open(filename, encoding='utf-8')
    file.readline()
    helper = parse_into_list(file)
    #print(helper)

    for receipt in helper:
        temp = {}
        if 'ΑΦΜ' in receipt[0] and len(receipt[0].split()[1])==10 and 'ΣΥΝΟΛΟ' in receipt[-1]:
            total = 0
            for i in range(1, len(receipt)-1):
                product = receipt[i].split()
                key = product[0].upper()
                if round(int(product[1])*float(product[2]) == float(product[3])):
                    if key in temp.keys():
                        temp[key][0] += int(product[1])
                        temp[key][2] += float(product[3])
                    else:
                        temp[key] = [int(product[1]), float(product[2]), float(product[3])]
                    total += float(product[3])
                    print(temp)
                else:
                    temp = {}
                    total = 0
                    break
                
        


while True:
    try:
        answer = int(input("Give your preference: (1: read new input file, 2: print statistics for a specific product, 3: print statistics for a specific AFM, 4: exit the program):\t"))
    except (TypeError, ValueError):
        answer = -1
    
    if answer == 1:
        try:
            readFile(str(input("File Name:\t")))
        except FileNotFoundError:
            pass
    elif answer == 2:
        pass
    elif answer == 3:
        pass
    elif answer == 4:
        break
    else:
        pass
    print("\n")
    print(receipts)