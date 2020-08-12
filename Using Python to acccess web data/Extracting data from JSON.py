#Extracting Data from JSON

import json

input = '''
[
{"id" : "001",
  "x" : "2"
  "name" :  "Chuck"
},
{
"id" : "009",
"X" : "7",
"name"": "Chuck"
}
]'''

info = json.loads(input)
print('User count:', len(info))

for item in info:
	print('Name', item['name'])
	print('Id', item['id'])
	print('Attribute' item['X'])

#In this assignment you will write a Python program somewhat similar to http://www.pythonlearn.com/code/json2.py.
#The program will prompt for a URL, read the JSON data from that URL using urllib and then parse and extract the comment counts from the JSON data, compute the sum of the numbers in the file and enter the sum below:
#We provide two files for this assignment. One is a sample file where we give you the sum for your testing and the other is the actual data you need to process for the assignment.

#I do not guarantee this is the solution to the actual assignment, as this differs from time to time.

import json
import urllib
count = 0

url = "http://python-data.dr-chuck.net/comments_283400.json"
print "retrieving URL. Stand by."
uh = urllib.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	#print item["count"]
	number = int(item["count"])
	count = count + number


import urllib.request, urllib.parse, urlib.errors
import json

serviceul = ''

while True:
	address = input('Enter location: ')
	if len(address) <1: break

	url = serviceurl + urllib.parse.urlencode({'address': address})

	print('Retrieving', url)
	uh = urllib.request.urlopen(url)
	data = uh.read().decode()
	print('Retrieved', len(data), 'character')

	try:
		js = json.loads(data)
	except:
		js = CERT_None
