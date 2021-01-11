
handle = open('mbox.txt')
print(handle)

#File handle as a sequence
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)


fhand = open('mbox.txt')
count = 0

for line in fhand:
    count += 1

print('Line count: ', count)
print('*' * 50)
#Reading the *Whole* File
fhand = open('mbox-short.txt')
inp = fhand.read()
print(len(inp))

print(inp[:20])
print('*' * 50)

#blank line The print statement adds a newline to each line
fhand = open('mbox-short.txt')
for line in fhand:
    if line.startswith('From'):
        print(line)

print('*' * 50)


#strip remove the new line
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.strip()
    if line.startswith('From'):
        print(line)

print('*' * 50)


#Searching Through a File (Fixed)

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From'):
        print(line)

#Skiping with continue
print('*' * 50)
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From'):
        continue
    print(line)


#Using in to Select Lines

print('*' * 50)
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not '@uct.az.za' in line:
        continue
    print(line)

#Prompt for  File Name

fname = input('Enter the file name')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject'):
        #count = count +1
        count +=1
print('There were', count, 'subject lines in', fname)


#Bad files name

fname = input('Enter the file name')
try:
    fhand = open(fname)
except:
    print('File cannot be opended', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('Subject'):
        #count = count +1
        count +=1
print('There were', count, 'subject lines in', fname)
