Kiyovu = {'Juvenal': 5, 'Theodore': 1, 'Hemedi': 2} # creating dictionary
print (Kiyovu)

Umuguzi = Kiyovu['Juvenal']
print("Umuntu wo mu ikipe yaguze million  " + str(Umuguzi) + " bus yiyo ikipe")

Kiyovu['Alex'] = 3
Kiyovu['Claude'] = 4
print(Kiyovu)


Rayonsport = {}  # creating a dictionary from scratch
Rayonsport['Rugwiro'] = 2   # adding element of dictionaries.
Rayonsport['Mudgeni'] = 6
Rayonsport['sugira'] = 9
Rayonsport['sadate'] = 'President'
print(Rayonsport)

del Rayonsport['sadate']    # remove a key-value paired value
print(Rayonsport)

favoritelanguage = {
      'Jen': 'Python',
      'sarah':'C',
      'edward' : 'ruby',
      'Phil' : 'Python'
}

print("Sarah favorite language is " + favoritelanguage['sarah'].title() + ".")

Quiz 6

Identity = {
    'Firstname' : 'Dushimirimana',
    'lastname' : 'Marcus',
    'age': 25,
    'city': 'Kigali1'
    }

for K, V in Identity.items(): # looping dictionary
    print(K )
    print(V)

favoritelanguage = {
      'Jen': 'Python',
      'sarah':'C',
      'edward' : 'ruby',
      'Phil' : 'Python'
     }
for key, Value in  favoritelanguage.items(): # Looping of key and value dictionaries
    print(key.title() + " favorite language is " + Value.title() + ".")

for key in favoritelanguage.keys(): # looping of the key only in dictionaries.
    print(key.title())

for key in sorted(favoritelanguage.keys()): # looping of the key only  in order for dictionaries.
    print(key.title() +", good, you did good job.")

for values in favoritelanguage.values(): # looping of the key only in dictionaries.
    print(values.title())

# Quiz 7:

River = {'Nile' : 'Egypt', 'Congnile' : 'RDC', 'Akanyaru' : 'Burundi'}

for Key, Value in River.items():
    print("The " + Key.title() + " runs through " + Value.title() + ".")

for key in River.keys():
    print(key)

for value in River.values():
    print(value)

sisters = [] # create  an empty

for Ynumber in range(30):  # creating a list of 30 dictionaries
    Ynumber = {'color': 'green', 'points' : 5, 'speed': 'slow'}
    sisters.append(Ynumber)

for z in sisters[:5]:
    print(z)

print("...")

for alien in aliens
