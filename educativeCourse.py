
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


# Dictionaries

# Un ordered dictionary

ages = {}

ages['Tom'] = 28
ages['Peter'] = 36


# ordered dictionary

from collections import OrderedDict

ages_1 = OrderedDict()

ages_1["Thomas"] = 28
ages_1["Peter"] = 36
ages_1["Sam"] = 44


d = {
    0 : [0,0,0],
    1 : [1,1,1],
    2 : [2,2,2]
}

ages = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10,
}


# Nested Dictionary

students = {
    "Peter": {"age": 10, "address": "Lisbon"},
    "Isabel": {"age": 11, "address": "Sesimbra"},
    "Anna": {"age": 9, "address": "Lisbon"},
}


    
Student = {
    "Peter": 10,
    "Isabel": 11,
    "Anna": 9,
    "Thomas": 10,
    "Bob": 10,
    "Joseph": 11,
    "Maria": 12,
    "Gabriel": 10
  }

students = {
      "Peter": {"age": 10, "address": "Lisbon"},
      "Isabel": {"age": 11, "address": "Sesimbra"},
      "Anna": {"age": 9, "address": "Lisbon"},
      "Gibrael": {"age": 10, "address": "Sesimbra"},
      "Susan": {"age": 11, "address": "Lisbon"},
      "Charles": {"age": 9, "address": "Sesimbra"},
  }

def calculateAvg(dict1):
    sum = 0
    length = len(dict1)
    for name, value in dict1.items():
        sum += value
    return sum /length
        
def calculateAvg1(dict1):
    length = len(dict1)
    return (sum(dict1.values()) / length)

def oldestStudent(dict1):
    value = list(dict1.values())
    key = list(dict1.keys())
    return key[value.index(max(value))]


def updateAge(dict1):
    values = list(dict1.values())
    keys = list(dict1.keys())
    
    new_values = []

    for i in range(0,len(values)):
        new_values.append(values[i]+1)
    
    result = {keys[i]:new_values[i] for i in range(len(dict1))}

    return result


def updateAge1(ages,n):
    new_dict = dict()
    for x in ages:
        new_dict[x] = ages[x] + n
    return new_dict


def totalStudents(dict1):
    return len(dict1.keys())

def calculateAverageAge(dict1):

    add_age = 0

    for thing in dict1.values():
        age = thing['age']
        add_age = add_age + age

    return (add_age/len(dict1.keys()))

def findStudents(dict1,place):

    names = []

    for key, subdict in dict1.items():
        for sublist in subdict.values():
            if (sublist == place):
                names.append(key)
    
    return sorted(names)

def findStudents1(dict1,place):
    names = []

    for key, value in dict1.items():
        if value["address"] == place:
            names.append(key)
    
    return sorted(names)

import operator

def sortedDict(dict1):
    return sorted(dict1.items())

a = {0:10,1:20,3:30}
c = dict(a)
c.update({4:40})


dic1={1:10, 2:20} 
dic2={3:30, 4:40} 
dic3={5:50,6:60}

d4 = dict(dic1)
d4.update(dic2)
d4.update(dic3)

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

def createDict(k,v):
    sampleDict = dict(zip(k,v))
    return sampleDict

dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

def mergeDict(dic1,dic2):
    dic3 = dict(dic1)
    dic3.update(dic2)
    return dic3

sampleDict = { 
   "class":{ 
      "student":{ 
         "name":"Mike",
         "marks":{ 
            "physics":70,
            "history":80
         }
      }
   }
}

sampleDict1 = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}


def findNameSalary(dict1):

    name = []
    salary = []

    for i , v in dict1.items():
        if i == 'name':
            name.append(v)
        elif i == 'salary':
            salary.append(v)

    return name,salary


def findNameSalary1(dict1):
    keys = ["name","age"]
    newDict = {k : dict1[k] for k in keys}
    return newDict


def removeKeys(dict1):
    keysRemove = ["age"]
    newDict = {k : dict1[k] for k in dict1.keys() - keysRemove}
    return newDict

sampleDict2 = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

def fidMarks(dict1):
    return min(dict1,key=dict1.get)

sampleDict4 = {
     'emp1': {'name': 'Jhon', 'salary': 7500},
     'emp2': {'name': 'Emma', 'salary': 8000},
     'emp3': {'name': 'Brad', 'salary': 6500}
}

