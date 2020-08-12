score = input("Enter Score:")
try:
    S = float(score)
    if S <= 1.0 and S >= 0.0:
       if S >= 0.9:
          print('A')

       elif S >= 0.8:
            print('B')

       elif S >= 0.7:
            print('C')

       elif S >= 0.6:
            print('D')

       elif S < 0.6:
            print('F')

except:
    print('Error')
