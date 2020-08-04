Largest = None
smallest = None
while True:
    try:
        num = raw_input("Enter a number: ")
        if num == 'done':
            break
        num = int(num)
        if largest is None or largest < num:
              largest = num
        elif smallest is None or smallest > num:
              smallest = num

    except :
        print ("Invalid Input")
        continue

print ("Maximum number is ", largest)
print ("Minimum number is ", smallest)
