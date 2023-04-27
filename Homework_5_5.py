suma = int(input())
s = [10,20,50,100,200,500,1000]
for id, nom in enumerate(s):
	while suma:
		suma = suma % (nom * 10)
		if suma < s[id + 1]:
			


