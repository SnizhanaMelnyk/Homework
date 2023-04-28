suma = int(input())
s = [10,20,50,100,200,500,1000]
suma_n = suma

while suma_n: 
  
  for id, nom in enumerate(s):
    
    k = suma // nom 
   
    if k > 10:
      k = 10
     
    elif k < 1:
      print('no')
      break
    suma_n = suma - (nom * k)  
    
       
    while suma_n % s[id + 1] :
      
      k -= 1
      suma_n = suma - (nom * k)
    suma = suma_n
    print(k, str(nom))
