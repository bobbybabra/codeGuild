jobList = ['Programmer','Brain Surgeon','Sandwich Artist','Wallflower']

checkIndex = jobList.index('Sandwich Artist')

# print checkIndex

if 2 == checkIndex:
    print ('Eat Fresh, my friend\n\n')

jobList.append('Standup comedian')

jobList.insert(0,'Americansniper')

for x in  jobList:
    print x

print jobList

list = range(1,21,2)
for x in list:
    print x

###### 		trivia of the day 	###########
## maximum recursion depth isn python is... 1000 ##

tup = range(1,11)
tuple(tup)
print ('the lowest possible score is %d and the highest is %d') % (tup[0],tup[9])
print('a judge can give a gymnist %d points') % tup[9]


