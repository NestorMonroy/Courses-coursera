import re

#Matching and extractind Data
#[0-9]+ One or more digits
#When use re.findall() it returns a list of zero or more sub-strings that match the regular expresion
x = 'My 2 favorite numbers are 19 and 43'
y = re.findall('[0-9]+', x)
#print(y)

x = 'My 2 favorite numbers are 19 and 43'
y = re.findall('[AEIOU]', x)
#print(y)

#The repeat characters (* and +) push outward in both directions (greedy) to match the largest possible string

x='From: Using the: character'
y= re.findall('^F.+:', x)
#print(y)

#Non-Greedy Matching -> Not all regular expresion repeat codes are greedy. 
#If you add a ? character, the + and * chill out a bit

x='From: Using the: character'
y= re.findall('^F.+?:', x)
#print(y)

#You can refine the match for re.findall() and separately determine which of the match is to be stracted by using parentesis
# \S+@\S+ => At least one non-whitespace character

x='Another From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y= re.findall('\S+@\S+', x)
#print(y)

#Fin-Tuning String Extraction
#Parentheses are not part of match - but they tell where to start and stop what string to stract

x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y= re.findall('^From (\S+@\S+)', x)
#print(y)

#'@([^ ]*) 
#Look through the string until you find an at sign
#[^ ] Match non-blank character, (*) Match many of them , () Extract the non-blank characters
data ='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', data)
#print(y)

#Event cooler Regex Version

# . => Skip a bunch of characteres, @ => looking for an at string
lin = 'From blabla stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('^From .*@([^ ]*)',lin)
print(y)

