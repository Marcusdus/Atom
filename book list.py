# bicycles = ['Marcus', 'Wicliff', 'Bonheur' ]
# print(bicycles)
# print(bicycles[2])
# print(bicycles[0].title())
# print(bicycles[-1])
# message = "I am the king of the jungle as " + bicycles[0].title() +"."
# print(message)

Names = ['rafiki', 'William', 'Aaron' ]
print(Names)
message = "Hey guy, are you ok ? " + Names[0].title()+"."
message1 = "Hey guy, are you ok ? " + Names[1].title()+"."
message2 = "Hey guy, are you ok ? " + Names[2].title()+"."
print(message)
print(message1)
print(message2)

transport = ['Benz', 'Hyundai','ford']
print(transport)

message3 = "My favorite transport is " + transport[0].title()+"."
message4 = "My favorite transport is " + transport[1].title()+"."
message5 = "My favorite transport is " + transport[2].title()+"."
print(message3)
print(message4)
print(message5)

transport[0] = 'Rangerover'
print(transport)


Invitees = ['Gasiza', 'Gedeon', 'Safari']
message6 = "You are invited to our dinner party Mrs:" + Invitees[0].title()+ "!"
message7 = "You are invited to our dinner party Mr:" + Invitees[1].title()+ "!"
message8 = "You are invited to our dinner party Mr:" + Invitees[2].title()+ "!"
print(message6)
print(message7)
print(message8)

Missing = Invitees[1].title() + " is missing,sorry to the information."
print(Missing)

del Invitees[1]
print(Invitees)

Invitees.insert(1, 'Joseline')
print(Invitees)


message9 = "You are invited to our dinner party Mr:" + Invitees[1].title()+ "!"
print(message9)

message10 = " Dinner tables have been expanded,you can book more !!!"
print(message10)

Invitees.insert(0, 'jacson')
Invitees.insert(2, 'Rafiki')
Invitees.insert(4, 'William')

print(Invitees)

message11 = "You are invited to our dinner party Mrs:" + Invitees[0].title()+ "!"
message12 = "You are invited to our dinner party Mr:" + Invitees[2].title()+ "!"
message13 = "You are invited to our dinner party Mr:" + Invitees[4].title()+ "!"

print(message11)
print(message12)
print(message13)


Invitees.pop()
print(Invitees)


Invitees.sort() # sorting list by alphabetic order.
print(Invitees)

Invitees.sort(reverse=True) # sorting a list in reverse order
print(Invitees)

print("\nHere is the list sorted temporarly:")
print(sorted(Invitees)) # temporarly list.

Invitees.reverse() # reverse order
print(Invitees)


Length = len(Invitees) # looking for Length of list
print(Length)





