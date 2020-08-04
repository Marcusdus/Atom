H = input ("Enter Hours:")
R = input ("Enter Rate:")


try:

    HI = float(H)
    RI = float(R)

except:
    print ("Error,please correct")

print(HI, RI)

if HI > 40 :
    Prd = HI * RI
    Otp = (HI - 40.0) * (RI * 0.5)
    xp = Prd + Otp

else :
    xp = HI * RI

print(xp)
