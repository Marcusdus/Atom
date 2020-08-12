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
	print('Attribute', item['X'])

