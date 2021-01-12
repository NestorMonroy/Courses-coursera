fname = input('Enter file: ')
if len(fname) < 1 : fname = 'clown.txt'
handle = open(fname)

di = {}

for line in handle:
    line = line.strip()
    #print(line)
    wds = line.split()
    #print(wds)

    for w in wds:
        #print(w)
        #print('**', w, di.get(w, -99))
        # if the key is not there the count is zero
        #oldcount = di.get(w,0)
        #print(w, 'old', oldcount)
        #newcount = oldcount + 1
        #di[w] = newcount
        # idiom: retrive/ create/ update counter
        di[w] = di.get(w, 0) + 1
        #print(w, 'new', di[w] )
        #print(w, 'new', newcount)
        # if w in di :
        #     di[w] = di[w] + 1
        #     #print('**Existing**')
        # else:
        #     di[w] = 1
        #     #print('***New***')
        # #print(di[w])

#print(di)


#now we want to find the most common word
largest = -1
theword = None
for k, v in di.items():
    #print(k,v)
    if v > largest:
        largest = v
        theword = k #cature/remember the word thar was largest

print('Done',theword, largest)