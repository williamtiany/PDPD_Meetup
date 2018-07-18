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
for entrystep in d1.entries:
    l_trim.append({'price': entrystep['price'], 'location': entrystep['location'], 'address': entrystep['address'], 'brand': entrystep['brand'], 'day': 'today'})

for entrystep in d2.entries:
	l_trim.append({'price': entrystep['price'], 'location': entrystep['location'], 'address': entrystep['address'], 'brand': entrystep['brand'], 'day': 'tomorrow'})

print (l_trim[0])
print ('\n')	

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
	
	