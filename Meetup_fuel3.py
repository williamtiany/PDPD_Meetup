import requests
import feedparser
import pprint

#create empty dictionaries
d1 = {}
d2 = {}

#parse feeds of today and tomorrow
d1 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?&Day=today')
d2 = feedparser.parse('http://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?&Day=tomorrow')

#create empty list
l_trim = []

#fill list with each element as dictionary of: <price>, <location>, <brand>, address, <date>=*day*
for loop_addentry in d1.entries:
    l_trim.append({'price': loop_addentry['price'], 'location': loop_addentry['location'], 'address': loop_addentry['address'], 'brand': loop_addentry['brand'], 'day': 'today'})

for loop_addentry in d2.entries:
	l_trim.append({'price': loop_addentry['price'], 'location': loop_addentry['location'], 'address': loop_addentry['address'], 'brand': loop_addentry['brand'], 'day': 'tomorrow'})

#sort by l_trim by key: <price>
def sorted_price(dkey):
    return dkey['price']
	
l_sorted = sorted(l_trim, key=sorted_price)

print (l_sorted[0])
print ('\n')

#Create and populate HTML file
strTable = '''
<table>
    <tr>
        <th scope="col">Price</th>
        <th scope="col">Location</th>
        <th scope="col">Address</th>
        <th scope="col">Brand</th>
        <th scope="col">Day</th>
    </tr>
'''

#Create increment
strTablerow = ""

for loop_Tablerow in l_sorted:
	strTablerow = '''
	<tr>
		<td> {first} </td>
	<tr>
	'''.format(first= 'price')
	
strTable= strTable + strTablerow

#Write strTable to html file 'fuelsortsite.html'
file = open('fuelsortsite.html', 'w')
file.write('strTablerow')#calling a string
file.close()