f = open('english.txt', 'r')

for elem in f:
   a = elem.split() 

L = []

for id,word in enumerate(a):
    l = []
    l.append(word)
    a.remove(word)
    
    for id,elem in enumerate(a):
        
        if elem in l:
            l.append(elem)
            a.remove(elem)
    L.append(l)

for i in L:
   print(i[0],'-',len(i))    



