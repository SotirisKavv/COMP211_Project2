receipts = {}


def parse_into_list(file):
    res, temp = [],[]
    for l in file:
        if l[0] == '-':
            res.append(temp)
            temp = []
        else:
            temp.append(l)
    return res


def merge(receipts, afm, dictionary):
    if afm in receipts.keys():
        for key in dictionary.keys():
            if key in receipts[afm].keys():
                receipts[afm][key][0] += dictionary[key][0]
                receipts[afm][key][1] += dictionary[key][1]
            else:
                receipts[afm][key] = dictionary[key]
    else:
        receipts[afm] = dictionary


def readFile(filename):

    file = open(filename, encoding='utf-8')
    file.readline()
    helper = parse_into_list(file)
    #print(helper)

    for receipt in helper:
        temp = {}
        if 'ΑΦΜ' in receipt[0] and len(receipt[0].split()[1])==10 and 'ΣΥΝΟΛΟ' in receipt[-1]:
            total = 0
            try:
                afm = int(receipt[0].split()[1])
            except (NameError, ValueError):
                afm = ''
            if afm != '':
                for i in range(1, len(receipt)-1):
                    product = receipt[i].split()
                    key = product[0].upper()[:-1]
                    if round(int(product[1])*float(product[2]), 2) == float(product[3]) and key != '':
                        if key in temp.keys():
                            temp[key][0] += int(product[1])
                            temp[key][1] += float(product[3])
                        else:
                            temp[key] = [int(product[1]), float(product[3])]
                        total += float(product[3])
                    else:
                        temp = {}
                        total = 0
                        break
                    #print(temp)
                if round(total, 2) == round(float(receipt[-1].split()[1]), 2):
                    merge(receipts, afm, temp)


def print_statistics_for_product(product):
    for afm in sorted(receipts.keys()):
        if product.upper() in receipts[afm].keys():
            print(str(afm)+' '+'{0:.2f}'.format(round(receipts[afm][product.upper()][1],2)))


def print_statistics_for_afm(afm):
    for product in sorted(receipts[afm].keys()):
        print(product+' '+'{0:.2f}'.format(round(receipts[afm][product.upper()][1],2)))


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
        try:
            print_statistics_for_product(input("Give preference:\t"))
        except KeyError:
            pass
    elif answer == 3:
        try:
            print_statistics_for_afm(int(input("Give preference:\t")))
        except KeyError:
            pass
    elif answer == 4:
        break
    else:
        pass
    print("\n")
    print(receipts)