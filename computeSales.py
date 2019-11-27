receipts = {}

def parse_into_list(file):
    res, temp = [],[]
    for l in file:
        if l[0] == '-':
            res.append(temp)
            temp = []
        else:
            temp.append(l)
    print(res)
    return res


def readFile(filename):

    file = open(filename, encoding='utf-8')
    file.readline()
    helper = parse_into_list(file)
    print(helper)


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