
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

myList = [1,4,8,5]

sum = 0

for value in myList:
    sum += value
print(sum)