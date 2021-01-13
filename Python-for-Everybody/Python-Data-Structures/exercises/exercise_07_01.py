"""
    Write a program that prompts for a file name, then 
    opens that file and reads through the file, and print the 
    contents of the file in upper case. Use the file words.txt 
    to produce the output below.
"""

fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opended', fname)
    quit()

for line in fhand:
    line = line.strip().upper()
    print(line)