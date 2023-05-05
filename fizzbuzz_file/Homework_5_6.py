f = open('text.txt', 'r')
for line in f:
    fizz, buzz, finish = map(int, line.split(' '))
    for i in range(1, finish + 1):
        if ((not(i % buzz)) and (not(i % fizz))):
            print('FB', end = ' ')
        elif not(i % buzz):
            print('B', end = ' ')
        elif not(i % fizz):
            print('F', end = ' ')
        else:
            print(i, end = ' ')
    print()
f.close()