import requests
import feedparser
import pprint

##Step 1 - Pull RSS feed and check data
##S1.1 How to parse using requests 
##S1.1.1 import WHOLE rss feed data##

r = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')
	
##S1.1.2 save parsed string as dictionary 'd_raw'
d_raw = feedparser.parse(r.text)
	
##S1.1.3 print out d_raw using print
print(d_raw)