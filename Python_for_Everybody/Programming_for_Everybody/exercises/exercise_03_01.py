"""
    3.1 Write a program to prompt the user for hours and rate per hour using 
    input to compute gross pay. Pay the hourly rate for the hours up to 40 
    and 1.5 times the hourly rate for all hours worked above 40 hours. Use 
    45 hours and a rate of 10.50 per hour to test the program (the pay 
    should be 498.75). You should use input to read a string and float() to 
    convert the string to a number. Do not worry about error checking the 
    user input - assume the user types numbers properly. 
"""

hrs = input('Enter Hours: ')
rate = input('Enter rates: ')

fh = float(hrs)
fr = float(rate)

if fh > 40:
    reg = fr * fh
    otp = (fh-40.0) * (fr*.5)
    xp = reg + otp
else:
    xp = fr * fh
    
print(f'Pay: {xp}')

# if fh <= 40:
#     xpay = fh * fr
#     print(xpay)
# elif fh > 40: 
#     xt = fh - 40 
#     #print(f'extra time {xt} ')
#     #print(f'1.5 times the hourly rate for all hours worked above 40 hours {xt*(1.5* r)} ')
#     #print(f'{40*r} + {xt*(1.5* r)}')
#     xpay= 40*fr + (xt * (1.5* fr))
#     print(xpay)
