receipts = {}       #global dictionary where receipt 
                    #components from file are stored

#function used for parsing a file into a list of lists
#it stores temporarly the line contents as list nodes and
#when it finds a line that starts with '-', it appends it
#at the list to be returned
def parse_into_list(file):
    res, temp = [],[]
    for l in file:
        if l.count('-') == len(l)-1: #checks if line starts with '-'
            res.append(temp)
            temp = []
        else:
            temp.append(l)
    return res

#funtion to merge 2 dictionaries based on the afm/key
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

#function to read a file and store its components into a nested dictionary
#checking if a receipt fullfils the basic requirements
def readFile(filename):

    file = open(filename, encoding='utf-8')
    file.readline()
    helper = parse_into_list(file)

    for receipt in helper:
        temp = {}
        if 'ΑΦΜ' in receipt[0] and len(receipt[0].split()[1])==10 and 'ΣΥΝΟΛΟ' in receipt[-1]:
            total = 0
            try:
                afm = int(receipt[0].split()[1])
            except (NameError, ValueError): #checks if afm consists of 10 ints
                afm = ''
            if afm != '':
                afm = receipt[0].split()[1] #saves 10-digit key for merge
                for i in range(1, len(receipt)-1):
                    if len(receipt[i].split()) == 4:    #checks if line has 4 columns
                        product = receipt[i].split()
                        key = product[0].upper()[:-1]
                        if round(int(product[1])*float(product[2]), 2) == float(product[3]) and key != '': #check if key isn't empty and the calculations are right
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
                if round(total, 2) == round(float(receipt[-1].split()[1]), 2): #checks if total is correctly calculated
                    merge(receipts, afm, temp)

#function to print the total price of a product per afm
def print_statistics_for_product(product):
    for afm in sorted(receipts.keys()):
        if product.upper() in receipts[afm].keys():
            print(str(afm)+' '+'{0:.2f}'.format(round(receipts[afm][product.upper()][1],2)))

#function to print the afm's total products with their total cost
def print_statistics_for_afm(afm):
    for product in sorted(receipts[afm].keys()):
        print(product+' '+'{0:.2f}'.format(round(receipts[afm][product.upper()][1],2)))

#main part
while True:
    try:
        answer = int(input("Give your preference: (1: read new input file, 2: print statistics for a specific product, 3: print statistics for a specific AFM, 4: exit the program):\t"))
    except (TypeError, ValueError): #check if answer isn't Integer
        answer = -1
    
    if answer == 1:
        try:
            readFile(str(input("File Name:\t")))
        except FileNotFoundError:
            pass
    elif answer == 2:
        try:
            print_statistics_for_product(str(input("Give preference: ")))
        except KeyError:
            pass
    elif answer == 3:
        try:
            print_statistics_for_afm(str(input("Give preference: ")))
        except KeyError:
            pass
    elif answer == 4:
        break
    else:   #invalid input
        pass
    print("\n")