# Friday Feb 6, 2015 ---- Bobby Babra

#1
print ('Hello World!')

print '\n\n'
#2
list = ['Apples','Oranges','Bananas']

#3
print (list)

#4
list[1] = 'Grapes'

#5
for x in list:
    print x

print '\n\n'
#6
people = {}

people['Bob'] = 22
people['Carol'] = 47
people['Justin'] = 14

# print people.items()

print '\n\n'
#7
def add(a , b):
    print a + b

#8
add(5 , 5)
add(10 , 15)
add(3 , 6)

print '\n\n'
#9
input = input('type an whole number & enter: > ')

while input <= 1000:
    input += 5
    print input

print '\n\n'
#10
nums = range(1,101)
for x in nums:
    if not x % 15:
        print 'fizzbuzz'
    elif not x % 5:
	print 'buzz'
    elif not x % 3:
	print 'fizz'
    else:
        print x

print '\n\n'
#11
class Customer():
    def __init__(self, name, age, location='Washington', creditScore=718):
	self.name = name
	self.age = age
	self.location = location
	self.creditScore = creditScore
#12
j = Customer('Jessie',"")
#13
print (j.name)
#14
print (j.location)
#15
print (j.creditScore)
#16
j.creditScore = 580
print (j.creditScore)

