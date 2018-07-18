
d = {'people': [{'first_name': 'Robin'}, {'first_name': 'John'}], 'version': 1}
print (d)
print ('\n')

l2 = []

for x1 in d['people']:
    l2.append(x1)

#l2.append(d['people'][0])
#l2.append(d['people'][1])
#end
	
print (l2)
print ('\n')

l3 = []
for x2 in d['people']:
   l3.append({ 'first_name': x2['first_name'], 'last_name': 'Smith'})

#l3.append({'first_name': d['people'][0]['first_name'], 'last_name': 'Smith')
#l3.append({'first_name': d['people'][1]['first_name'], 'last_name': 'Smith')
#end
   
print (l3)
print ('\n')