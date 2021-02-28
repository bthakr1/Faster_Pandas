
"""
██╗    ██╗███████╗██╗      ██████╗ ██████╗ ███╗   ███╗███████╗    ████████╗ ██████╗     ████████╗██╗  ██╗███████╗         ██╗██╗   ██╗███╗   ██╗ ██████╗ ██╗     ███████╗    ██╗██╗██╗    
██║    ██║██╔════╝██║     ██╔════╝██╔═══██╗████╗ ████║██╔════╝    ╚══██╔══╝██╔═══██╗    ╚══██╔══╝██║  ██║██╔════╝         ██║██║   ██║████╗  ██║██╔════╝ ██║     ██╔════╝    ██║██║██║    
██║ █╗ ██║█████╗  ██║     ██║     ██║   ██║██╔████╔██║█████╗         ██║   ██║   ██║       ██║   ███████║█████╗           ██║██║   ██║██╔██╗ ██║██║  ███╗██║     █████╗      ██║██║██║    
██║███╗██║██╔══╝  ██║     ██║     ██║   ██║██║╚██╔╝██║██╔══╝         ██║   ██║   ██║       ██║   ██╔══██║██╔══╝      ██   ██║██║   ██║██║╚██╗██║██║   ██║██║     ██╔══╝      ╚═╝╚═╝╚═╝    
╚███╔███╔╝███████╗███████╗╚██████╗╚██████╔╝██║ ╚═╝ ██║███████╗       ██║   ╚██████╔╝       ██║   ██║  ██║███████╗    ╚█████╔╝╚██████╔╝██║ ╚████║╚██████╔╝███████╗███████╗    ██╗██╗██╗    
 ╚══╝╚══╝ ╚══════╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚══════╝       ╚═╝    ╚═════╝        ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚════╝  ╚═════╝ ╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝╚═╝╚═╝    
                                                                                                                                                                                                                                         
"""          

# check if the number is odd or even

def evenOdd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("odd")

# Check parity

def checkParity(n):
    result = (n % 2)
    return result

# check range or not

def inRange(x,y):
    return (x < 1/3 < y)

# multuple string 3 times

def getStr(s):
    s = s[:1] + s[0] + s[1:]
    s = s[:1] + s[0] + s[1:]
    s = s[:3] + s[3] + s[3:]
    s = s[:3] + s[3] + s[3:]
    s = s[:6] + s[6] + s[6:]
    s = s[:6] + s[6] + s[6:]

    strlen = len(s)
    return [s,strlen]

# find occurence of string or character

def findOccurence(s):
    a = s.find("b")
    b = s.find("ccc")
    return [a,b]

# change casing to upper and lower both

def changeCase(s):
    upper_case = s.upper()
    lower_case = s.lower()
    return [upper_case,lower_case]


def sumList(n):
    sum = 0
    for i in range(0,len(n)):
        sum += n[i]
    return sum

def sumList1(l):
    sum = 0
    for x in l:
        sum += x
    return sum

def findMaximum(list1):
    maximum = list1[0]
    for number in list1:
        if number > maximum:
            maximum = number
    return maximum

def findMaximumValueIndex(list1):
    maximum = list1[0]
    index_value = []
    for index, value in enumerate(list1):
        if value > maximum:
            maximum = value
            index_value = list1.index(maximum)
    return [index_value,maximum]


def findMaximumValueIndex1(list1):
    maximum = list1[0]
    index = 0
    for i, value in enumerate(list1):
        if value > maximum:
            maximum = value
            index = i
    return [index,maximum]

def reverse(list1):
    return list1[::-1]

def reverse1(list1):
    length = len(list1)
    s = length

    new_list = [None]*length

    for item in list1:
        s = s - 1
        new_list[s] = item
    return new_list

def isSorted(list1):
    flag = 0
    i = 1
    while i < len(list1):
        if list1[i] < list1[i-1]:
            flag = 1
        i += 1
    
    if (not flag):
        return True
    else:
        return False

def hasDuplicates(list1):
    list2 = sorted(list1)

    flag = 0
    i = 0

    while i < len(list2):
        if list2[i] == list2[i-1]:
            flag = 1
        i += 1
    
    if (flag):
        return True
    else:
        return False


def hasDuplicates1(list1):
    flag = 0

    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if (list1[i] == list1[j]):
                flag = 1

    if (flag == 1):
        return True
    else:
        return False


def printEvenOdd(n):

    list1 = [x for x in range(n+1)]
    
    list2 = list1[::-1]
    
    for i in range(0,len(list2)):
        if list2[i] % 2 == 0:
            print("Even Number : " , list2[i])
        else:
            print("Odd Number :" , list2[i])


def printEvenOdd1(n):

    while (n > 0):
        if (n % 2 == 0):
            print("Even Number ", n)
        else:
            print("Odd Number", n)

    n = n - 1
printEvenOdd1(10)
