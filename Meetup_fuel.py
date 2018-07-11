import requests
import feedparser
import pprint

##STEP 1 - Pull RSS feed and check data

#S1.1 Parse using just feedparser
d = 0
d = feedparser.parse('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')

#S1.1.0 Check feed
print (d.feed.title)
print (d.feed.subtitle)
print ("\n")

'''#Alternative 1.1# Use requests and feedparser
r = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')

##S1.1.2 Save parsed data as dictionary 'd'
d = feedparser.parse(r.text)

'''

'''#Optional 1.1# Pprint to check data
##S1.3 print out d using pprint
pprint.pprint(d,indent = 4)
'''

#Optional 1.2# Print each key in d
print ("Keys in d are " + str(d.keys()))

#Optional 1.3# Print the class/type of each key in d
# Also print number of entries if list or dictionary
for key in d:
    if type(d[key]) is list:
	    print (key + " is type " + str(type(d[key])) + " with " + str(len(d[key])) + " entries.")
    
    elif type(d[key]) is dict:
	    print (key + " is type " + str(type(d[key])) + " with " + str(len(d[key])) + " entries.")
	
    else: 
	    print (key + " is type " + str(type(d[key])))
print ("\n")

##STEP 2 - Make new dictionary with relevant data

#Optional 2.1# Print example entry
print (d.entries[0])
print ("\n")

#Optional 2.2# Print each key in d.entries[0]
print ("Keys in d.entries[0] are " + str(d.entries[0].keys()))

#Optional 2.3# Print the class/type of each key in d.entries[0]
# Also print number of entries if list or dictionary
for key in d.entries[0]:
    if type(d.entries[0][key]) is list:
	    print (key + " is type " + str(type(d.entries[0][key])) + " with " + str(len(d.entries[0][key])) + " entries.")
    
    elif type(d.entries[0][key]) is dict:
	    print (key + " is type " + str(type(d.entries[0][key])) + " with " + str(len(d.entries[0][key])) + " entries.")
	
    else: 
	    print (key + " is type " + str(type(d.entries[0][key])))
print ("\n")


##STEP 3 - Trim Data

#S3.1 Create List with <price>, <location>, <address>, <brand>
l_trim = []

#S3.2 ?Append dictionary elements from d.entries[x] into new list?
#how to point list 

for entrystep in d.entries:
    l_trim.append({'price': entrystep['price'], 'location': entrystep['location'], 'address': entrystep['address'], 'brand': entrystep['brand']})

'''Test append everything 
for entrystep in d.entries:
    l_trim.append({'price_trim': d.entries['price'], 'location_trim': d.entries['location'], 'address_trim': d.entries['address'], 'brand_trim': d.entries['brand']})
'''
	
#Optional 3.1# Print example entry for l_trim
print (l_trim[0])
print("\n")


'''#S3.2 Sort list by price
l_trim = l_trim.sort(key=lambda x: x[1])

#Alternative 3.2 Sort DICTIONARY by price
for key, value in sorted(mydict.iteritems(), key=lambda (k,v): (v,k)):
    print "%s: %s" % (key, value)

source: https://www.saltycrane.com/blog/2007/09/how-to-sort-python-dictionary-by-keys/
'''

'''def sorted_price(d):
    return d['price']
	
l_trim_s = sorted(l_trim, key=sorted_price)
'''