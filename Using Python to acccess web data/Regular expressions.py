import re
x = 'My 2 favorite numbers are 19 and 42'
y = re.findall('[0-9]+' ,x) # looking for digits.
print(y)

y = re.findall('[AEIOU]+' ,x) # looking for capital letters.
print(y)

x1 = 'From: using the : character'
y1 = re.findall('^F.+:', x1)
print(y1)

x2 = From marcus.duh@cst.ur.rw Sat Jan 5 09:14:16 2008
y2 = re.findall('\S+@\S+',x2) # S is for non blink space character.
y3 = re.findall(^From (\S+@\S+)' ,x) () # brackets help to extract without From
print(y3)

words = line.split() # using other techniques for extracting by splitting method.
email = words[1]
pieces = email.split('@')
print(pieces[1])

x3 = 'From marcus.duh@cst.ur.rw Sat Jan 5 09:14:16 2008'
y3 = re.findall('@([^ ]*)',x3) # @ for extracting
print(y3)

hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) !=1 : continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlio))
