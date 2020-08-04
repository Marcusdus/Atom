Kigali = []

Kigali.append('Kicukiro')
Kigali.append('Gasabo')
Kigali.append('Nyarugenge')

for district in Kigali: # looping our equation.
    print(district)
    print(district.title() +", best city!")
    print("districts of our city, " + district.title() +".\n")

for value in range(1,5): # using range in looping.
    print(value)

numbers = list(range(1,6)) # converting range into list.
print(numbers)

even_numbers = list(range(2,11,2)) #In this example, the range() function starts with the value 2 and then adds 2 to that value.
print(even_numbers)


square = []
for value in range(1,11):
    square = value**2
    squares.append(square)

    print(squares)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, ]
min(numbers)
max(numbers)
sum(numbers)

# Quiz 4

squares = [value**2 for value in range (1,11)]
print(squares)

for value in range(0,21):
    print(value)

numbers1 = list(range(1,1000000))
for i in numbers1:
    print(i)

minimum = min(numbers1) # minimum value in the list.
maximum = max(numbers1) # maximum value in the list.
summation = sum(numbers1) # summation value in the list.

print(minimum)
print(maximum)
print(summation)

Oddnumber = list(range(0,20,1)) # list of the odd numbers
for n in Oddnumber:
    print(n)

multiplethree = list(range(2,31,3)) # list of multiple of 3
for t in multiplethree:
    print(t)

cube1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for z in cube1:
    cube3 = z**3  # generate cubic of list values.
    print(cube3)

print(Kigali[0:3]) # slicing of list.
print(Kigali[2:])

Kigalivillage = Kigali[:] # copying of list.
print(Kigalivillage)

Kigali.append('Rugende')
Kigalivillage.append('Kabuga')

print(Kigali)
print(Kigalivillage)
