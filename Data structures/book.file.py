with open('words.txt') as file:
    contents = file.read()
    print(contents)

file_path = 'E:\MOOCs\Python specialisation\Atom\words.txt'
with open(file_path) as file_object:

with open(filename) as file_object:
    for line in file_object:
        print(line)
        print(line.rstrip())

lines = contents.readlines()  # reading lines inside file.

for line in lines:
    print(line.rstrip())

file1 = 'programming.txt' # creating a new file.

with open(file1, 'w') as docs:
    docs.write('I love programming.') # write a new line
    docs.write('I love creating new games.\n')


# Quiz 8

Names = input("Enter your name: ")
file2 = 'guest.txt'
with open(file2, 'w') as docs1:
    file2.write(Names)


Names1 = input("Enter your name: ")
file3 = 'book.txt'

for line in file3:
    with open(file3, 'w') as docs2:
        file3.write(Names1)
        print("Greeting Mr :", Names1)


try:
    print(5/0)
except ZeroDivisionerror: # error of dividing with zero.
    print("You can`t divide by zero!")


print("Give me two numbers, and i`ll divide them.")
print("Enter 'q' to quit.")

while True: # making a simple calculator
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number:")
    if second_number == 'q':
        break
    answer = int(first_number) / int(second_number)
    print(answer)

filename = 'alice.txt'

try:
    with open(filename)as file_object:
        contents = f_obj.read()
except FileNotFoundError:
    msg = "Sorry, the file " + filename + "does not exist."
    print(msg)

else:
    words = contents.split()
    num_words = len(words) # count number of words in text.
    print("The file " + filename + "has about " + str(num_words)+ "words.")





def count_words (filename):
    """ Count the approximate number of words in a file."""
    try:
        with open(filename)as file_object:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + "does not exist."
        print(msg)

    else:
        words = contents.split()
        num_words = len(words) # count number of words in text.
        print("The file " + filename + "has about " + str(num_words)+ "words.")

filename = 'alice.txt'
count_words(filename)



file3 = with open()

with open (filename, 'a')as file_object: # Open file in appending mode for adding on existing file.
    file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write(" I love creating apps that can run in a browser.\n")

try:
    x = input("Give me a number: ")
    x = int(x)

    y = input("Give me another number: ")
    y = int(y)

except ValueError:
    print("sorry,I really needed a number")

    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
