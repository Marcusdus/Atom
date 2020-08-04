H = input ("Enter Hours:")
R = input ("Enter Rate:")

HI = float(H)
RI = float(R)

def computepay (Product):
    Product = HI * RI
    return Product

def computepay1 (Product1):
    Product1 = HI * RI
    Otp = (HI - 40.0) * (RI * 0.5)
    XP = Prd + Otp
    return XP

if HI < 40:
   print("Pay", computepay('Product'))

else:
      print("Pay", computepay1('Product1'))
