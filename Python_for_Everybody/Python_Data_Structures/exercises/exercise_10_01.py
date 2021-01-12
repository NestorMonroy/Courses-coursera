fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = {}

for line in handle:
    line = line.strip()
    wds = line.split()

    for w in wds:
        # idiom: retrive/ create/ update counter
        di[w] = di.get(w, 0) + 1

#print(di)
# x = sorted(di.items()) 
# print(x[:5])

tmp = []
for k, v in di.items():
    #print(k,v)
    newt = (v, k)
    tmp.append(newt)

#print('Flipped',tmp)
#tmp = sorted(tmp)
tmp = sorted(tmp, reverse=True)
#print('Sorted', tmp[:5])

for v, k in tmp[:5]:
    print(k,v)