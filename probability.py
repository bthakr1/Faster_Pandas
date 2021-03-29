# Probability

# Reference 

# https://www.youtube.com/watch?v=CAtUFfkbKjY

# Total Number of Cards : 52
# Total Number of Red : 26
## Hearts : 13
### K, Q, J : 3
### 2-10 : 9
### A : 1
## Diamonds : 13 
### K, Q, J : 3
### 2-10 : 9
### A : 1
# Total Number of Black : 26
## Spades : 13
### K, Q, J : 3
### 2-10 : 9
### A : 1
## Club : 13
### K, Q, J : 3
### 2-10 : 3
### A : 1
import math 

def factorial(n):

    factorial = 1

    if n < 0 :
        print("Sorry, Factorial does not exists for negative number")
    elif n == 0:
        return 1
    else:
        for i in range(1,int(n)+1):
            factorial = factorial * i
        return factorial

# Functional to calculate Permutation : Order Matters

def nPr(n,r):
    if n < 0 or r < 0:
        print("Wrong Arguments")
    else:
        return math.floor(factorial(n)/factorial(n-r))

# Function to calculate Combination : Order Does not Matter

def nCr(n,r):
    return math.floor(factorial(n)/(factorial(r)*factorial(n-r)))


# What is the Probability of Being Dealth with 4 Face Cards and 1 Ace
# There are 12 Face Cards
# There are 4 Ace Cards

print("Number of ways of getting a 4 Face Cars AND 1 Ace is : ", nCr(12,4)*nCr(4,1))

# What is the Probability of Being Dealth with a KING Followed by An Ace
# Not replacement
# There are 4 Kings
# There are 4 Aces 

print("Probability of getting a King followed by an Ace : ", "{0:.4f}".format(((4/52)*(4/51))))

# Probability of getting a Diamond or a King
# Diamond : 13
# King : 4
# King of Diamond : 1
# OR means both
# AND means intersection

print("Probability of getting a diamond OR a king : ", (13/52)+(4/52)-(1/13))