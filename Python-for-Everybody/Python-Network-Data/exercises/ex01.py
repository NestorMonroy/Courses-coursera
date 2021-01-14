"""
    In this assignment you will read through and parse a file with text and numbers. You will extract all 
    the numbers in the file and compute the sum of the numbers. 
 
"""
import re
fname = input('Enter file: ')
if len(fname) < 1 : fname = 'regex_sum_1129444.txt'
handle = open(fname)
nlist = list()

# for line in handle:
#     if re.search('[0-9]+', line):
#         xnum = re.findall('[0-9]+',line)
#         nlist.append(xnum)

#final = [int(val) for sublist in nlist for val in sublist]
#print(final)
#print(sum(final))

"""
"""
# for line in handle:
#     xnum = re.findall('[0-9]+',line)
#     if len(xnum) < 1 : continue

#     for i in range(len(xnum)):
#         num = int(xnum[i])
#         nlist.append(num)

# # print(nlist)
# print(len(nlist))
# print(sum(nlist))

"""
"""

for line in handle:
    xnum = re.findall(r'[0-9]+', line)
    nlist = nlist + xnum

num = [int(nlist) for nlist in nlist]
    
#print(num)
print(sum(num))
# total = 0
# for ynum in num:
#     total = total+ ynum

# print(total)