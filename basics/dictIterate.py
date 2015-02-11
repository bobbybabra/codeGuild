people = {}

people['Bob'] = 22
people['Carol'] = 47
people['Justin'] = 14

for i, k in people.items():
    print (i,k)

#for i in people.keys():
#    print (i)

list(people.keys())
print people.keys()

# print(people)
people = {}

########### from quiz solution, this dict is not formatted
#### correctly, but the point is down below on iterating through
### the dict when there is a dict w/in the dict
## see kevin long's script

people['Bob'] = {age:22}
people['Carol'] = {age:47}
people['Justin'] = {age:14}

# for (i, k) in (people.keys(), people):
#    print (i + people.get(k))
for i, j in people.values():
    print i + j
#for i in people.keys():
#    print (i)

list(people.keys())
print people.keys()

# print(people)

for index, person in people.items():
    print index, person['age']
people = {}

people['Bob'] = 22
people['Carol'] = 47
people['Justin'] = 14

for i, k in people.items():
    print (i,k)

#for i in people.keys():
#    print (i)

list(people.keys())
print people.keys()

# print(people)
