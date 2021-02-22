values = ["a","b","c"]

for value in values:
    print(value)

index = 0
# With index
for value in values:
    print(index,value)
    index += 1
# With range
for index in range(len(values)):
    value = values[index]
    print(index,value)
# With enumerate
for count, value in enumerate(values):
    print(count,value)

list2 = ["Python","is","fun"]
# One more example of enumerate
for index, value in enumerate(list2):
    print(index,value)

users = ["user 1","user 2", "user 3"]

for index, value in enumerate(users, start=1):
    if index % 2 == 0:
        print("Even Users  :", value)
    else:
        print("Odd Users :", value)
    
def even_items(iterable):
    return [v for i , v in enumerate(iterable, start=1) if  i % 2 == 0]

seq = list(range(1,11))

print(seq)

print(even_items(seq))
