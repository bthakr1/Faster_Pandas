
candies = [2,3,5,1,3]

extraCandies = 3

def kidsWithCandies(candies,extraCandies):
    maxCandies = max(candies)
    result = []
    for i in range(len(candies)):
        if candies[i] + extraCandies >= maxCandies:
            result.append(True)
        else:
            result.append(False)
    return result

def inplaceKidsWithCandies(candies,extraCandies):
    return [candy + extraCandies >= max(candies) for candy in candies]
