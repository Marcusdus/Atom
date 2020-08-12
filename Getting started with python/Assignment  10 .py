fname = input("Enter file name:")
fh = open(fname)
count = 0
average = 0
for line in fh:
    if not line.startswitch ("X- DSPRAM- confidence:") : continue
    average +=float(line[20:-1].strip())
    count = count + 1

print("Average spam confidence:", (average/count))
