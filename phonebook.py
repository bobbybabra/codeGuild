'''
simple phonebook using dictionary function
'''

#query = a.lowercase

#if book.has_key(query):
#    print "%s's number is: % query
#    book[query].items

#else:
#    print "%s is not in the dictionary" %query

book={}

book['chris']='555-1212'
book['john']="555-4343"
book['sam']='555-1234'
book['sally']='555-9060'
book['joni']='867-5309'

#print book.items()
#print book.keys()
#print book.values()

query = raw_input('search name: ').lower()

if book.has_key(query):
    print 'ok ma-man here you go: '
    print book[query]

else:
    print "%s is not in the dictionary" %query
#    book.get()[query].value
#dict = {'chris': {'name': 'chris', 'number': '555-1234'}, 'sam': {'name': 'sam', 'number': '555-2345'}

#book[chris]
#get(...)
# |      D.get(k[,d]) -> D[k] if k in D, else d.  d defaults to None.


