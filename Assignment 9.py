text = "X-DSPAM-Confidence:    0.8475"
ipos = text.find('0')
print(ipos)
# Number = str[ipos:]
ipus = text.find('5')
print(ipus)

result = text[23:]
print(result)
decimal = float(result)
print(decimal)
