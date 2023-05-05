f = open('text.txt', 'r')
L = []
for line in f:
    fizz, buzz, finish = map(int, line.split(' '))
    l = []
    for i in range(1, finish + 1):
        if ((not(i % buzz)) and (not(i % fizz))):
            l.append('FB')
        elif not(i % buzz):
            l.append('B')
        elif not(i % fizz):
            l.append('F')
        else:
            l.append(i)
    L.append(l)
print(L)
f.close()	

f = open('text1.txt', 'w')
for l in L:
    print(' '.join([str(elem) for elem in l]), file = f)
f.close()