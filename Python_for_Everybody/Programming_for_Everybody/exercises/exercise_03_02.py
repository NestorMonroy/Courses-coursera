hrs = input('Enter Hours: ')
rate = input('Enter rates: ')

try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()

print(fh, fr)
if fh > 40:
    reg = fr * fh
    otp = (fh-40.0) * (fr*.5)
    xp = reg + otp
else:
    xp = fr * fh
    
print(f'Pay: {xp}')