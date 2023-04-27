suma = int(input())
s = [1000,500,200,100,50,20,10]
for nom in s:
  print(suma // nom, f'купюр номіналом {nom} грн')
  suma = suma % nom