import re

hand = open("regex_sum_42.txt")
x=list()
for line in hand:
     y = re.findall('[0-9]+',line)
     x = x+y

sum=0
for z in x:
    sum = sum + int(z)

print(sum)

Extracting Data from JSON

#In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py.
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#I do not guarantee this is the solution to the actual assignment, as this differs from time to time.

import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read()

info = json.loads(data)
#print(info) #to see the info dictionary/object
#print(json.dumps(info, indent=2))

count = 0
sum = 0

for item in info['comments']:
    num = item['count']
    sum = sum + int(num)
    count = count + 1

print('Count: ', count)
print('Sum: ', sum)



import urllib.error, urllib.request, urllib.parse
import json

target = 'http://py4e-data.dr-chuck.net/json?'
local = input('Enter location: ')
url = target + urllib.parse.urlencode({'address': local, 'key' : 42})

print('Retriving', url)
data = urllib.request.urlopen(url).read()
print('Retrived', len(data), 'characters')
js = json.loads(data)
print(json.dumps(js, indent = 4))
print('Place id', js['results'][0]['place_id'])
